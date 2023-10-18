"""
This is a fake module, inteded to provide autocompletion and proper type hints
All classes are built using Harmony's python documentation :
https://docs.toonboom.com/help/harmony-22/scripting/pythonmodule/index.html

Author:
Tristan Languebien (tlanguebien@gmail.com)
"""

from typing import List

class PythonFunction(tuple):
    def __init__(self):
        super().__init__()

class BaseObject(tuple):
    pass

class ListObj():
    pass

class IterableObj():
    pass

class Project(BaseObject):
    """
    Generic Project wrapper - overridden as needed for the appropriate application.

    The Object Model Core's Project wrapper. Used to wrap the currently loaded project in the application and provides access to the properties and children of the project.
    """
    def __init__(self):
        super().__init__()
    
    @property
    def dirty(self) -> bool:
        """
        Identifies if the project is currently in a dirty state (has it been modified).

        When an action modifies the project, the project is marked as dirty. Undoing the operations, or saving, will result in the project no longer being dirty.

        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        harmony.open_project( "path/to/project.xstage" )
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project
        history = proj.history
        print( "Dirty: %s"%proj.dirty )                              #Expecting "Dirty: False", since the scene was just opened above.
        scn  = proj.scene
        top  = scn.top
        new_node = top.nodes.create( "PEG", "PEG_001" )
        print( "Dirty: %s"%proj.dirty )                              #Expecting "Dirty: True", since a node was added.
        history.undo( len(history) )                                 #Undo everything in the history, to return to the start state.
        print( "Dirty: %s"%proj.dirty )                              #Expecting "Dirty: False", since everything was undone.
        ```
        """
        return True
        
    @property
    def dirty_previously(self) -> bool:
        """
        Identifies if the project has ever been in a dirty state (has it ever been modified).

        When an action modifies the project, the project is marked as dirty. Undoing the operations, or saving, will result in the project no longer being dirty.

        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        harmony.open_project( "path/to/project.xstage" )
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project
        history = proj.history
        print( "Dirty: %s"%proj.dirty )                              #Expecting "Dirty: False", since the scene was just opened above.
        scn  = proj.scene
        top  = scn.top
        new_node = top.nodes.create( "PEG", "PEG_001" )
        print( "Dirty: %s"%proj.dirty )                              #Expecting "Dirty: True", since a node was added.
        proj.save_all()
        print( "Dirty: %s"%proj.dirty )                              #Expecting "Dirty: False", since everything was saved.
        print( "Dirty Prev: %s"%proj.dirty_previously )              #Expecting "Dirty Prev: True", since something was done at some point.
        ```
        """
        return True
        
    @property
    def history(self):
        """
        The undo history of the application. Can be used to undo and redo commands in the history.

        The history is useful for undoing, redoing, and creating undo-states in the application's history.

        Creating an Undo State:
        ```python
        import math
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        sess.notify_enabled = False                                  #Disable application events, so everything happens under-the-hood, quickly.
        proj    = sess.project
        scn     = proj.scene
        top     = scn.top
        history = proj.history
        history.begin( "Unnecessary Peg Spiral" )                    #All subsequent peg creation commands will be accumulated into this history item.
        times_around = 3.0
        for n in range( 1000 ):                                      #Create 1000 pegs -- for fun!
        perc = ( n / 1000.0 )
        rad  = perc * 2.0 * math.pi * times_around                 #Time to be fancy!
        dist = 300.0 * perc
        new_node = top.nodes.create( "PEG", "PEG_%04d"%(n) )
        new_node.position.x = math.cos( rad ) * dist
        new_node.position.y = math.sin( rad ) * dist
        history.end()                                                #This history item will be closed, and actions are no longer accumulated.
        sess.notify_enabled = True                                   #Reenable application events to see all 100 fancy new pegs (in record time!)
        ```
        
        Undoing the Last State:
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj    = sess.project
        history = proj.history
        history.undo()                                               #Why did we just create 1000 pegs in a spiral? Undo it!
        ```
        """
        return History()
        
    @property
    def resolution(self):
        """
        Get the resolution properties of the scene.

        The OMC::ProjectResolution object allows for read/write access to the current project's resolution and related project settings. Setting a New Resolution:

        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj       = sess.project
        resolution = proj.resolution
        print( "Current Resolution: %s x %s"%(resolution.x, resolution.y) )
        resolution.x = 2578
        resolution.y = 1080
        print( "New Resolution: %s x %s"%(resolution.x, resolution.y) )   #Expected result: "New Resolution: 2578 x 1080"
        ```
        """
        return ProjectResolution()

class Preferences(BaseObject):
    """
    The user preferences for the application.

    The preference handler for the application provides read and write access to the current application preferences. This is useful for storing and modifying tool preferences.

    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    prefs = sess.preferences                                     #Get preferences handler.
    prefs["PEG_DEFAULT_SEPARATE_POSITION"] = True                #Expectation: The Peg default separate position preference will now be set to true.
    ```
    """
    def __init__(self):
        super().__init__()
        
    def __getitem__(self, name:str):
        """Get and set a preference by name."""
        return PreferencePair()
    
    def list(self):
        """Convert the dynamic list into a static list of preference items."""
        return [PreferencePair]
    
    def value(self, key:str, defaultValue):
        """Get a preference value with a default value as a fallback if that key doesn't exist."""
        return
    
    def replace(self, key:str, item):
        """Replace a preference at the given key with a value – an error will occur if the preference types don't match."""
        return
    
    def type(self, key:str) -> str:
        """Identify the type of preference at the given key."""
        return ""
    
    def reset(self, key:str) -> bool:
        """Reset the preference to its default value."""
        return True

class Javascript(BaseObject):
    """
    An interface for providing access to javascript classes and functions.

    The Javascript interface can be used to call javascript methods in the application. It can also be used to maintain a JS environment form within Python.

    Note: In order to maintain the interface between Javascript and Python, the Javascript code and its resulting objects remain persistent within Javascript when loaded through Python. This allows for a consistent level of persistence between Python and Javascript.
    ```python
    from ToonBoom import harmony
    sess = harmony.session()
    js = sess.javascript
    #Original Javascript
    js_script = "var getFrame = function(){ return frame.current(); }; var setFrame = function(setValue){ frame.setCurrent( setValue ); };"
    #Evaluated Javascript -- this will not contain the evaluated JS code.
    wrapped_js = js.load_string(js_script)
    #Use the getFrame function to return the current frame within the environment, via Javascript.
    current_frame = wrapped_js["getFrame"].call()
    print( "Current Frame : %s"%current_frame )
    next_frame = current_frame + 1
    print( "Setting Next Frame : %s"%next_frame )
    wrapped_js["setFrame"].call( [next_frame] )
    ```
    """
    def __init__(self):
        super().__init__()
    
    def evaluate(self, javascript:str):
        """
        Evaluate a javascript string and return the results.

        Evaluates a string in javascript and returns the resulting object. To evaluate with arguments, use call_function() method instead.

        Evaluate Javascript - inspect it in Python

        ```python
        from ToonBoom import harmony
        sess = harmony.session()
        js = sess.javascript
        eval_script = \"""val = { "object001" : 1, "object002" : { "value": 2 }, "object003" : ["A","B","C","D","E"], "object004": frame.current() } \"""
        results = js.evaluate( eval_script )
        print( "object001: %s"%results["object001"] )
        print( "object002: %s"%results["object002"]["value"] )
        print( "object003: "   )
        for x,n in enumerate(results["object003"]):
        print( "  %s: %s"%(x,n) )
        print( "object004: %s"%results["object004"] )
        ```

        Returns
            The object returned when evaluating the javascript string – this value can be null.
        """
        return
    
    def eval(self, javascript:str):
        """
        Alias to evaluate() method.

        Returns
            The object returned when evaluating the javascript string – this value can be null.
        """
        return
    
    def call_function(self, javascript:str, functionName:str, arguments, selfValue):
        """
        Evaluate and call a javascript function and return the results.

        Evaluates and calls a function in Javascript and returns the resulting object. May take arguments as a single element or as an array.

        Parameters
            javascript	- A string providing javascript with the available function to be called.
            functionName	- The function to call within the provided javascript.
            arguments	- A list of arguments with which the javascript function will be called.
            selfValue	- Optional, a script value that will be bound to the this context of the function.
        
        Call a Test Function with Arguments and Context
        ```python
        from ToonBoom import harmony
        sess = harmony.session()
        js = sess.javascript
        my_javascript = \"""
        function test( arg1, arg2, arg3 ){
            MessageLog.trace( arg1 + " : " + arg2 + " : " + arg3 );
            MessageLog.trace( this.context );
            return true;
        }
        \"""
        results = js.call_function( my_javascript, "test", ["Value1", "Value2", "Value3"], { "context" : "Hello World" } )
        ```
        
        Returns
            The object returned when evaluating the javascript string – this value can be null.
        """
        return
    
    def load_file(self, path:str, delayedInitialization:bool=False):
        """
        Loads a javascript object from a file at the given path.

        Evaluates and loads the javascript object as an accessible object in Python. This object and the functions and objects within it will remain persistent as long as the Python object is maintained.

        See load_file() for an example.

        Returns
            The OMC::JavascriptObject representing the loaded file.
        """
        return JavascriptObject()
    
    def load_string(self, script:str, delayedInitialization:bool=False):
        """
        Loads a javascript object from an evaluated string.

        Evaluates and loads the javascript object as an accessible object in Python. This object and the functions and objects within it will remain persistent as long as the Python object is maintained.

        The Javasscript is only evaluated once – and the internal objects will retain any changes made to them.
        
        A Demo of the Javascript Persistence
        ```python
        from ToonBoom import harmony
        sess = harmony.session()
        js = sess.javascript
        js_string = \"""
        globalObject = 0;
        function increment()
        {
            globalObject++;
            return globalObject;
        }
        \"""
        js_obj = js.load_string( js_string )
        print( js_obj["increment"].call() ) #1
        print( js_obj["increment"].call() ) #2
        print( js_obj["increment"].call() ) #3
        print( js_obj["increment"].call() ) #4
        #Forcefully re-evaluate the Javascript.
        js_obj.reload()
        #Note that the calls restart from 1 again.
        print( js_obj["increment"].call() ) #1
        print( js_obj["increment"].call() ) #2
        print( js_obj["increment"].call() ) #3
        print( js_obj["increment"].call() ) #4
        ```

        Returns
            The OMC::JavascriptObject representing the loaded string.
        """
        return JavascriptObject()
    
    def available_scripts(self) -> List[str]:
        """
        Returns a list of all javascripts available to the application in the script paths.

        List Available Scripts
        ```python
        from ToonBoom import harmony
        sess = harmony.session()
        js = sess.javascript
        list_scripts = js.available_scripts()
        for script_filename in list_scripts:
        print( script_filename )
        ```

        Returns
            List of available scripts names.
        """
        return [""]
    
    def eval_available_script(self, availableScriptName:str, functionName:str, arguments, selfValue):
        """
        Evaluates a function with its arguments inside a given available script.

        Call an Available Script
        ```python
        from ToonBoom import harmony
        sess = harmony.session()
        js = sess.javascript
        #Call the TB_orderNetworkDown function in the packaged  TB_orderNetworkDown.js script.
        js.eval_available_script( "TB_orderNetworkDown.js", "TB_orderNetworkDown", []
        ```

        Returns
            The object returned when evaluating the javascript string – this value can be null.
        """
        return JavascriptObject()
    
    def available_script_functions(self) -> List[str]:
        """
        Returns a list of all the functions available for calling inside a given available script.

        ```python
        from ToonBoom import harmony
        sess = harmony.session()
        js = sess.javascript
        list_scripts = js.available_scripts()
        for script_name in list_scripts:
        print( "%s: "%( script_name ) )
        try:
            script_funcs = js.available_script_functions( script_name )
            for func_name in script_funcs:
            print( "    %s "%( func_name ) )
        except:
            print( "    Failed to load script" )
        ```

        Returns
            List of available function names.
        """
        return [""]

class Node(BaseObject):
    """
    The node wrapping object. Represents a specific node in the scene.

    The node object represents a node within a scene. This object will maintain its link, even if the node is renamed. Some operations, such as copying and pasting, as well as moving nodes will result in this object no longer being valid.
    The node object provides access to the node's details, ports and attributes and is useful for automatic rig tasks in a scene.

    There exists multiple subclasses of the node object, these provide custom utilities for specialized node types:

    OMC::CameraNode : Represents a Camera node.
    OMC::DisplayNode : Represents a Display node.
    OMC::GroupNode : Represents a Group node.
    OMC::PegNode : Represents a Peg.
    OMC::ReadNode : Represents a Read/Drawing node.
    Each node specialization provides unique methods and properties for that node type, which simplifies automation with that specific node. This means that different node types will have different methods and properties available, but all nodes will inherit all standard methods from this base class.

    Identify All Nodes in a Scene:
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    nodes = scene.nodes                                          #Get the node list of the scene.
    #Iterating on the node list with a for-loop
    for node in nodes:                                            #For loop on the node list.
    print( "Node : %s"%(node.path) )
    ```

    Find Only Pegs in the Scene
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    nodes = scene.nodes                                          #Get the node list of the scene.
    #Iterating on the node list with a for-loop
    for node in nodes:                                            #For loop on the node list.
    if node.type.upper() == "PEG":                             #A upper-case comparison is useful for case-insensitivity. 
        print( "Peg : %s"%(node.path) )
    ```
    """
    def __init__(self):
        super().__init__()
    
    def parent_scene(self):
        """
        Getaaa the parent scene for the node.

        Every node belongs within a scene, this method provides the scene (OMC::Scene, or OMH::Scene) object to which this node belongs.

        Identify the Scene of the Current Node
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        nodes = scene.nodes                                          #Get the node list of the scene.
        try:
        first_node = nodes[0]                                      #Just using the first node as an example.
        except:
        first_node = False
        node_scene = first_node.parent_scene()                       #In this case, redundant as we already have the scene owner above.4
        print( "Same Scene: %s"%( node_scene == scene ) )            #Expectation: "Same Scene: True"
        ```
        """
        return Scene()
    
    def parent_group(self):
        """
        Gets the parent group for the node.

        Retrieves the group-object in which this node belong (OMC::GroupNode). Every node belongs within a group – even the top-level nodes belong to a transparent group named 'Top'. The 'Top' group node behaves in the same manner as any other group, but is not visible within the node view (See OMC::Scene::top).

        Identify the Group of a Random Node in the Scene
        ```python
        import random
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        nodes = scene.nodes                                          #Get the node list of the scene.
        try:
        random_node = nodes[random.randint(0,len(nodes))]          #Get a random node, and find its parent group.
        except:
        random_node = False
        node_group = random_node.parent_group()                      #In this case, redundant as we already have the scene owner above.4
        print( "Parent Group: %s"%(node_group) )
        ```
        """
        return GroupNode()
    
    def move_to(self, groupPath:str, x:int=0, y:int=0):
        """
        Moves the node into a group.

        Similar to OMC::NodeList::move, moves this node from one group to another based on the provided group path – but the OMC::Node connection is maintained. Fails with an error if the move fails.
        
        Parameters
            groupPath	- The path to the group into which this node will be placed.
            x	- The x coordinate of the node in the node view.
            y	- The y coordinate of the node in the node view.
        
        Move a Group Node into the Top Scene Group
        ```python
        import random
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        nodes = scene.nodes                                          #Get the node list of the scene.
        original_node = nodes["Top/Group1/Node"]                     #Get a node by name.
        original_node.move_to( "Top" )                               #Move the node to the new path.
        print( "New Node Path: %s"%(original_node.path) )            #Print the new path for the node.
        ```
        """
        return

    @property
    def attributes(self):
        """
        Provides the list of attributes of the node.

        The attribute-list is a dynamic list object (OMC::AttributeList) that provides the manipulatable attribute objects for the node. These attribute objects are useful for changing node attribute values both statically and over time (if the attribute is animateable).

        Print All Attributes for All Nodes (This could take time in heavier scenes)
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        nodes = scene.nodes                                          #Get the node list of the scene.
        #Iterating on the node list with a for-loop
        for node in nodes:                                            #For loop on the node list.
        print( "Node: %s"%(node.path) )
        for attribute in node.attributes:                           #Get available attributes on the node.
            print( "  -- Attribute: %s"%(attribute) )                 #Print All available attributes on the node.
        ```
        """
        return AttributeList()
        
    @property
    def ports_in(self):
        """
        Provides the list of input ports belonging to the node.

        Provides a dynamic list object (OMC::PortList) of input ports on the node. The portlist object is also used for generating new in-ports (OMC::InPort) on the node when the node-type supports dynamic port creation.
        Ports are connected to one another for rigging-purposes – a node's in-ports must be connected to another node's out-ports.

        Find First Node – Identify Port Count
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        nodes = scene.nodes                                          #Get the node list of the scene.
        try:
        first_node = nodes[0]                                        #Just using the first node as an example.
        except:
        first_node = False
        if first_node:
        portsin_count = len( first_node.ports_in )
        print( "Node %s has %s input ports."%( first_node.path, portsin_count ) )
        else:
        print( "Unable to find a node." )
        ```
        """
        return PortList()
        
    @property
    def ports_out(self):
        """
        Provides the list of output ports belonging to the node.

        Provides a dynamic list object (OMC::PortList) of output ports on the node. The portlist object is also used for generating new out-ports (OMC::OutPort) on the node when the node-type supports dynamic port creation.
        Ports are connected to one another for rigging-purposes – a node's in-ports must be connected to another node's out-ports.

        Find First Node – Identify Port Count
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        nodes = scene.nodes                                          #Get the node list of the scene.
        try:
        first_node = nodes[0]                                        #Just using the first node as an example.
        except:
        first_node = False
        if first_node:
        portsout_count = len( first_node.ports_out )
        print( "Node %s has %s output ports."%( first_node.path, portsout_count ) )
        else:
        print( "Unable to find a node." )
        ```
        """
        return PortList()
        
    @property
    def name(self) -> str:
        """
        Get/set the name of the node.

        The name of the node is the unique node name within a group. Given a node with "Top/Group/NodeName", the last section "NodeName" is the unique node-name within the group. This can also be used to rename the node in-place – in the event that the provided name is not unique, a new unique name will be generated.

        Add a Prefix to All Selected Nodes
        ```python
        import random
        from PySide6 import QtWidgets
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        selection = scene.selection                                  #Get the selected nodes.
        sel_node_size = len(selection.nodes)                         #How many nodes are selected?
        if sel_node_size > 0:
        nodestr = "Node"
        if sel_node_size > 1:
            nodestr = "Nodes"
        prefix, accept = QtWidgets.QInputDialog.getText( None, "Prefix", "Prefix %s %s"%(sel_node_size, nodestr) )      # Using PySide's built-in utilities to pop-up a string request.
        if accept and len(prefix)>0:
            for node in selection.nodes:
            if not node.name.startswith( prefix ):
                replacement_name = "%s%s"%(prefix, node.name)
                print( "Renaming %s to %s"%(node.name, replacement_name) )
                node.name = replacement_name                         #Renaming the node by setting its name.
        ```
        """
        return ""
        
    @property
    def path(self) -> str:
        """
        Get the path of the node. The path of the node is the absolute location of a node within a scene, including its name. The node's path provides the absolute location and the name of the node and can be used to both move and rename the node as needed.

        Rename the Node with the Path

        ```python
        import random
        from PySide6 import QtWidgets
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        selection = scene.selection                                  #Get the selected nodes.
        sellist = selection.nodes.list()                             #Create a static list, impervious to further node changes.
        newgroup = scene.nodes.create( "GROUP", "NEW_GROUP" )
        sel_node_size = len(sellist)                                 #How many nodes are selected?
        if sel_node_size > 0:
        for selnode in sellist:                                    #For each node, move it into the new group, and name it based on its type.
            new_name = selnode.type.upper()
            new_path = [ newgroup.path, new_name ]
            selnode.path = "/".join(new_path)                        #Join the group's full path 'Top/NEW_GROUP' with the new name.
            print( "New Node Location : %s"%(selnode.path) )
        ```
        """
        return ""
        
    @property
    def type(self) -> str:
        """
        Get the type of the node.

        All nodes have an underlying keyword node-type. This type value defines the type of the node and its utility in the scene. This is useful when looking for a specific node type in a scene.

        Find all Nodes, Move them 10 Units Right
        ```python
        import random
        from PySide6 import QtWidgets
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        nodes = scene.nodes                                          #Get the scene's node list. All nodes within the scene.
        for node in nodes:
        if node.type.upper() == "PEG":                             #Its generally good practice to compare strings in a case insensitive manner.
            #We found a peg, hurrah! 
            #Only pegs have the apply_translation method.
            node.apply_translation( [1, scene.frame_count], harmony.Vector3d(10.0, 0.0, 0.0 ) )  #Applies the translation to a range of frames.
        ```
        """
        return ""
        
    @property
    def position(self):
        """
        The position of the node in the node view.

        Provides a modifiable OMC::Node_Coordinates object. This can be used to modify the position of a node within the node view. See OMC::Node_Coordinates for more information.
        """
        return Node_Coordinates()
        
    @property
    def enabled(self) -> bool:
        """
        Get/set whether the node is enabled.

        Nodes that are disabled (enabled = False) have specific behaviour based on the type of node that is disabled. Generally, a disabled node is passed-through and ignored for transformations and when rendering the image. Disabling a node is useful when turning off portions of a rig, or comparing the output of a node.

        Disable All 'FX'
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        nodes = scene.nodes                                          #Get the scene's node list. All nodes within the scene.
        for node in nodes:
        try:                                                                            #There may not be a port at that index, instead, just request it and catch the error.
            if not node.ports_in.dynamic:                                                 #A basic assumption that a effect module cannot be dynamic. 
            if node.ports_in[0].type == "IMAGE" and node.ports_out[0].type == "IMAGE":  #An effect is a node with an image input and output. 
                print( "Disabling Node: %s"%(node.path) ) 
                node.enabled = False        
        except:
            pass
        ```
        """
        return True
        
    @property
    def cached(self) -> bool:
        """
        Get/set whether the node is cached.

        A boolean property that defines whether or not the node is cached as part of the rig cache. Nodes with caching enabled will use a cached bitmap when rendering to OpenGL.
        """
        return True
        
    @property
    def locked(self) -> bool:
        """
        Get/set whether the node is locked.

        A boolean property that defines whether the node is locked. Locked nodes will restrict certain kinds of interactions.
        """
        return True
        
    @property
    def colour(self):
        """
        Get/set the colour of the node.

        Sets the node's colour in the scene. The node colour is used in the node view as a coloured swatch and in the timeline as a tint on the timeline layer. The property is a colour object specific to the given node – and it accepts colours defined by OMC::Colour.

        Tint All Selected Nodes Red
        ```python
        from PySide6 import QtWidgets
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        proj.history.begin( "Tinting Nodes" )
        sess.notify_enabled = False
        node_sel = scene.selection.nodes
        colour = QtWidgets.QColorDialog.getColor()
        if colour.isValid():
        for node in node_sel:
            node.colour = harmony.Colour( colour.red(), colour.green(), colour.blue(), colour.alpha() )
        sess.notify_enabled = True
        proj.history.end()
        ```
        """
        return Colour()
        
    @property
    def cacheable(self) -> bool:
        """
        Get whether the node can be cached.

        Identifies if the node is cacheable, and can be cached with the OMC::Node::cached node property.
        """
        return True
        
    @property
    def version_max(self) -> int:
        """
        Get the max version of the node available.

        Certain nodes are versioned and these versions can change between versions releases and builds of the application. The version_max property provides the max version number that the node supports. The version of the node can be changed with the OMC::Node::version property.
        """
        return 1
        
    @property
    def version(self) -> int:
        """
        Get and set the version of the node.

        Certain nodes are versioned and these versions can change between versions releases and builds of the application. The version property identifies the current version of the node, which can be up to a maximum of the value provided by OMC::Node::version_max.
        """
        return 1
        
    @property
    def matte_port(self):
        """
        Returns the matte port, if one exists.

        Some node-types provide a matte-port (sometimes hidden) that provides specialized functionality for providing a matte while rendering. This property provides the matte-port as a OMC::InPort if one is available.

        Attach a mask to a drawing
        ```python
        from PySide6 import QtWidgets
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        proj.history.begin( "Attaching a Mask" )
        drawing = scene.nodes["Top/Drawing"]
        mask    = scene.nodes["Top/Mask"]
        matte_port = drawing.matte_port                              #Get the drawing's matte port
        if matte_port:
        matte_port.link( mask.ports_out[0] )                       #Link the matte port to the out-port (0th) on the mask node.
        # OR 
        matte_port.source = mask.ports_out[0]                      #This is equivalent ot the link command above, but the source is set as a property instead.   
        proj.history.end()
        ```
        """
        return Port()
        
    @property
    def thumbnail_timeline(self) -> bool:
        """
        Get and set whether the node shows a thumbnail in the timeline.

        Defines whether the thumbnail in the timeline view is enabled. When enabled, the node in the timeline will be expanded and a thumbnail will be visible. Generally, only image-type nodes (nodes with an image output port) support thumbnails in the timeline.

        Identify the Image Nodes and Enable Thumbnails
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        proj.history.begin( "Enabling Timeline Thumbnails" )
        nodes = scene.nodes
        for node in nodes:
        try:                                                       #Not all nodes provide a 0th port, instead of looking for one, just do the work and catch the error.
            port = node.ports_out[0]
            if port.type == "IMAGE":
            print( "Enabling Timeline Thumbnail : %s"%(node.path) )
            node.thumbnail_timeline = True
        except:
            pass
        proj.history.end()
        ```
        """
        return True
        
    @property
    def data(self):
        """
        The data handler that manages node data for views and tools.

        The OMC::Node::data property will provide a map of custom data handlers that are dynamic properties defined by the application in specific contexts. These contexts include data for specific views (timeline, xsheet, node-view) and data for specific tools. This will be implemented and expanded in future versions of the DOM.
        """
        return NodeDataHandler()
        
    @property
    def metadata(self) -> str:
        """
        The metadata handler object to provide metadata information.

        Metadata can be used to store generic information in the scene, and in nodes. This data is created and accessed through the object (OMC::MetaDataHandler) provided by this property.

        Print all Metadata in the node.
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Drawing"]                            #The node that is being checked for metadata.
        if len(node.metadata) == 0:
        print( "Node has no Metadata" )
        for metadata in node.metadata:
        print( "Key : %s"%(metadata.key) )
        print( "  Value : %s"%(metadata.value) )
        print( "  Type : %s"%(metadata.type) )
        ```

        Create Some Metadata
        ```python
        import json
        import time
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Drawing"]                            #The node that is being checked for metadata.
        metadata = node.metadata                                     #The metadata handler.
        production_data = {
                            "artist"   : "John Doe",
                            "scene_id" : "TB_001_0010",
                            "date"     : int(time.time())
                        }
        metadata["production_data"] = json.dumps( production_data )
        print( "Set Production Data" )
        json_data = metadata["production_data"].value
        retrieved_data = json.loads( json_data )
        for x in retrieved_data:
        print( "%s : %s"%(x, retrieved_data[x]) )
        #The metadata will be saved and available within the scene in subsequent instances of Harmony. This is useful for saving
        #generic data related to scenes or nodes.
        ```
        """
        return MetaDataHandler()
        
    @property
    def valid(self) -> bool:
        """
        Whether the bool is currently valid and the node still exists in the scene.

        The Document Object Model maintains links between the object in the DOM and the actual object in Harmony. Certain methods and actions within the GUI will devalidate the DOM objects, and in these cases the object is considered no longer valid. This can happen if the object is kept in memory in the DOM and other actions are performed in the GUI.
        The valid property defines whether or not the object is still valid. If actions are performed on an object that is no longer valid, an error will be thrown and needs to be caught and dealt with appropriately. It is particularly important to catch errors and check for validity on nodes in longer-running/persistent scripts. Only a few methods will devalidate a node within the same script.

        Checking for Valid Nodes
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        first_node   = scene.nodes.create( "PEG", "PEG001" )
        target_group = scene.nodes.create( "GROUP", "GROUP001") 
        #These nodes are both valid.
        print( "First Node: %s"%(first_node.valid) )                #Expectation: "First Node: True"
        print( "Group Node: %s"%(target_group.valid) )              #Expectation: "Group Node: True"
        # Moving a node to a group will result in the devalidation of the object -- since the move operation destroys the original node
        # and recreates it in the target location.
        resulting_node = target_group.nodes.move( first_node )
        #The original node that was moved is no longer valid.
        print( "First Node: %s"%(first_node.valid) )                #Expectation: "First Node: False"
        try:
        print( "Bad Node Path: %s"%(first_node.path) )
        except:
        print( "This was expected -- the original first_node is no longer valid due to move." )
        #But the 'move' method was nice enough to provide the resulting moved node.
        print( "Resulting Node: %s %s"%(resulting_node.valid, resulting_node.path) ) #Expectation: "Resulting Node: True Top/GROUP001/PEG001"
        ```
        """
        return True
        
    @property
    def subselections(self):
        """
        A list of subselectable objects that belong to the node.

        Provides a list of subselection objects, with IDs. These are used when selecting controllers on a given node and are best used in conjunction with the selection interface.
        """
        return NodeSubselectionList()

class Column(BaseObject):
    """
    Represents and provides the methods for a column in a scene.

    Columns are provided and created from the column list of the scene (OMC::Scene::columns). These columns are attached to attributes and are used to provide the attributes with animated values.
    Different types of attributes require different types of columns; these columns have their own subclasses in order to provide type-specific functionality:
        OMC::BezierColumn : A column providing an interpolated value from a bezier curve defined by control points.
        OMC::DrawingTimingColumn : A column providing a drawing based on a drawing path, prefix and frame value.
        OMC::EaseColumn : A column providing a value based on interpolated easing points.
        OMC::ElementColumn : A column providing a drawing based on an attached Element, its drawings and a timing value.
        OMC::ExpressionColumn : A column providing a value based on a scripted expression.
        OMC::Path3DColumn : A column providing a 3D Point value based on a path, keypoints and a velocity.
        OMC::QuaternionColumn : A column providing a quaternion rotation value.
        OMC::VeloBasedColumn : A column providing a value based on a curve path and a velocity.

    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    proj.history.begin( "Generating Test Column" )
    columns = scene.columns                                      #The overall node list of the scene.
    #Create the new Bezier Column
    new_column = columns.create( "BEZIER", "NEW_BEZIER_COLUMN" )
    value_incremental = 0
    #Add a keyframe value every 10 frames.
    for frame in range(1,60)[::10]:
    print( "Setting Key Value at %s : %s"%(frame, value_incremental) )
    new_column[frame] = value_incremental
    value_incremental = value_incremental + 1
    proj.history.end()
    ```
    """
    def __init__(self):
        super().__init__()
    
    def get_entry(self, atFrame:float, subColumnIndex:int=-1):
        """
        Returns the value of a cell in a column.

        Parameters
            atFrame	: The frame number at which to retrieve the value from.
            subColumnIndex	: The index of the sub-column. Only 3D Path columns support sub-column. They have sub-columns for the X, Y, Z and velocity values on the 3D Path. Each sub-column has an index:
            X = 1
            Y = 2
            Z = 3
            Velocity = 4
        
        Returns
            Returns the value of a cell in a column.
        """
        return
    
    def set_entry(self, atFrame:float, value, subColumnIndex:int=-1):
        """
        Sets the value of a cell in a column.

        Parameters
            atFrame	The frame number at which to set the value to.
            value	: the new value
            subColumnIndex	: The index of the sub-column. Only 3D Path columns support sub-column. They have sub-columns for the X, Y, Z and velocity values on the 3D Path. Each sub-column has an index:
            X = 1
            Y = 2
            Z = 3
            Velocity = 4
        """
        return
    
    def scale(self, scale_factor:int):
        """Scales the values in a column by a scaling factor."""
        return
    
    @property
    def name(self) -> str:
        """Get/set the name of the column. This is the internal name of the column which is used as a unique identifier."""
        return ""
        
    @property
    def display_name(self) -> str:
        """Get/Set the displayable name of the column (like it would appear in the xSheet view)."""
        return ""
        
    @property
    def type(self) -> str:
        """Get the type of the node."""
        return ""
        
    @property
    def anonymous(self) -> str:
        """Get/set the anonymous state of the column."""
        return ""
        
    @property
    def linked_nodes(self) -> List[Node]:
        """Identifies nodes that are linked to the column."""
        return [Node()]
        
    @property
    def linked_attributes(self):
        """Identifies attributes that are linked to the column."""
        return [Attribute()]
    
class About(BaseObject):
    """
    Get the active about details from the instance of the application.
    Provided from the Application (OMH::Harmony::about)
    The About class provides general information about the current application session. This includes environment information, and general application information
    
    Examples:
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        about = sess.about                                           #Get about object.
        print( about.path_application )                              #Expectation: Prints the path to the Harmony application's path.
        ```
    """
    def __init__(self):
        super().__init__()
    
    @property
    def flavor_string(self) -> str:
        """Returns a string that represents the flavor of the application. e.g. Harmony."""
        return ""
    
    @property
    def flavor_string_translated(self) -> str:
        """Returns the version info string."""
        return ""

    @property
    def version_major(self) -> int:
        """Returns the major version number."""
        return 1

    @property
    def version_minor(self) -> int:
        """Returns the minor version number."""
        return 1
    
    @property
    def version_patch(self) -> int:
        """Returns the patch version number."""
        return 1
    
    @property
    def build_number(self) -> int:
        """Returns the build number."""
        return 1
    
    @property
    def product_name(self) -> str:
        """String that is the name of application."""
        return ""
    
    @property
    def version_full(self) -> bool:
        """True whenever this application is a Commercial / Full variant."""
        return True
    
    @property
    def version_educational(self) -> bool:
        """True whenever this application is an Educational variant."""
        return True
    
    @property
    def path_application(self) -> str:
        """String that is the path of the application."""
        return ""
    
    @property
    def path_binary(self) -> str:
        """String that is the folder where the binaries can be found."""
        return ""
    
    @property
    def user_name(self) -> str:
        """The user name."""
        return ""
    
    @property
    def harmony(self) -> bool:
        """True when connected to a database or when compiled with Harmony Premium."""
        return True

    @property
    def harmony_premium(self) -> bool:
        """True whenever the application running is a Preimium variant."""
        return True
    
    @property
    def harmony_essentials(self) -> bool:
        """True whenever the application running is an Essentials variant."""
        return True
    
    @property
    def harmony_advanced(self) -> bool:
        """True whenever the application running is an Advanced variant."""
        return True
    
    @property
    def storyboard(self) -> bool:
        """True whenever the application running is Stage."""
        return True
    
    @property
    def arch_windows(self) -> bool:
        """True when running on Windows."""
        return True
    
    @property
    def arch_linux(self) -> bool:
        """True when running on Linux."""
        return True
    
    @property
    def arch_mac(self) -> bool:
        """True when running on mac."""
        return True
    
    @property
    def arch_mac_intel(self) -> bool:
        """True when running on an Apple OS X operating system on Mac Intel."""
        return True
    
    @property
    def arch_mac_ppc(self) -> bool:
        """True when running on an Apple OS X operating system on Mac PowerPC."""
        return True
    
    @property
    def arch_mac_m1(self) -> bool:
        """True when running on an Apple OS X operating system on Mac M1."""
        return True
    
    @property
    def interactive(self) -> bool:
        """True whenever this application is running in an interactive mode with a GUI."""
        return True
    
    @property
    def app_stage(self) -> bool:
        """True whenever the application running is Stage."""
        return True
    
    @property
    def app_scan(self) -> bool:
        """True whenever the application running is Scan."""
        return True
    
    @property
    def app_main(self) -> bool:
        """True when the application is Harmony or Storyboard, and not a peripheral application."""
        return True
    
    @property
    def mode_paint(self) -> bool:
        """True when the application is in Paint mode."""
        return True
    
    @property
    def mode_xsheet(self) -> bool:
        """True when the application is in Xsheet mode."""
        return True
    
    @property
    def mode_database(self) -> bool:
        """True when the application is in Database mode."""
        return True
    
    @property
    def version_demo(self) -> bool:
        """True whenever this application is a Demo variant."""
        return True
    
    @property
    def mode_python(self) -> bool:
        """True whenever the application is running from the external Python module interface."""
        return True
    
    @property
    def mode_batch(self) -> bool:
        """True whenever the application is running from the external batch-mode from the commandline."""
        return True
    
class Actions(BaseObject):
    """
    The Action global object.

    Provided from the Application (OMH::Harmony::actions)

    The application's action interface is used to perform underlying actions within the GUI in the application. Generally, actions are only available internally within the GUI. This interface can also be used to list available actions that can be performed.
    In the event that a scripted solution is not available through the DOM, an action may be available. It is worth noting that actions can require user input and subsequent application event callbacks, some of which are not supported in a scripted environment.
    
    Examples:
    Print Available Actions
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        actions = sess.actions                                       #Get actions handler.
        for responder in actions.responders:
        print( responder )
        action_list = actions.actions(responder)
        for action in action_list:
            print( "   %s"%(action) )                               #Expectation - All responders will be listed with their available actions.
        ```
    
    Run an Action from a Responder
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        actions = sess.actions                                       #Get actions handler.
        result = actions.perform( "onActionCreatePeg()", "Node View" )
        if result == "ACTION_NOTHING_TO_DO":
        print( "Run ActionCreatePeg from Node View responder." )
        ```
    """
    def __init__(self):
        super().__init__()
    
    def actions(self, responder:str) -> list:
        """
        Retrieve the list of actions for a given responder.

        Parameters
            responder	responder identity to investigate.
        """
        return []
    
    def perform(self, slot:str, responder:str, parameters:str):
        """
        1/3 - slot

        Perform the requested action (slot - menu item, toolbar item,...)
        Perform the requested action for the main application responder. If the main responder doesn't own the requested action, try to use the current view with focus as the responder.

        ------------------------------------------------------------------------
        2/3 - slot + responder

        Perform the requested action (slot - menu item, toolbar item,...)
        Perform the requested action for a specific responder.

        ```python
        from ToonBoom import harmony                                                #Import the Harmony Module
        sess = harmony.session()                                                    #Get access to the Harmony session, this class.
        actions = sess.actions                                                      #Get actions handler.
        actions.perform("onActionToggleApplyToolToAllLayers()", "drawingView");
        ```
        
        Parameters
            slot	The action function name (ex: onMyAction()).
            responder	The responder to the function name (ex: drawingView).

        ------------------------------------------------------------------------
        3/3 - slot + responder + parameters

        Execute an action using the action manager on the given responder with parameters.

        Parameters
            slot	action to execute. See Actions.getActionList() for action list.
            responder	command target. See ActionsgetResponderList() for responder list.
            parameters	action parameter(s). Use an array [] to provide multiple action parameters.
        
        Example usage:
        ```python
        from ToonBoom import harmony                                                #Import the Harmony Module
        sess = harmony.session()                                                    #Get access to the Harmony session, this class.
        actions = sess.actions                                                      #Get actions handler.
        actions.perform( "onActionShowDeformer(QString)","miniPegModuleResponder", "Top/Deformation-Drawing" );
        ```
        """
        return
    
    def performForEach(self, slot:str, responder:str):
        """
        Execute an action using the action manager on all responder instances.

        Parameters
            slot	action to execute. See Actions.getActionList() for action list.
            responder	command target. See Actions.getResponderList() for responder list.
        """
        return
    
    def validate(self, slot:str):
        """
        1/2 - slot

        Validate the requested action (slot - menu item, toolbar item,...)

        Validate the requested action for the main application responder. If the main responder doesn't own the requested action, try to use the current view with focus as the responder.

        ```python
        from ToonBoom import harmony                                                #Import the Harmony Module
        sess = harmony.session()                                                    #Get access to the Harmony session, this class.
        actions = sess.actions                                                      #Get actions handler.
        validate_data = actions.validate( "onActionAbout()" );
        ```

        Parameters
            slot	The action function name(ex : onMyAction()).

        Returns
            A script object that has the valid_responder, valid_slot, enabled and checked boolean properties.
        
        ------------------------------------------------------------------------
        2/2 - slot + responder

        Validate the requested action (slot - menu item, toolbar item,...)

        Validate the requested action for a specific responder.

        ```python
        from ToonBoom import harmony                                                #Import the Harmony Module
        sess = harmony.session()                                                    #Get access to the Harmony session, this class.
        actions = sess.actions                                                      #Get actions handler.
        # Toggle on the Apply Tool to Line and Colour Art option only if it's off.
        validateData = actions.validate("onActionToggleApplyToolToAllLayers()", "drawingView");
        if( not validateData.checked )
        actions.perform("onActionToggleApplyToolToAllLayers()", "drawingView");
        ```

        ```python
        from ToonBoom import harmony                                                #Import the Harmony Module
        sess = harmony.session()                                                    #Get access to the Harmony session, this class.
        actions = sess.actions                                                      #Get actions handler.
        # Toggle on the Apply Tool to Line and Colour Art option only if it's off.
        validateData = actions.validate("onActionCreateNewDeformationChain()", "miniPegModuleResponder");
        if( not (validateData.isValid and validateData.enabled) )
        print("The desired action is unavailable, please select an element node");
        ```

        Parameters
            slot	The action function name (ex: onMyAction()).
            responder	The responder to the function name (ex: drawingView).

        Returns
            A script object that has the isValid, enabled and checked boolean properties.
        """
        return
    
    @property
    def responders(self) -> List[str]:
        """
        Retrieve the list of responder names.
        """
        return

class Rect2D(BaseObject):
    def __init__(self, width:float=0.0, height:float=0.0):
        super().__init__()
        self.width = width
        self.height = height

class Rect2DI(BaseObject):
    def __init__(self, width:float=0.0, height:float=0.0):
        super().__init__()
        self.width = width
        self.height = height

class AllocatedRect2D(Rect2D):
    """Provides a rectangle with position, width and height, provided as a double value."""
    def __init__(self, width:float, height:float, x:float, y:float):
        super().__init__()
    
    @property
    def x(self) -> float:
        """Origin of the object in the x axis."""
        return
    
    @property
    def y(self) -> float:
        """Origin of the object in the y axis."""
        return
    
    @property
    def width(self) -> float:
        """width of the object"""
        return
    
    @property
    def height(self) -> float:
        """height of the object"""
        return


class AllocatedRect2DI(BaseObject):
    """Provides a rectangle with position, width and height, provided as an integer value."""
    def __init__(self, width:float, height:float, x:float, y:float):
        super().__init__()
    
    @property
    def x(self) -> float:
        """Origin of the object in the x axis."""
        return
    
    @property
    def y(self) -> float:
        """Origin of the object in the y axis."""
        return
    
    @property
    def width(self) -> float:
        """width of the object"""
        return
    
    @property
    def height(self) -> float:
        """height of the object"""
        return

class Application(BaseObject):
    """
    The object representing the overall running application at the base level.

    The top level object, representing the currently running application, Harmony, Storyboard or Control Center. Generally provided from the main Python module's session.
    """
    def __init__(self):
        super().__init__()
    
    def process_one_event(self):
        """
        Processes the next event in the application's event queue.

        In the event that the script requires updates in the GUI, process_one_event() will ublock the application from the current script and run the next event in the application queue.
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        session = harmony.session()
        actions = session.actions
        actions.perform( "actionThatRequiresGUI" )
        session.process_one_event()
        ```
        """
        return

    def log(self, log:str, level:str):
        """
        [1/2] - log

        Write to the application's Message Log; defaults to a trace_level log.

        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        session = harmony.session()
        session.log( "Hello World!" )                                #Expectation: Hello World appears in the MessageLog's view.
        ```

        ------------------------------------------------------------------------
        [2/2] - log + level

        Write to the application's Message Log with different levels as an option.

        The Message Log supports three levels of output, which can be specified in this function.

        Available log levels include:

        trace : The standard trace output in the MessageLog view.
        debug : The debug output in the MessageLog view, only available when the Application's debug mode is enabled.
        error : The error output in the MessageLog view, as well as a critical error popup window.
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        session = harmony.session()
        session.log( "Hello Debug World!", "debug" )                 #Expectation: Hello World appears in the MessageLog's view.
        ```
        """
        return

    def trace(self, log:str):
        """Write to the application's Message Log as trace output."""
        return
    
    def debug(self, log:str):
        """Write to the application's Message Log as debug output."""
        return
    
    def error(self, log:str):
        """Write to the application's Message Log as error output."""
        return

    def thread_lock(self):
        """
        Locks the application to allow for a thread to process commands.

        When running in threads – accessing Harmony objects without a thread lock will result in an error. Instead, get the application's lock in the external thread, and release it when complete to regain activity in the main application thread afterwards.
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        from time import sleep
        from threading import Thread
        session = harmony.session()
        def thread_task():
        session.thread_lock()
        print("RUNNING TEST")
        proj = session.project
        scene = proj.scene
        nodes = scene.nodes
        for n in nodes:
            print(n.name)
        session.thread_unlock()
        thread = Thread(target=thread_task)
        thread.start()
        # The thread will be queued to run on the main thread when it becomes available.
        # concurrent work cannot be done, as the main thread needs to be available at some point.
        # processOneEvent() may be needed to force the queued event to occur.
        ```
        """
        return
    
    def thread_unlock(self):
        """
        Unlocks the application after a thread has processed commands.

        See thread_lock() for more information.
        """
        return

    def run_function(self, func:PythonFunction):
        """
        Runs the provided function while locking and unlocking the application as needed.

        Similar to lock() and unlock(), this will run the provided function and lock and unlock the application as necessary.
            ```python
            #In an external Python thread ---
            from ToonBoom import harmony                                 #Import the Harmony Module
            from time import sleep
            from threading import Thread
            session = harmony.session()
            def mainthread_action():
            print("RUNNING TEST")
            proj = session.project
            scene = proj.scene
            nodes = scene.nodes
            for n in nodes:
                print(n.name)
            def thread_task():
            session.run_function( mainthread_action )
            thread = Thread(target=thread_task)
            thread.start()
            print( "Concurrent Work Being Done" )
            ```
        """
        return
    
    def run_on_main(self, func:PythonFunction, blocking:bool):
        """
        Runs the provided method on the main thread.

        Only available in the internal Python Console

        Using run_on_main will send the function-call to the main thread and it is run there safely. The external thread locks until the main thread has finished.

        Note– this requires that the main thread be available to run the function at some point; the call will time out if is does not become available in a timely manner.

        ```python
        #In an external Python thread ---
        from ToonBoom import harmony                                 #Import the Harmony Module
        from time import sleep
        from threading import Thread
        session = harmony.session()
        def mainthread_action():
        print("RUNNING TEST")
        proj = session.project
        scene = proj.scene
        nodes = scene.nodes
        for n in nodes:
            print(n.name)
        def thread_task():
        session.run_function( mainthread_action )
        thread = Thread(target=thread_task)
        thread.start()
        #The thread will queue the function onto the main thread, the function is called when the main thread can appropriately run it.
        ```
        """
        return

    @property
    def project(self) -> Project:
        """Get the active project from the instance of the application."""
        return Project()

    @property
    def about(self) -> About:
        """Get the active about details from the instance of the application."""
        return About()
    
    @property
    def preferences(self) -> Preferences:
        """Get the active preferences from the instance of the application."""
        return Preferences()
    
    @property
    def actions(self) -> Actions:
        """Get the application's actions."""
        return Actions()
    
    @property
    def views(self):
        """Get the application's available views."""
        raise RuntimeError("Views not yet supported in Harmony")
    
    @property
    def tools(self):
        """Get the application's available tools."""
        raise RuntimeError("Tools not yet supported in Harmony")
    
    @property
    def interfaces(self):
        """Get the DOM interface manager."""
        raise RuntimeError("Interfaces not yet supported in Harmony")
    
    @property
    def javascript(self) -> Javascript:
        """Get the Javascript interface, used for interacting with Javascript scripts."""
        return

class Attribute(BaseObject):
    """
    The attribute wrapper.

    This object wraps a single attribute owned by a node or an attribute. Attributes provide data, sometimes animateable, to the node and can be modified to control the behaviour of the node.
    There exists multiple subclasses of the node object, these provide custom utilities for specialized node types:

    OMC::BoolAttribute : An attribute providing a bool, true or false.
    OMC::ColourAttribute : An attribute providing a colour.
    OMC::DoubleAttribute : An attribute providing a double number.
    OMC::DrawingAttribute : An attribute providing a drawing reference.
    OMC::ElementAttribute : An attribute providing an element reference.
    OMC::EnumAttribute : An attribute providing a specific option value.
    OMC::IntAttribute : An attribute providing an integer number.
    OMC::Position2DAttribute : An attribute providing a 2D position [xy].
    OMC::Position3DAttribute : An attribute providing a 3D position [xyz]
    OMC::TextAttribute : An attribute providing a text value.
    OMC::TimingAttribute : An attribute providing a timing column for drawings.
    """
    def __init__(self):
        super().__init__()

    def node(self) -> Node:
        """
        The node that owns this attributes.

        Retrieves the Node that owns this attribute.

        Returns
            Returns the owning OMC::Node object related to this attribute.
        """
        return Node()

    def unlink(self) -> bool:
        """
        Unlinks a column from the attribute.

        Returns
            Returns whether the column has been successfully removed from the attribute.
        
        Unlinks any column from the attribute.
        Also see OMC::Column::column with property None.

        ```python
        node.attribute["attrbKeyword"].unlink()
        #Same as:
        node.attribute["attrbKeyword"].column = None
        ```
        """
        return True

    def link(self) -> bool:
        """
        Links a column to the attribute, making it animate over time.

        Returns
            Returns whether the column has been successfully linked to the attribute.
            Links a column to the attribute, making it animate over time.

        Returns
            Returns whether the column has been successfully linked to the attribute.
        
        Links a column to the attribute, if the column is compatible with the attribute type. Also see setting OMC::Column::column with a Column object property.
        """
        return True

    def set_text_value(self) -> bool:
        """
        Modify an attribute with a text value at a given frame. Change an attribute with a text value applied at a specific frame. This provides similar utility as the Javascript libraries available for the application.

        Parameters
            atFrame	- The frame at which to set the attribute.
            value	- The new value of the attribute.
            
        Returns
            Returns whether the attribute has been successfully changed.
        """
        return True

    def get_text_value(self) -> str:
        """
        Get a text value at a given frame. Retrieve the text value of an attribute at a specific frame. This provides similar utility as the Javascript libraries available for the application.

        Parameters
            atFrame	- The frame at which to set the attribute.

        Returns
            Returns the text value of the string at the given frame.
        """
        return ""
     
    @property
    def column(self) -> Column:
        """
        Get and set the column object attached to the the attribute, if it is supported.

        Attributes that are animateable will support columns that provide values per frame. Different attribute-types support different column types. The OMC::Attribute::column provides access to getting and setting the Column object associated with this attribute.
        Note
        Setting a column will override any other column associated with the attribute. Setting the column to none will unlink the column (similar to ONC::Attribute::unlink)

        Get the Column Associated with the Attribute:
            ```python
            from ToonBoom import harmony                                 #Import the Harmony Module
            sess = harmony.session()                                     #Get access to the Harmony session, this class.
            proj = sess.project                                          #Get the active session's currently loaded project.
            scene = proj.scene                                           #Get the top scene in the project.
            node_path = "Top/Node"
            node = scene.nodes[ node_path ]
            if node:
            for attrbs in node.attributes:
                if attrbs.column:
                print( "%s has column %s"%(attrbs.full_keyword, attrbs.column.name) )
            else:
            print( "Unable to find node: %s"%(node_path) )
            ```
        
        Set the Column on the Attribute
            ```python
            from ToonBoom import harmony                                 #Import the Harmony Module
            sess = harmony.session()                                     #Get access to the Harmony session, this class.
            proj = sess.project                                          #Get the active session's currently loaded project.
            scene = proj.scene                                           #Get the top scene in the project.
            node_path = "Top/Node"
            node = scene.nodes[ node_path ]
            type_map = {                                                 #Different attrb types support different column types, create a lookup map.
                        "PATH_3D"         : "3D_PATH",
                        "QUATERNION_PATH" : "QUATERNION_PATH",
                        "TIMING"          : "TIMING",
                        "DOUBLE"          : "BEZIER",
                        "DOUBLEVB"        : "BEZIER",
                        "INT"             : "BEZIER"
                        }
            if node:
            idx = 0
            
            #Create a recursive function to apply columns to even the subattributes.
            def create_new_columns( nodelist, type_map ):
                global idx
                for attrb in nodelist:
                if attrb.linkable:                                                                                #The attribute is linkable, so it will support a columm.
                    if attrb.type.upper() in type_map:                                                            #Ensure our lookup map supports the attrb type.
                        
                        while True:
                        try:                                                                                      #Iterate until a new column is available with the provided name.
                            newcol = scene.columns.create( type_map[attrb.type.upper()], "NEW_COLUMN_%03d"%(idx) )  #Create a new column for this attribute.
                            break
                        except:
                            idx = idx + 1
                
                        print( "Linking %s to %s"%(newcol.name, attrb.full_keyword) )
                        attrb.column = newcol                                                                       #Set the newly created column to the attribute.
                        
                        idx = idx + 1
                    else:
                        print( "Unsupported Attrb type : %s"%(attrb.type) )
                elif attrb.subattributes:
                    create_new_columns( attrb.subattributes, type_map )
            
            #Use the recursive function to set a new column on every attribute.
            create_new_columns( node.attributes, type_map )
            ```
        """
        return Column()
        
    @property
    def column_name(self) -> str:
        """
        Get and set the column name attached to the the attribute.

        A utility to allow references to the column by name, instead of by Column object (OMC::Column). This would be similar to the following:

        ```python
        node.attribute["attrbKeyword"].column_name = column_object.name
        #Same as:
        node.attribute["attrbKeyword"].column = column
        ```
        """
        return ""
        
    @property
    def keyword(self) -> str:
        """
        Get the keyword of the attribute.

        All columns are referenced by their keyword when relative to a given parent object. Otherwise, they are referenced by their full_keyword (OMC::Column::full_keyword) property – which contains the full path to that attribute on a given Node.

        Note
        The keyword is useful when relative to a given parent, but the full_keyword will provide the absolute path of the attribute. Notice in the example below, that only the relative keyword is printed.
        Get the Keyword of All Attributes on a Node

        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node_path = "Top/Node"
        node = scene.nodes[ node_path ]
        def attrb_keywords( attrblist, depth ):
        for attrb in attrblist:
            print( "%s %s"%( "  "*depth, attrb.keyword ) )           #Only printing the keyword of the attribute. Note, subattributes will only print their basename, and not their parent's in a path.
            
            if attrb.subattributes: 
            attrb_keywords( attrb.subattributes, depth+1 )         #If we hit something with subattributes, print those too!
        if node:
            attrb_keywords( node.attributes, 0 )
        
        else:
            print( "Unable to find node: %s"%(node_path) )
        ```
        """
        return ""
        
    @property
    def display_name(self) -> str:
        """
        Get the display name of the attribute.

        Provides the display name of the attribute. The display name is read only, and is the name of the attribute provided within the GUI to the user.
        """
        return ""
        
    @property
    def type_name(self) -> str:
        """
        Get the display name of the attribute.

        Provides the type-name of the attribute. Different attribute-types provide different information to the node and also require different column-types when linked (if linkable).

        Note
        Different subclasses of the OMC::Attribute object are provided for different attribute types. These different subclasses provode specific utilties for that attribute-type. See OMC::BoolAttribute, OMC::ColourAttribute, OMC::DoubleAttribute, OMC::DrawingAttribute, OMC::ElementAttribute, OMC::EnumAttribute, OMC::IntAttribute, OMC::Position2DAttribute, OMC::Position3DAttribute, OMC::TextAttribute and OMC::TimingAttribute.

        See OMC::Attribute::column for an example.
        """
        return ""
        
    @property
    def full_keyword(self) -> str:
        """
        Return the full keyword of the Attribute.

        All columns can be referenced by their full keyword as this provides the full path to the given attribute on a Node.

        Note
        The full_keyword is useful when referencing an attribute from a node, even if that attribute is a subattribute of another. Notice in the example below, that only the full keyword is printed, which provides the path to the attribute from the base of the node's attribute list (see OMC::AttributeList::operator[ QString& keyword ]).
        Get the Keyword of All Attributes on a Node

        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node_path = "Top/Node"
        node = scene.nodes[ node_path ]
        def attrb_keywords( attrblist, depth ):
        for attrb in attrblist:
            print( "%s %s"%( "  "*depth, attrb.full_keyword ) )      #Only printing the keyword of the attribute. Note, subattributes will only print their basename, and not their parent's in a path.
            if attrb.subattributes:
            attrb_keywords( attrb.subattributes, depth+1 )         #If we hit something with subattributes, print those too!
        if node:
        attrb_keywords( node.attributes, 0 )
        else:
        print( "Unable to find node: %s"%(node_path) )
        ```
        """
        return ""
        
    @property
    def dynamic(self) -> bool:
        """
        Identifies if the attribute is dynamic.

        Dynamic attributes are those that are created with scripted access to an attribute and are created dynamically and uniquely for that node. These dynamic attributes are not necessarily standard for the node-type, and can be added or removed from the node on-demand.
        See OMC::AttributeList::create_dynamic_attr for more information.

        Create a new Double Dynamic Attribute

        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node_path = "Top/Node"
        node = scene.nodes[ node_path ]
        if node:
        attrbs = node.attributes
        created_attribute = attrbs.create_dynamic_attr( "DOUBLE", "DYNAMIC_NAME", "DYNAMIC_DISPLAY", True )
        if created_attribute:
            if created_attribute.dynamic:                            #Expected to be true, since we just created it.
            print( "Created Dynamic Attribute: %s"%(created_attribute.full_keyword) )
            created_attribute.set_value(1, 10, False)
        else:
            print( "Failed to create attribute." )
        else:
        print( "Node does not exist: %s"%(node_path) )
        ```
        """
        return ""
        
    @property
    def linkable(self) -> bool:
        """
        Identifies if the attribute is linkable and can have a column linked to it.

        Only some attributes are animateable and accept a column. If a column is set on a non-linkable attribute, an error is thrown.
        See OMC::Attribute::column for an example.
        """
        return ""
        
    @property
    def subattributes(self):
        """
        Get the list of subattributes belonging to the attribute.

        Provides the subattribute list (OMC::AttributeList) for this attribute, if one is available. Only certain attribute-types are considered complex, and contain subattributes.

        Identify if an Attribute has Subattributes

        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node_path = "Top/Node"
        node = scene.nodes[ node_path ]
        if node:
        for attrbs in node.attributes:
            if attrbs.subattributes:
            print( "Attrb %s has %s subattributes."%(attrbs.full_keyword, len(attrbs.subattributes) ) )
            else:
            print( "Attrb %s has no subattributes."%(attrbs.full_keyword) )
        else:
        print( "Unable to find node: %s"%(node_path) )
        ```

        See OMC::Attribute::column for more examples.
        """
        return AttributeList()
    

class AttributeList(ListObj, IterableObj):
    """
    Represents a list of attributes for a node, or subattributes of an attribute.

    An AttributeList provides the attributes owned by the parent. In most cases, the AttributeList is provided by a Node via OMC::Node::attributes. Some attributes are complex and have subattributes, accessible from OMC::Attribute::subattributes.
    The AttributeList allows for list iteration in for loops, indexed access with the list operator[int_idx], and named access with the map operator["name"]

    Identify All Attributes Recursively on a Node

    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    node_path = "Top/Node"
    node = scene.nodes[ node_path ]
    if node:
    #Start with the base node's list, and recursively look through each attributelist thereafter.
    #A recursive function to look at all attributes in any attribute list, the node's attributes, or subattributes.
    def detail_all_attributes( attrblist, depth ):
        for attrb in attrblist:
        print( "%s %s -- %s"%( "  "*depth, attrb.full_keyword, attrb.type )  )
        if attrb.subattributes:                                                   #If this attribute has further subattributes, detail them too.
            detail_all_attributes( attrb.subattributes, depth+1 )
    #Start detailing the attributes. . .
    detail_all_attributes(node.attributes, 0) 
    
    else:
    print( "Unable to find the node : %s"%node_path )
    ```
    ------------------------------------------------------------------------
    Direct Access to an Attribute by Keyword

    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    peg_path = "Top/Peg"
    peg = scene.nodes[ peg_path ]
    if peg:
    #Knowing that a peg has a PIVOT attribute, access it directly with the map operator:
    pivot_attr = peg.attributes[ "PIVOT" ] 
    if pivot_attr:
        #FOUND IT!
        frame = 1
        pivot_attr.set_value( frame, harmony.Point3d(3.0, 1.0, 0.0), False )     #Set the pivot at the attribute level.    
        print( "Set the Peg's Pivot at frame : %s"%(frame) )
    else:
        print( "Failed to find PIVOT attribute." )
        
    #Also, sub attributes can be retrieved in two ways:
    pivot_attr_x1 = peg.attributes["PIVOT.X"]
    pivot_attr_x2 = peg.attributes["PIVOT"].subattributes["X"]
    
    print( "These are equivalent: %s and %s"%(pivot_attr_x1.full_keyword, pivot_attr_x2.full_keyword) )
    else:
    print( "Unable to find the node : %s"%peg_path )
    ```
    """
    def __init__(self):
        super().__init__()
    
    def __getitem__(self, idx:int, attribute_name:str) -> Attribute:
        """
        [1/2] - idx

        Provides the attribute at the given index.

        Allows for index access to an Attribute.

        Iterate over the Attribute List with Index

        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node_path = "Top/Node"
        node = scene.nodes[ node_path ]
        attribs = node.attributes
        attrib_size = len(attribs)
        for idx in range(attrib_size):                               #Instead of iterating over the object, iterate over the list with an index.
        attrb = attribs[idx] 
        print( "Attribute at Index %s: %s"%(idx, attrb.full_keyword) )
        ```
        ------------------------------------------------------------------------
        [2/2] - attribute_name

        Provides the attribute at the given index.

        Allows for index access to an Attribute.

        Direct Access to an Attribute by Keyword

        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        peg_path = "Top/Peg"
        peg = scene.nodes[ peg_path ]
        if peg:
        #Knowing that a peg has a PIVOT attribute, access it directly with the map operator:
        pivot_attr = peg.attributes[ "PIVOT" ] 
        if pivot_attr:
            #FOUND IT!
            frame = 1
            pivot_attr.set_value( frame, harmony.Point3d(3.0, 1.0, 0.0), False )     #Set the pivot at the attribute level.    
            print( "Set the Peg's Pivot at frame : %s"%(frame) )
        else:
            print( "Failed to find PIVOT attribute." )
            
        #Also, sub attributes can be retrieved in two ways:
        pivot_attr_x1 = peg.attributes["PIVOT.X"]
        pivot_attr_x2 = peg.attributes["PIVOT"].subattributes["X"]
        
        print( "These are equivalent: %s and %s"%(pivot_attr_x1.full_keyword, pivot_attr_x2.full_keyword) )
        else:
        print( "Unable to find the node : %s"%peg_path )
        ```
        """
        return Attribute()

    def contains(self,attr:str) -> bool:
        """
        Identifies if the list contains the attribute (or subattribute).

        Useful when identifying if an attribute is contained within an attribute list. This is also used with Python's built in in operator.

        Check for Attribute in List
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        peg_path = "Top/Peg"
        peg = scene.nodes[ peg_path ]
        if peg:
            #Check for an Attribute that exists:
            if "PIVOT" in peg.attributes:
            print( "PIVOT EXISTS" )
            else:
            print( "PIVOT DOESNT EXISTS -- ERROR" )
            
            #This is equivalent:
            
            if peg.attributes.contains("PIVOT"):
            print( "PIVOT EXISTS" )
            else:
            print( "PIVOT DOESNT EXISTS -- ERROR" )
            
            if "DOESNT_EXIST" in peg.attributes:
            print( "This really shouldn't exist. . ." )
            else:
            print( "This is expected.peg" )
        ```
        """
        return True

    def list(self):
        """
        Converts the dynamic list into a static list of attribute objects.

        By default, the AttributeList object is a dynamic list-type. This means that the object does not contain a persistent list, but behaves dynamically when a node is requested from it. Sometimes, a static list is preferred and this method will generate a static list of OMC::Attribute objects. Note, although the list is static, the objects within the list remain dynamic and refer to a node within the project.
        """
        return [Attribute()]
    
    def create_dynamic_attr(self, type:str, name:str, displayName:str, linkable:bool):
        """
        Creates a dynamic attribute on the node.

        Custom dynamic attributes can be added to nodes by the attribute list owned by the Node. These dynamic attributes behave as normal attributes, but can be added and removed as needed.

        Parameters
            type	- The type of the dynamic attribute.
            name	- The name of the attribute.
            displayName	- The display name of the attribute.
            linkable	- Whether the attribute can be linked to a column.

        Returns
            Returns the newly-created dynamic Attribute.

        Create a new Double Attribute

        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node_path = "Top/Node"
        node = scene.nodes[ node_path ]
        if node:
        attrbs = node.attributes
        created_attribute = attrbs.create_dynamic_attr( "DOUBLE", "DYNAMIC_NAME", "DYNAMIC_DISPLAY", True )
        if created_attribute:
            print( "Created Dynamic Attribute: %s"%(created_attribute.full_keyword) )
            created_attribute.set_value(1, 10, False)
        else:
            print( "Failed to create attribute." )
        else:
        print( "Node does not exist: %s"%(node_path) )
        ```
        """
        return
    
    def remove_dynamic_attr(self, attr:str):
        """
        Removes a dynamic attribute from the node.

        Removes the dynamic attribute provided as an argument, if it exists in this list. Throws an error if there is an issue otherwise.

        Parameters
            attr	- The name of the attribute.
        """
        return

class KeyframeableColumn(Column):
    def __init__(self):
        super().__init__()
        
    def keyframes_clear(self, startFrame:int=1, endFrame:int=-1):
        return
    
    def keyframe_exists(self, frame:int) -> bool:
        return
    
    def keyframe_create(self, frame:int):
        return
    
    def keyframe_remove(self, frame:int):
        return
    
    def keyframe_list(self) -> List[int]:
        return [1]

    @property
    def hold_start(self) -> int:
        return 1
    
    @property
    def hold_stop(self) -> int:
        return 1
    
    @property
    def hold_step(self) -> int:
        return 1
    
    @property
    def control_point_size(self) -> int:
        return 1
    
    @property
    def control_points(self):
        return ControlPointList()

class BezierColumn(KeyframeableColumn):
    """
    A column providing an interpolated value from a bezier curve defined by control points.


    Generate an Example Column
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    proj.history.begin( "Generating Test Column" )
    columns = scene.columns                                      #The overall node list of the scene.
    #Create the new Bezier Column
    new_column = columns.create( "BEZIER", "NEW_BEZIER_COLUMN" )
    value_incremental = 0
    #Add a keyframe value every 10 frames.
    for frame in range(1,60)[::10]:
    print( "Setting Key Value at %s : %s"%(frame, value_incremental) )
    new_column[frame] = value_incremental
    value_incremental = value_incremental + 1
    proj.history.end()
    ```
    """
    def __init__(self):
        super().__init__()
    
    def __getitem__(self, frame:int):
        """
        The column object is is iterable and can provide values at given frames with the list operator. The frame value can be get and set from this interface.


        Print Column Values
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        columns = scene.columns                                      #The overall node list of the scene.
        bez_col = columns["BEZIER_COLUMN_NAME"]
        for n in range( 1, scene.frame_count ):
        print( "Value at %s : %s"%(n, bez_col[n].value ) )
        ```
        """
        return BezierColumnValue()
    
    def create_Point(self,frame:float, value:float, handleLeftX:float, handleLeftY:float, handleRightX:float, handleRightY:float, constSeg:bool, continuity:str):
        """
        Creates or sets a keyframe point on the Bezier column.

        Parameters
            frame	: Frame number for the point.
            value	: Value of the column at the given point
            handleLeftX	: X value for the left handle of the point.
            handleLeftY	: Y value for the left handle.
            handleRightX	: X value for the right handle.
            handleRightY	: Y value for the right handle.
            constSeg	: Boolean expression (with a true or false value) to indicate whether the segment is constant or interpolated.
            continuity	: String value for the continuity of the point. The string must be in all upper-case. The following are the acceptable values: STRAIGHT, SMOOTH and CORNER.
        """
        return
    
    def keyframes_clear(self, startFrame:int=1, endFrame:int=-1):
        """
        Removes the keyframe(s) located at the given range.

        Parameters
            startFrame	: The starting frame number of the range, inclusive.
            endFrame	: The ending frame number of the range, inclusive.
        """
        return
    
    def keyframe_exists(self, frame:int) -> bool:
        """
        Returns true if the column has a keyframe at the given argument.

        Parameters
            frame	: The frame number or list of frame numbers to retrieve the value from.
        
        Returns
            Returns true there is a keyframe at the given frame.
        """
        return True
    
    def keyframe_create(self, frame:int):
        """
        Set or add a keyframe at the given frame.

        The value evaluated at the given frame will be the keyframe's value.

        Parameters
            frame	: The frame number or list of frame numbers to retrieve the value from.
            """
        return
    
    def keyframe_remove(self, frame:int):
        """Remove the keyframe at the given frame, if any."""
        return
    
    def keyframe_list(self) -> list:
        """
        Returns the list of frames at which there's a keyframe.

        Returns
            Returns the list of frames at which there's a keyframe
        """
        return []
    
    def get_entry(self, atFrame:float, subColumnIndex:int=-1):
        """
        Returns the value of a cell in a column.

        Parameters
            atFrame	: The frame number at which to retrieve the value from.
            subColumnIndex	: The index of the sub-column. Only 3D Path columns support sub-column. They have sub-columns for the X, Y, Z and velocity values on the 3D Path. Each sub-column has an index:
            X = 1
            Y = 2
            Z = 3
            Velocity = 4

        Returns
            Returns the value of a cell in a column.
        """
        return
    
    def set_entry(self, atFrame:float, value, subColumnIndex:int=-1):
        """
        Sets the value of a cell in a column.

        Parameters
            atFrame	The frame number at which to set the value to.
            value	: the new value
            subColumnIndex	: The index of the sub-column. Only 3D Path columns support sub-column. They have sub-columns for the X, Y, Z and velocity values on the 3D Path. Each sub-column has an index:
            X = 1
            Y = 2
            Z = 3
            Velocity = 4
        """
        return
    
    def scale(self, scale_factor:float):
        """Scales the values in a column by a scaling factor."""
        return
    
    @property
    def hold_start(self) -> int:
        """The start value of the hold."""
        return 1
        
    @property
    def hold_stop(self) -> int:
        """The stop value of the hold."""
        return 1
        
    @property
    def hold_step(self) -> int:
        """The step value of the hold."""
        return 1
        
    @property
    def control_point_size(self) -> int:
        """The number of control points in the column."""
        return 1
        
    @property
    def control_points(self):
        """Get the controlpoints in the column."""
        return ControlPointList()
        
    @property
    def name(self) -> str:
        """Get/set the name of the column. This is the internal name of the column which is used as a unique identifier."""
        return ""
        
    @property
    def display_name(self) -> str:
        """Get/Set the displayable name of the column (like it would appear in the xSheet view)."""
        return ""
        
    @property
    def type(self) -> str:
        """Get the type of the node."""
        return ""
        
    @property
    def anonymous(self) -> str:
        """Get/set the anonymous state of the column."""
        return ""
        
    @property
    def linked_nodes(self) -> List[Node]:
        """Identifies nodes that are linked to the column."""
        return [Node()]
        
    @property
    def linked_attributes(self) -> List[Attribute]:
        """Identifies attributes that are linked to the column."""
        return [Attribute()]

class ColumnValue(BaseObject):
    """A frame-value object that is provided from a column's list[idx] operator or iterator."""
    def __init__(self):
        super().__init__()
    
    @property
    def frame(self) -> float:
        """The frame at which the object provides a value."""
        return 1.0
        
    @property
    def value(self) -> float:
        """The value at the given frame."""
        return 1.0
    

class BezierColumnValue(ColumnValue):
    """
    The value provided by a BezierColumn when accessed as a list, or iterated.

    This object provides the value of a Bezier Column when accessed as a list. Print Column Values
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    columns = scene.columns                                      #The overall node list of the scene.
    bez_col = columns["BEZIER_COLUMN_NAME"]
    at_frame = 1
    col_frame_val = bez_col[at_frame]                            #Accessing as a list using 'at_frame'
    print( "Value at frame %s : %s"%(col_frame_val.frame, col_frame_val.value) )
    ```
    """
    def __init__(self):
        super().__init__()
    
    @property
    def frame(self) -> float:
        """The frame for which this object provides a value."""
        return 1.0
        
    @property
    def value(self) -> float:
        """The value at the given frame."""
        return 1.0
        
    @property
    def key(self) -> bool:
        """True if the given frame is a keyframe on the Bezier column."""
        return True
        
    @property
    def const_segment(self) -> bool:
        """True to indicate that the point is on a constant segment, or false to indicate that the point is not on a constant segment."""
        return True
        
    @property
    def continuity(self) -> str:
        """The continuity of the curve that follows the point. One of the following values will be returned, in upper-case: SMOOTH, CORNER or STRAIGHT."""
        return ""
        
    @property
    def handle_left_x(self) -> float:
        """The X value of the left handle of a point on the column."""
        return 1.0
        
    @property
    def handle_left_y(self) -> float:
        """The Y value of the left handle of a point on the column."""
        return 1.0
        
    @property
    def handle_right_x(self) -> float:
        """The X value of the right handle of a point on the column."""
        return 1.0
        
    @property
    def handle_right_y(self) -> float:
        """The Y value of the right handle of a point on the column."""
        return 1.0
        
    @property
    def keyframe_previous(self):
        """The previous frame at which there is a keyframe present, this frame value object if its currently a keyframe."""
        return BezierColumnValue()
        
    @property
    def keyframe_next(self):
        """The next frame at which there is a keyframe present. If none are present, returns none."""
        return BezierColumnValue()

class ControlPoint(BaseObject):
    """
    The control point base class, this is specialized for the specific column types that provide specialized ControlPoint types.

    For more information, see the following:

    OMC::KeyframeableColumn : The generic Keyframeable Column interface.
    OMC::BezierColumn : A column providing an interpolated value from a bezier curve defined by control points.
    OMC::EaseColumn : A column providing a value based on interpolated easing points.
    OMC::Path3DColumn : A column providing a 3D Point value based on a path, keypoints and a velocity.
    OMC::QuaternionColumn : A column providing a quaternion rotation value.
    OMC::VeloBasedColumn : A column providing a value based on a curve path and a velocity.
    """
    def __init__(self):
        super().__init__()
    
    @property
    def frame(self) -> float:
        """The X value (the frame floating point number) of the control point on its column."""
        return 1.0
        
    @property
    def value(self):
        """The value of this control point."""
        return
    
class BezierControlPoint(ControlPoint):
    """
    An object that represents the control point of bezier column.

    Provided by OMC::BezierColumn::control_points. Provides the keyframes and keyframe options associated with a keyframeable bezier column.
    Look Through Bezier Keyframes
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    columns = scene.columns                                      #The overall column list of the scene.
    bez_col = columns["BEZIER_COLUMN_NAME"]
    keyframes = bez_col.control_points                           #This list provides BezierControlPoint objects.
    for keyframe in keyframes:
    print( "Key At: %s %s"%(keyframe.frame, keyframe.value)  )
    ```
    """
    def __init__(self):
        super().__init__()
    
    @property
    def value(self) -> float:
        """The Y value of the control point on its function curve."""
        return 1.0
        
    @property
    def const_segment(self) -> bool:
        """True to indicate that the point is on a constant segment, or false to indicate that the point is not on a constant segment."""
        return True
        
    @property
    def continuity(self) -> str:
        """The continuity of the curve that follows the point. One of the following values will be returned, in upper-case: SMOOTH, CORNER or STRAIGHT."""
        return ""
        
    @property
    def handle_left_x(self) -> float:
        """The X value of the left handle of a point on the column."""
        return 1.0
        
    @property
    def handle_left_y(self) -> float:
        """The Y value of the left handle of a point on the column."""
        return 1.0
        
    @property
    def handle_right_x(self) -> float:
        """The X value of the right handle of a point on the column."""
        return 1.0
        
    @property
    def handle_right_y(self) -> float:
        """The Y value of the right handle of a point on the column."""
        return 1.0
        
    @property
    def frame(self) -> float:
        """The X value (the frame floating point number) of the control point on its column."""
        return 1.0
    

class BoolAttribute(Attribute):
    """
    The boolean attribute wrapper.

    This object wraps a bool attribute owned by a node. The bool attribute is an attribute that provides a true or false value and is not animateable.

    Using a Bool Attribute
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    node = scene.nodes["Top/Node"]                               #Find the peg node.
    proj.history.begin( "Changing Bool Attribute" )              #Start a history action.
    bool_attribute_keyword = "ENABLE_3D"                         #The path to a bool attribute
    attribute = node.attributes[bool_attribute_keyword]          #Get the attribute by name
    if attribute:
    at_frame = 1  
    current_value = attribute.value(at_frame)                  #Get the attribute's value.
    print( "CURRENT VALUE: %s"%( current_value ) )             #Show the current value of the attribute. Note, the bool attribute is not animateable.
                                                                #The frame arg is exists for consistency with other attributes, but is ignored.
    
    attribute.set_value( at_frame, not current_value )         #Set the current value to its inverse.
    new_value = attribute.value(at_frame)                      #Get the attribute's new value after having been changed.
    print( "NEW VALUE: %s"%( new_value ) )                     #Show the new value of the attribute.
                                                                
    else:
    print( "Unable to find attribute by keyword: %s"%(bool_attribute_keyword) )
    proj.history.end( )
    ```
    """
    def __init__(self):
        super().__init__()
    
    def localvalue(self) -> bool:
        """
        Get the attribute's localvalue as a bool value.

        Provides the localvalue as a bool value. The local value is the non-animateable value of an attribute when no column is present. If the attribute can be linked and has a column linked to it, the value at a frame is provided by the column and the local value is ignored.

        Note
        Its generally better to reference the value over the localvalue. When no column is present, the value will also provide the localvalue – this is not true in reverse, if a column is present, the localvalue will still reference the ignored localvalue. Non-animateable attributes that cannot be linked will only provide the localvalue.


        Retrieve a Bool Localvalue
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Node"]                               #Find the peg node.
        bool_attribute_keyword = "ENABLE_3D"                         #The path to a bool attribute
        attribute = node.attributes[bool_attribute_keyword]          #Get the attribute by name
        if attribute:
        current_value = attribute.localvalue()                     #Get the attribute's localvalue.
        print( "LOCALVALUE: %s"%( current_value ) )                #Show the localvalue of the attribute. Note, the bool attribute is not animateable.                                                   
        else:
        print( "Unable to find attribute by keyword: %s"%(bool_attribute_keyword) )
        ```
        """
        return True
    
    def value(self, frame:int) -> bool:
        """
        Get the attribute's value as a bool value at a given frame.

        Provides the value as a bool value. If the attribute can be linked and has a column linked to it, the value at a frame is provided by the column and the local value is ignored.


        Retrieve a Bool Value
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Node"]                               #Find the peg node.
        bool_attribute_keyword = "ENABLE_3D"                         #The path to a bool attribute
        attribute = node.attributes[bool_attribute_keyword]          #Get the attribute by name
        if attribute:
        at_frame = 1
        current_value = attribute.value(at_frame)                       #Get the attribute's value at frame 1 -- the attribute is non-animateable, 
                                                                        #and the value will be the same as localvalue.
        print( "VALUE AT FRAME %s : %s"%( at_frame, current_value ) )   #Show the value of the attribute. Note, the bool attribute is not animateable.
        else:
        print( "Unable to find attribute by keyword: %s"%(bool_attribute_keyword) )
        ```
        """
        return True
    
    def set_localvalue(self, value:bool):
        """
        Sets the attribute's local value as a bool value.

        Sets the local value of the attribute to the provided bool value. The local value is the non-animateable value of an attribute when no column is present. If the attribute can be linked and has a column linked to it, the value at a frame is provided by the column and the local value is ignored.

        Note
        Its generally better to reference the value over the localvalue. When no column is present, the value will also provide the localvalue – this is not true in reverse, if a column is present, the localvalue will still reference the ignored localvalue. Non-animateable attributes that cannot be linked will only provide the localvalue.
        
        Parameters
            value	- the bool value to which the attribute should be set.


        Set a Bool Localvalue
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Node"]                               #Find the peg node.
        bool_attribute_keyword = "ENABLE_3D"                         #The path to a bool attribute
        attribute = node.attributes[bool_attribute_keyword]          #Get the attribute by name
        if attribute:
        current_value = attribute.localvalue()                     #Get the attribute's localvalue.
        print( "CURRENT LOCALVALUE: %s"%( current_value ) )        #Show the current localvalue of the attribute. Note, the bool attribute is not animateable.
        
        attribute.set_localvalue( not current_value )              #Set the attribute's local value to the opposite value.
        new_value = attribute.localvalue()                         #Get the attribute's new localvalue, to check it for debug/example purposes
        print( "NEW LOCALVALUE: %s"%( new_value ) )                #Show the new localvalue of the attribute.
        
        else:
        print( "Unable to find attribute by keyword: %s"%(bool_attribute_keyword) )
        ```
        """
        return
    
    def set_value(self, frame:int, value:bool):
        """
        Set the attribute's value as a bool value at a given frame.

        Sets the value of the attribute to the provided bool value at the given frame. If the attribute can be linked and has a column linked to it, the value is set on the column – otherwise, it is set on the localvalue of the attribute.

        Parameters
            frame	- the frame at which the attribute is set – for bool attributes, this is will be ignored but is kept for consistency with other attributes.
            value	- the bool value to which the attribute should be set.


        Set a Bool Value at a Frame
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Node"]                               #Find the peg node.
        bool_attribute_keyword = "ENABLE_3D"                         #The path to a bool attribute
        attribute = node.attributes[bool_attribute_keyword]          #Get the attribute by name
        if attribute:
        at_frame = 1
        current_value = attribute.value( at_frame )                                  #Get the attribute's value.
        print( "CURRENT VALUE AT FRAME %s : %s"%( at_frame, current_value ) )        #Show the current value of the attribute. Note, the bool attribute is not animateable.
        
        attribute.set_value( at_frame, not current_value )                           #Set the attribute's value to the opposite value.
        new_value = attribute.value(at_frame)                                        #Get the attribute's new localvalue, to check it for debug/example purposes
        print( "NEW VALUE AT FRAME %s : %s"%( at_frame, new_value ) )                #Show the new localvalue of the attribute.
        
        else:
        print( "Unable to find attribute by keyword: %s"%(bool_attribute_keyword) )
        ```
        """
        return
    
    def node(self) -> Node:
        """
        The node that owns this attributes.

        Retrieves the Node that owns this attribute.

        Returns
            Returns the owning OMC::Node object related to this attribute.
        """
        return Node()
    
    def unlink(self) -> bool:
        """
        Unlinks a column from the attribute.

        Returns
            Returns whether the column has been successfully removed from the attribute.
        
        Unlinks any column from the attribute.
        Also see OMC::Column::column with property None.

        ```python
        node.attribute["attrbKeyword"].unlink()
        #Same as:
        node.attribute["attrbKeyword"].column = None
        ```
        """
        return True
    
    def link(self, column) -> bool:
        """
        Links a column to the attribute, making it animate over time.

        Returns
            Returns whether the column has been successfully linked to the attribute.
        
        Links a column to the attribute, if the column is compatible with the attribute type. Also see setting OMC::Column::column with a Column object property.
        """
        return True
    
    def set_text_value(self, atFrame:int, value:str):
        """
        Modify an attribute with a text value at a given frame. Change an attribute with a text value applied at a specific frame. This provides similar utility as the Javascript libraries available for the application.

        Parameters
            atFrame	- The frame at which to set the attribute.
            value	- The new value of the attribute.
        
        Returns
            Returns whether the attribute has been successfully changed.
        """
        return
    
    def get_text_value(self, atFrame:int) -> str:
        """
        Get a text value at a given frame. Retrieve the text value of an attribute at a specific frame. This provides similar utility as the Javascript libraries available for the application.

        Parameters
            atFrame	- The frame at which to set the attribute.
        
        Returns
            Returns the text value of the string at the given frame.
        """
        return ""
    
    
class Cable(BaseObject):
    """
    Represents and provides the methods for a cable connecting nodes in the node view.

    The cable is the representation of a connection between Ports on a Node, and is useful for tracing the connection between nodes.

    Follow a Cable
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    peg = scene.nodes["Top/Peg"]                                 #Find the peg node.
    #We'll simply follow this peg's connection downwards via the first available connection to the 0th port.
    #Using a method so that it can be called for each node that is followed.
    def recursive_cable_follower( node ):
    print( "Following : %s "%(node.path) )
    try:
        port = node.ports_out[0]    
        cable = port.cables[0]                                   #Use the first attached cable to this port.
        next_node = cable.destination_node                       #Where does this cable connect to next?
        
        recursive_cable_follower( next_node )                    #Follow the next node. . . 
        
    except:
        print( "Failed to continue -- is there any valid connection?" )
    recursive_cable_follower( peg )
    ```
    """
    def __init__(self):
        super().__init__()
    
    def insert(self, node:Node, inPort, outPort):
        """Insert a node in between the currently connected nodes by this cable."""
        return Cable()
    
    def unlink(self):
        """Disconnect the cable."""
        return
    
    @property
    def source(self):
        """Get and set the source port from which this cable is connected."""
        return OutPort()
        
    @property
    def source_node(self) -> Node:
        """Get and set the source node from which this cable is connected."""
        return Node()
        
    @property
    def destination(self):
        """Get and set the destination port to which this cable is connected."""
        return InPort()
        
    @property
    def destination_node(self) -> Node:
        """Get the destination node to which this cable is connected."""
        return Node()
        
    @property
    def source_flat_node(self) -> Node:
        """Get the node from which this cable is connected, ignoring all waypoints, groups and multiports."""
        return Node()
        
    @property
    def source_flat(self):
        """Get the node from which this cable is connected, ignoring all waypoints, groups and multiports."""
        return Port()
    
class CableList(ListObj, IterableObj):
    """
    Provides a list of OMC::Cables attached to an OutPort.

    The CableList provides a dynamic list of cables attached to an OutPort, that connect the port to an InPort of another Node.
    This is provided from OutPort::cables
    List Cables Attached to a Node's Port

    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    peg = scene.nodes["Top/Peg"]                                 #Find the peg node.
    out_port = peg.ports_out[0]                                  #The first Out Port of a node.
    cablelist = out_port.cables
    print( "Number of Cables : %s"%len( cablelist ) )            #Print the amount of cables attached to the port.
    for idx,cable in enumerate(cablelist):
    print( "Cable %s : %s"%(idx, cable.destination_node.path) ) #Print what the cable is connected to.
    ```
    """
    def __init__(self):
        super().__init__()
    
    def contains(self, cable:str) -> bool:
        """Identifies if the list contains the cable."""
        return
    
    def list(self) -> List[Cable]:
        """Converts the dynamic list into a concrete list of cable objects."""
        return [Cable()]
    
    def __getitem__(self, idx:int, searchString:str) -> Cable:
        """
        [1/2] - searchString
        
        Search for an cable in the node with a specialized search string. Search string formatting to be discussed.

        Returns
            The cable found at the given string.
        
        ------------------------------------------------------------------------
        [2/2] - idx

        The CableList object is is iterable and can provide values at given index with the list operator.

        ```python
        Print Column Values

        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        peg = scene.nodes["Top/Peg"]                                 #Find the peg node.
        try:
        out_port = peg.ports_out[0]                                #The first Out Port of a node.
        cablelist = out_port.cables
        
        print( "Port has %s Cables"%(len(cablelist)) )
        for n in range( len(cablelist) ):
            print( "%s Cable : %s"%(n, cablelist[n].destination_node.path) )
        except:
        print( "Failed, does the node or port exist?" )
        ```
        """
        return Cable()

class CameraNode(Node):
    """
    Represents and provides the methods for a camera node.

    The camera node represents a camera within the scene. The camera, along with an attached transformation, will define the position, scale and field of view of the viewport and will affect OpenGL and final renders when it is active.
    """
    def __init__(self):
        super().__init__()
    
    def matrix(self, frame:int):
        """
        Gets the matrix of the camera at the given frame.

        Provides the current transformation matrix that is being used to transform the camera's position, scale and rotation within the scene.
        Returns
            OMC::Matrix of camera at given frame.

        Identify Details of Camera Transform
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        camera = scene.nodes["Top/Camera"]                           #Find the camera node.
        matrix = camera.matrix( 1 )
        matrix_values = matrix.extract_parameters_3d( harmony.Point3d() )
        print( "Translation : %s"%(matrix_values[0]) )
        print( "Scale       : %s"%(matrix_values[1]) )
        print( "Rotation    : %s"%(matrix_values[2]) )
        ```
        """
        return Matrix()
    
    @property
    def active(self) -> bool:
        """
        Get and sets if the camera is currently active.

        The property defines whether the camera is currently active in the scene. Only one camera can be active in the scene at a time. This serves the same purpose as OMC::Scene::camera, but allows one to set the scene's active camera from the node.
        """
        return True
    
class Cel(BaseObject):
    """
    An object that contains a reference to a rendered cel (image) in the application.

    This is generally provided from the Render Handler (OMH::HarmonyRenderHandler) when a slot or callback function is provided for the on_frame_ready event. The cel represents a rendered image in memory, and provides tools to export it to a file format as needed.

    A Render Handler with a Frame-Ready Callback

    ```python
    from PySide6.QtGui     import QPixmap, QScreen
    from PySide6.QtWidgets import QApplication, QWidget, QLabel, QSizePolicy, QVBoxLayout
    import tempfile
    import math
    import os
    from ToonBoom import harmony                                 #Import the Harmony Module
    #Helper Class to Render the Results into -- this is pure PySide Qt
    class ImageShow(QWidget):
    def __init__(self):
        super().__init__()
        self.init()
    def init(self):
        self.setWindowTitle( "Render-Tester" )
        self.label = QLabel(self)
        self.pixmap = QPixmap()
    def setImage(self, path, title, frame, count):
        self.setWindowTitle( title )
        
        frmn = frame-1  #0-indexed frame
        squared = int(math.sqrt(count)+0.5)
        offsetx = frmn%squared
        offsety = int(frmn/squared)
        screenSize = QScreen.availableGeometry( QApplication.primaryScreen() )
        width_target  = screenSize.width()/squared
        height_target = screenSize.height()/squared
        self.resize( width_target, height_target )
        self.pixmap.load( path )
        self.label.setPixmap( self.pixmap.scaled( self.width(), self.height() ) );
        
        frmX = ( screenSize.width () - self.width () ) / 2.0
        frmY = ( screenSize.height() - self.height() ) / 2.0
        self.move( offsetx*width_target, offsety*height_target )
        self.show()
    def resizeEvent( self, event ):
        self.label.setPixmap( self.pixmap.scaled( self.width(), self.height() ) )
        self.label.resize( self.width(), self.height() )
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    nodes = scene.nodes
    readnode = False
    #This will keep the displayers alive -- otherwise they'll open and close as it leaves the method.
    displayers = []
    #Find the first avbailable read node.
    for node in nodes:
    if node.type.upper() == "READ":
        readnode = node
        break
    if readnode:
    print( "Rendering %s"%(readnode.path) )
    renderhandler = proj.create_render_handler()                        #Create a new render handler.
    frame_count = 25 
    def renderhandler_ready_frame( node, frame, cel ):                  #This will be the callback function
        displayer = ImageShow()                                           #A helper utility for showing the rendered images.
        displayers.append( displayer )                                    #Keep it alive.
        print( "Frame Ready : %s at %s"%(node.path, frame) )
        
        #The callback provides a frame.
        frame_output = os.path.join( tempfile.gettempdir(), "%s.%05d.png"%(node.name, frame) )
        print( "Saving to: %s"%(frame_output) )
        
        cel.write( frame_output )                                                        #Write the cel to a temp directory.
        
        #Show it!
        displayer.setImage( frame_output,  "%s at %s"%(node.path, frame), frame, frame_count )       
    renderhandler.frame_ready_callback = renderhandler_ready_frame                     #Add the callback function to the handler.
                                                                                    
    renderhandler.node_add( readnode )                                                 #Add the readnode to the list of nodes to render.
    renderhandler.render( 1, frame_count )                                             #Render the frames 1-10
    
    else:
    print( "Unable to find a Read Node to render." )
    ``` 
    """
    def __init__(self):
        super().__init__()
    
    def allocated_rect(self):
        """Retrieve allocated area of sparse image. Is equal to full area for non-sparse images. Allocated rect. 4-tuple (x1, y1, width, height)."""
        return Rect2D()
    
    def rect(self):
        """Retrieve full area of image. Full rect. 4-tuple (x1, y1, width, height)."""
        return Rect2D()
    
    def cel3D(self) -> bool:
        """True if the cel a 3D cel."""
        return True
    
    def write(self, path:str, formatstring:str, optionstring:str):
        """
        [1/3] - no args

        Get a permanent copy of cel image file. This function without parameters is valid only for ports that point to a physically valid file on disk.
        ------------------------------------------------------------------------
        [2/3] - path

        Get a permanent copy of cel image file of specific format.

        Parameters
            path	File path to the file to create

        ------------------------------------------------------------------------
        [3/3] - path + formatstring + optionstring

        Get a permanent copy of cel image file of specific format.

        Parameters
            path	File path to the file to create
            formatstring	Format to convert image into
            optionstring	Image extension specific option (ie. TGA, TGA3, TGA4, SGIDP)
        """
        return

class Clipboard(BaseObject):
    """
    Provides copy and paste functionality.

    The clipboard object is provided from the scene (OMH::HarmonyScene) and provides access to copy and paste functionality. It is useful for copying content from a scene or templates and reusing it in different locations.

    Copying Content
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    clipboard = scene.clipboard                                  #The clipboard object.
    selection_handler = scene.selection                          #The selection handler.
    selection_handler.nodes.select_all()                         #Select all nodes in the scene.
    copy_object = clipboard.copy( selection_handler.nodes.list() )    #Create a copy_object in memory from the selection.
    selection_handler.select_none()
    new_nodes = clipboard.paste_new_nodes( copy_object, scene.top )   #Paste duplicate nodes into the top-group of the scene.
    for node in new_nodes:
    print( "Pasted: %s"%(node.path) )                               #Announce the new node's path
    if node.parent_group().path == scene.top.path:
        node.position.y = node.position.y + 300                         #Move it up, to avoid overlap with existing content
    ```

    Create a Template
    ```python
    import os
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    clipboard = scene.clipboard                                  #The clipboard object.
    selection_handler = scene.selection                          #The selection handler.
    selection_handler.nodes.select_all()                         #Select all nodes in the scene.
    copy_object = clipboard.copy( selection_handler.nodes.list() )    #Create a copy_object in memory from the selection.
    output_path = os.path.expanduser( "~/Template_Example" )
    directory = clipboard.create_template(copy_object, "Template_Example", output_path, False )
    if directory and len(path)>0:
    full_path = os.path.join( output_path, directory )
    if os.path.exists(full_path):
        print( "Output a Template: %s"%(full_path) )
    else:
    print( "Failed to output a template." )
    ```
    """
    def __init__(self):
        super().__init__()
    
    def paste_template(self, templateSrcPath:str, insertFrame:int, column, options):
        """
        Pastes the template into the scene.

        Parameters
            templateSrcPath	: The path of the template.
            insertFrame	: The frame at which insert commences.
            column	: The name of the existing column in which template will be inserted.
        """
        return
    
    def paste_template_into_group(self, srcPath:str, insertFrame:int, group, options) -> bool:
        """
        Pastes the template into a group of the scene.

        Parameters
            srcPath	: The path of the template.
            groupName	: The name of the group node into which the template will be pasted.
            insertFrame	: The frame at which insert commences.

        Returns
            Returns true if successful.
        """
        return True
    
    def paste_action_template(self, srcPath:str, insertFrame:int, node, compositionOptions, options):
        """
        Pastes the action template into the scene and excludes nodes that are in the list.

        Parameters
            srcPath	: The path of the template.
            nodeName	: The name of the existing node in which we will insert template.
            insertFrame	: The frame at which insert commences.
            compositionOptions	: Defines how to handle the selection of nodes onto which to paste. Separately controls to paste of groups, effects and composite nodes when building the selection. Default value: { "groups": true, "effects": true, "composites": false }
        
        Returns
            Returns true if successful.
        """
        return
    
    def copy(self, nodePaths:List[str], startFrame:int=1, numFrames:int=0, copyOptions=None):
        """
        Create an object that represent a 'copy' of a selection of nodes and a range of frames.

        Create an object that represent a 'copy' of a selection of nodes and a range of frames. This object can be pasted or saved in the template library. It is practically identical to what the user would copy from a selection of layers and frames in the timeline.

        Parameters
            nodePaths	: The list of nodes to be copied.
            createOption	: Options that should be used when doing the creating the copy. See SCR_CopyOptions for more information about these options.
        
        Returns
            Returns a newly created 'drag object' that represent a copy of the selection. The drag object can be saved or pasted back to the scene (using the paste() function)
            NULL if unable to create a dragobject.
        """
        return CopyObject()
    
    def paste(self, copyObject, nodePaths:List[str], startFrame:int=1, numFrames:int=0, pasteOptions=None):
        """
        Pastes the drag object as an action template. Must paste over a selection of nodes. No new nodes are created by this action.

        Parameters
            copyObject	: The dragObject to be pasted.
            selectionOfNodes	: The list of nodes to be pasted over.
            startFrame	: The start frame for the selection. First frame is 1.
            numFrames	: The number of frames to paste across.
            pasteOptions	: Options that should be used when pasting. See SCR_PasteOptions for more information about these options.
        """
        return
    
    def paste_new_nodes(self, copyObject, group, pasteOptions=None):
        """
        Paste an external drag object as new nodes. This is similar to pasting on the node view where new nodes are created (from an external selection).

        Parameters
            copyObject	- the actual drag object - see copy() or copyFromTemplate() to create this drag object.
            group	- root group where the new nodes will be created. If empty string is provided, it will paste at the root.
            pasteOptions	- paste special options (ie. create keyframes, drawings, new columns, or relink columns,.... - see paste special dialog and SCR_PasteOptions).
        
        Returns
            The pasted nodes.
        """
        return Node()
    
    def copy_from_template(self, filename:str, startFrame:int=1, numFrames:int=0, copyOptions=None):
        """
        Load a template from the file system onto a copy object, which can then be pasted onto the scene.

        Parameters
            filename	- the exact filename of the .tpl folder. Need to be the folder, not the .xstage file.
            startFrame	start frames for the data pasted. Starting at 1. However, if 0 is provided, the whole template is copied.
            numFrames	- number of frames to paste, up to the maximum number of frames. If 'startFrame' is 0, this parameter is disregarded.
            createOption	- options that should be used when doing the code. See SCR_CopyOptions for more information about these options.
        
        Returns
            Returns a new created copy.
        """
        return CopyObject()
    
    def create_selection_template(self, name:str, path:str, copyOptions=None) -> str:
        """
        Creates template from the current selection in the scene, using only the current drawing versions.

        No template is created when there is nothing selected, when the path is not valid or when there is an IO error.

        Parameters
            name	: The name of the new template.
            path	: The location of the new template.
            copyOptions	: Options to define how the selection is copied when templated.
        
        Returns
            Returns the full path of the new template. Will return an empty string if no template file was created.
        """
        return ""
    
    def create_template(self, copyObject, name:str, path:str, addDefaultCamera:bool=False) -> str:
        """
        Creates template from the copy object using only the current drawing versions.

        No template is created when there is nothing selected, when the path is not valid or when there is an IO error.

        Parameters
            name	: The name of the new template.
            path	: The location of the new template.
            addDefaultCamera	: Whether the default camera should be included in the template.
        
        Returns
            Returns the directory name of the new template. Will return an empty string if no template file was created.
        """
        return ""

class Colour(BaseObject):
    """
    A generic colour object that can be used as a colour argument for some internal methiods.

    Create a Colour Object
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    colour_object = harmony.Colour( 255, 0, 0, 255 )             #RED!
    colour_object = harmony.fromHSL( 180, 100, 100, 100 )        #CYAN!
    ```
    """
    def __init__(self, r:int=255, g:int=255, b:int=255, a:int=255):
        super().__init__()
    
    @staticmethod
    def fromHSL(h:float, s:float, l:float, a:float):
        return Colour()
    
    @property
    def r(self) -> int:
        """Get and set the red value of the colour 0-255."""
        return 1
        
    @property
    def g(self) -> int:
        """Get and set the green value of the colour 0-255."""
        return 1
        
    @property
    def b(self) -> int:
        """Get and set the blue value of the colour 0-255."""
        return 1
        
    @property
    def a(self) -> int:
        """Get and set the alpha value of the colour 0-255."""
        return 1
        
    @property
    def h(self) -> float:
        """Get and set the hue value of the colour 0-360.0."""
        return 1.0
        
    @property
    def l(self) -> float:
        """Get and set the lightness value of the colour 0-100.0."""
        return 1.0
            
    @property
    def s(self) -> float:
        """Get and set the saturation value of the colour 0-100.0."""
        return 1.0
            
    @property
    def hex(self) -> str:
        """Get and set the hex value of the node in form #FFFFFF."""
        return ""
    
class ColourAttribute(Attribute):
    """
    The colour attribute wrapper.

    This object wraps a colour attribute owned by a node. The colour attribute is an attribute that provides a OMC::Colour value and can be animateable.
    """
    def __init__(self):
        super().__init__()
    
    def localvalue(self) -> Colour:
        """
        Get the attribute's localvalue as a OMC::Colour value.

        Provides the localvalue as a OMC::Colour value. The local value is the non-animateable value of an attribute when no column is present. If the attribute can be linked and has a column linked to it, the value at a frame is provided by the column and the local value is ignored.

        Note
        Its generally better to reference the value over the localvalue. When no column is present, the value will also provide the localvalue – this is not true in reverse, if a column is present, the localvalue will still reference the ignored localvalue. Non-animateable attributes that cannot be linked will only provide the localvalue.


        Retrieve a OMC::Colour Localvalue
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Colour-Card"]                        #Find the Colour Card node.
        color_attribute_keyword = "COLOR"                            #The path to a color attribute
        attribute = node.attributes[color_attribute_keyword]         #Get the attribute by name
        if attribute:
        current_value = attribute.localvalue()                     #Get the attribute's localvalue.
        #Show the localvalue of the attribute.
        print( "LOCALVALUE: %s %s %s %s"%( current_value.r, current_value.g, current_value.b, current_value.a ) )       
        else:
        print( "Unable to find attribute by keyword: %s"%(color_attribute_keyword) )
        ```
        """
        return Colour()
    
    def value(self, frame:int):
        """
        Get the attribute's value as a OMC::Colour value at a given frame.

        Provides the value as a Colour value. If the attribute can be linked and has a column linked to it, the value at a frame is provided by the column and the local value is ignored.


        Retrieve a Colour Value
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Colour-Card"]                        #Find the Colour Card node.
        colour_attribute_keyword = "COLOR"                           #The path to a Colour attribute
        attribute = node.attributes[colour_attribute_keyword]        #Get the attribute by name
        if attribute:
        at_frame = 1
        current_value = attribute.value(at_frame)                       #Get the attribute's value at frame 1
                                                                        #and the value will be the same as localvalue.
        #Show the value of the attribute.
        print( "VALUE AT FRAME %s : %s %s %s %s"%( at_frame, current_value.r, current_value.g, current_value.b, current_value.a ) )  
        else:
        print( "Unable to find attribute by keyword: %s"%(colour_attribute_keyword) )
        ```
        """
        return
    
    def set_localvalue(self, value:Colour):
        """
        Sets the attribute's local value as a OMC::Color value.

        Sets the local value of the attribute to the provided OMC::Color value. The local value is the non-animateable value of an attribute when no column is present. If the attribute can be linked and has a column linked to it, the value at a frame is provided by the column and the local value is ignored.

        Note
        Its generally better to reference the value over the localvalue. When no column is present, the value will also provide the localvalue – this is not true in reverse, if a column is present, the localvalue will still reference the ignored localvalue. Non-animateable attributes that cannot be linked will only provide the localvalue.
        Parameters
        value	- the OMC::Colour value to which the attribute should be set.


        Set a OMC::Color Localvalue
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        import random
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Colour-Card"]                        #Find the CC node.
        colour_attribute_keyword = "COLOR"                           #The path to a Colour attribute
        attribute = node.attributes[colour_attribute_keyword]        #Get the attribute by name
        if attribute:
        current_value = attribute.localvalue()                     #Get the attribute's localvalue.
        #Show the current localvalue of the attribute.
        print( "CURRENT LOCALVALUE: %s %s %s %s"%( current_value.r, current_value.g, current_value.b, current_value.a ) )        
        new_color = harmony.Colour( random.randint(0,255), random.randint(0,255), random.randint(0,255), random.randint(0,255) )
        attribute.set_localvalue( new_color )                      #Set the attribute's local value to the new value
        new_value = attribute.localvalue()                         #Get the attribute's new localvalue, to check it for debug/example purposes
        print( "NEW LOCALVALUE: %s %s %s %s"%( new_value.r, new_value.g, new_value.b, new_value.a ) )   
        else:
        print( "Unable to find attribute by keyword: %s"%(colour_attribute_keyword) )
        ```
        """
        return
    
    def set_value(self, frame:int, value:Colour, adjustLastKeyframe:bool=False):
        """
        Set the attribute's value as a OMC::Colour value at a given frame.

        Sets the value of the attribute to the provided OMC::Colour value at the given frame. If the attribute can be linked and has a column linked to it, the value is set on the column – otherwise, it is set on the localvalue of the attribute.

        Note
        If no column is present, setting an animateable column's value on the attribute will result in the creation of a new column.
        Parameters
        frame	- the frame at which the attribute is set.
        value	- the OMC::Colour value to which the attribute should be set.


        Set a Colour Value at a Frame
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Colour-Card"]                        #Find the CC node.
        colour_attribute_keyword = "COLOR"                           #The path to a Colour attribute
        attribute = node.attributes[colour_attribute_keyword]        #Get the attribute by name
        if attribute:
        at_frame = 1
        current_value = attribute.value( at_frame )                #Get the attribute's value.
        #Show the current localvalue of the attribute.
        print( "CURRENT VALUE AT %s : %s %s %s %s"%( at_frame, current_value.r, current_value.g, current_value.b, current_value.a ) )
        new_color = harmony.Colour( random.randint(0,255), random.randint(0,255), random.randint(0,255), random.randint(0,255) )
        attribute.set_value( at_frame, new_color )                                                      #Set the attribute's local value to the new value
        new_value = attribute.value( at_frame )                                                         #Get the attribute's new localvalue, to check it for debug/example purposes
        print( "NEW VALUE AT %s : %s %s %s %s"%( at_frame, new_value.r, new_value.g, new_value.b, new_value.a ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(colour_attribute_keyword) )
        ```
        """
        return
    
    def offset_value(self, frameOrRange, value):
        """
        Offsets the attribute's value at a given frame or frame range.

        Provided a OMC::Colour object, will offset the existing value (either the animated value, or local value if none exists) by the color argument's value.

        Parameters
        frameOrRange	-
        value	- The OMC::Colour object to by which the attribute is offset.

        Offset a Color Attribute
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Colour-Card"]                        #Find the CC node.
        colour_attribute_keyword = "COLOR"                           #The path to a Colour attribute
        attribute = node.attributes[colour_attribute_keyword]        #Get the attribute by name
        if attribute:
        at_frame = 1
        current_value = attribute.value( at_frame )                #Get the attribute's value.
        #Show the current localvalue of the attribute.
        print( "CURRENT VALUE AT %s : %s %s %s %s"%( at_frame, current_value.r, current_value.g, current_value.b, current_value.a ) )
        new_color = harmony.Colour( random.randint(-255,255), random.randint(-255,255), random.randint(-255,255), random.randint(-255,255) )
        range = [ at_frame, scene.frame_count ]                    #The range will be from at_frame, to the last frame of the scene.
        attribute.offset_value( range, new_color )                 #Offset the attribute's value by the provided value
        new_value = attribute.value( at_frame )                    #Get the attribute's new localvalue, to check it for debug/example purposes
        print( "NEW VALUE AT %s : %s %s %s %s"%( at_frame, new_value.r, new_value.g, new_value.b, new_value.a ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(colour_attribute_keyword) )
        ```
        """
        return

class ColumnList(ListObj, IterableObj):
    """
    Represents a list of columns in a scene.

    Provided from the OMC::Scene::columns.

    Columns are the time-based objects that provide values to animateable attributes on nodes. The scene's column list (OMC::ColumnList) is a list containing all columns in the scene and can be used to create, modify and remove columns as needed.

    List All Columns:
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    columns = scene.columns                                      #The overall node list of the scene.
    for col in columns:
    print( "Column: %s (%s)"%(col.name, col.type) )
    ```
    """
    def __init__(self):
        super().__init__()
    
    def contains(self, Column) -> bool:
        """Identifies if the list contains the column."""
        return True
    
    def list(self) -> List[Column]:
        """Converts the dynamic list into a concrete list of column objects."""
        return [Column()]
    
    def __getitem__(self, name:str):
        """
        Search for a column in the scene with a specialized search string. Search string formatting to be discussed.

        Returns
            The Column found at the given string.
        """
        return Column()
    
    def create(self, type:str, name:str, options=None):
        """
        Add a column of the given type to the list's scene.

        Parameters
            type	The type of the new column [ Available types: DRAWING, SOUND, 3D_PATH, BEZIER, EASE, EXPR, TIMING, VELOBASED, QUATERNION_PATH, ANNOTATION ]
            name	The name of the new column. If empty, a unique anonymous name will be created.
            options	When creating drawing columns, an option argument provides more utility. In form { "scanType" : "type", "fieldChart" : 12, "pixmapFormat" : "format", "vectorType" : "type", "createNode" : False }
        
        Returns
            The new column object added to the column list.
        """
        return
    
    def linked_nodes(self, Column) -> List[Node]:
        """Identifies nodes that are linked to the column(s)."""
        return [Node()]
    
    def linked_attributes(self, Column) -> List[Attribute]:
        """Identifies attributes that are linked to the column(s)."""
        return [Attribute()]
    

class ControlPointList(ListObj, IterableObj):
    """
    A class representing a list of control points, providing utilities to modify the list.

    Provided from various Column objects that can provide keyframes (OMC::KeyframeableColumn) via the control_points attribute. The type of control point varies based on the type of Column being accessed.

    The ControlPointList is iterable and provides standard list functions (size and index operator).
    For more information, see the following:

    OMC::KeyframeableColumn : The generic Keyframeable Column interface.
    OMC::BezierColumn : A column providing an interpolated value from a bezier curve defined by control points.
    OMC::EaseColumn : A column providing a value based on interpolated easing points.
    OMC::Path3DColumn : A column providing a 3D Point value based on a path, keypoints and a velocity.
    OMC::QuaternionColumn : A column providing a quaternion rotation value.
    OMC::VeloBasedColumn : A column providing a value based on a curve path and a velocity.

    List Control Points on a Column
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    columns = scene.columns                                      #The column list for the scene.
    for column in columns:
    if column.type.upper() == "BEZIER":
        control_point_list = column.control_points
        
        print( "%s has %s Control Points"%(column.name, len(control_point_list)) )
        for control_point in control_point_list:
        print( "    Control Point at %s : %s"%(control_point.frame, control_point.value) )
    ```
    """
    def __init__(self):
        super().__init__()
    
    def __getitem__(self, idx:int) -> ControlPoint:
        """The Control Point List object is is iterable and can provide values at given index with the list operator."""
        return ControlPoint()
    
    def create(self, frame:int):
        """
        Set or add a control point at the given frame.

        The value evaluated at the given frame will be the keyframe's value.

        Parameters
            frame	: The frame number at which the keyframe is set or added.
        """
        return
    
    def remove(self, frame:int):
        """Remove the control point at the given index."""
        return

class CopyObject(BaseObject):
    """
    An object that represents copied content in memory.

    This object is used within OMC::Clipboard and is provided when copying content into memory. It can be used in various methods to reference and paste data afterwards.
    The object doesn't provide any direct utility, but references a unique clipboard object in memory.

    Copying Content
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    clipboard = scene.clipboard                                  #The clipboard object.
    selection_handler = scene.selection                          #The selection handler.
    selection_handler.nodes.select_all()                         #Select all nodes in the scene.
    copy_object = clipboard.copy( selection_handler.nodes.list() )    #Create a copy_object in memory from the selection.
    selection_handler.select_none()
    new_nodes = clipboard.paste_new_nodes( copy_object, scene.top )   #Paste duplicate nodes into the top-group of the scene.
    for node in new_nodes:
    print( "Pasted: %s"%(node.path) )                               #Announce the new node's path
    if node.parent_group().path == scene.top.path:
        node.position.y = node.position.y + 300                         #Move it up, to avoid overlap with existing content
    ```
    """
    def __init__(self):
        super().__init__()

class CopyOptions(BaseObject):
    """Copy Options used in copy methods within OMC::Clipboard."""
    def __init__(self):
        super().__init__()
    
    def CopyOptions(self, options):
        """
        Generate a Copy_Option object from an argument object.

        Generates a Copy_Option object from an object argument in the form: { "add_modelling_dir" : True, "addScanFiles" : True, "include_default_camera_name" : True }
        """
        return
    
    @property
    def add_modelling_dir(self) -> bool:
        """Set to true to copy the modeling directory into the template."""
        return True
        
    @property
    def add_scan_files(self) -> bool:
        """Set to true to copy the scan files associated to the selected drawings."""
        return True
        
    @property
    def include_default_camera_name(self) -> bool:
        """
        Use this when you want the camera in a template to be set as default camera in the target scene.

        Note
        This is not necessary if there is no camera assigned in the target scene, as the incoming camera will automatically be set as default camera.
        """
        return True

class DisplayNode(Node):
    """Represents and provides the methods for a display node."""
    def __init__(self):
        super().__init__()

class DoubleAttribute(Attribute):
    """
    The double attribute wrapper.

    This object wraps a double attribute owned by a node. The double attribute is an attribute that provides a double number value and can be animateable.
    """
    def __init__(self):
        super().__init__()
    
    def localvalue(self) -> float:
        """
        Get the attribute's localvalue as a double value.

        Provides the localvalue as a double value. The local value is the non-animateable value of an attribute when no column is present. If the attribute can be linked and has a column linked to it, the value at a frame is provided by the column and the local value is ignored.

        Note
        Its generally better to reference the value over the localvalue. When no column is present, the value will also provide the localvalue – this is not true in reverse, if a column is present, the localvalue will still reference the ignored localvalue. Non-animateable attributes that cannot be linked will only provide the localvalue.


        Retrieve a Double Localvalue
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Peg"]                                #Find the Peg node.
        double_attribute_keyword = "POSITION.X"                      #The path to a double attribute
        attribute = node.attributes[double_attribute_keyword]        #Get the attribute by name
        if attribute:
        current_value = attribute.localvalue()                     #Get the attribute's localvalue.
        #Show the localvalue of the attribute.
        print( "LOCALVALUE: %s "%( current_value ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(double_attribute_keyword) )
        ```
        """
        return 1.0
    
    def value(self, frame:int) -> float:
        """
        Get the attribute's value as a double value at a given frame.

        Provides the value as a double value. If the attribute can be linked and has a column linked to it, the value at a frame is provided by the column and the local value is ignored.


        Retrieve a Double Value
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Peg"]                                #Find the Peg node.
        double_attribute_keyword = "POSITION.X"                      #The path to a double attribute
        attribute = node.attributes[double_attribute_keyword]        #Get the attribute by name
        if attribute:
        at_frame = 1
        current_value = attribute.value(at_frame)                       #Get the attribute's value at frame 1
        #Show the value of the attribute.
        print( "VALUE AT FRAME %s : %s"%( at_frame, current_value ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(double_attribute_keyword) )
        ```
        """
        return 1.0
    
    def set_localvalue(self, value:float):
        """
        Sets the attribute's local value as a double value.

        Sets the local value of the attribute to the provided double value. The local value is the non-animateable value of an attribute when no column is present. If the attribute can be linked and has a column linked to it, the value at a frame is provided by the column and the local value is ignored.

        Note
        Its generally better to reference the value over the localvalue. When no column is present, the value will also provide the localvalue – this is not true in reverse, if a column is present, the localvalue will still reference the ignored localvalue. Non-animateable attributes that cannot be linked will only provide the localvalue.
        Parameters
        value	- the double value to which the attribute should be set.


        Set a OMC::Color Localvalue
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        import random
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Peg"]                                 #Find the Peg node.
        double_attribute_keyword = "POSITION.X"                       #The path to a double attribute
        attribute = node.attributes[double_attribute_keyword]         #Get the attribute by name
        if attribute:
        current_value = attribute.localvalue()                     #Get the attribute's localvalue.
        #Show the current localvalue of the attribute.
        print( "CURRENT LOCALVALUE: %s"%( current_value ) )
        new_value = random.uniform( attribute.minimum, attribute.maximum )
        attribute.set_localvalue( new_value )                      #Set the attribute's local value to the new value
        new_value = attribute.localvalue()                         #Get the attribute's new localvalue, to check it for debug/example purposes
        print( "NEW LOCALVALUE: %s"%( new_value ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(double_attribute_keyword) )
        ```
        """
        return
    
    def set_value(self, frame:int, value:float, adjustLastKeyframe:bool=False):
        """
        Set the attribute's value as a double value at a given frame.

        Sets the value of the attribute to the provided double value at the given frame. If the attribute can be linked and has a column linked to it, the value is set on the column – otherwise, it is set on the localvalue of the attribute.

        Note
        If no column is present, setting an animateable column's value on the attribute will result in the creation of a new column.
        Parameters
        frame	- the frame at which the attribute is set.
        value	- the double value to which the attribute should be set.


        Set a Double Value at a Frame
        ```python
        import random
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Peg"]                                 #Find the Peg node.
        double_attribute_keyword = "POSITION.X"                       #The path to a double attribute
        attribute = node.attributes[double_attribute_keyword]         #Get the attribute by name
        if attribute:
        at_frame = 1
        current_value = attribute.value( at_frame )                #Get the attribute's value.
        #Show the current localvalue of the attribute.
        print( "CURRENT VALUE AT %s : %s"%( at_frame, current_value ) )
        new_value = random.uniform( attribute.minimum, attribute.maximum )
        attribute.set_value( at_frame, new_value )                                                      #Set the attribute's local value to the new value
        new_value = attribute.value( at_frame )                                                         #Get the attribute's new localvalue, to check it for debug/example purposes
        print( "NEW VALUE AT %s : %s"%( at_frame, new_value ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(double_attribute_keyword) )
        ```
        """
        return
    
    def offset_value(self, frameOrRange, value:float):
        """
        Offsets the attribute's value at a given frame or frame range.

        Provided a double object, will offset the existing value (either the animated value, or local value if none exists) by the double.

        Parameters
        frameOrRange	- A frame range provided by a list in form [startFrame, endFrame]
        value	- The double object to by which the attribute is offset.

        Offset a Double Attribute
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Peg"]                                 #Find the Peg node.
        double_attribute_keyword = "POSITION.X"                       #The path to a double attribute
        attribute = node.attributes[double_attribute_keyword]         #Get the attribute by name
        if attribute:
        at_frame = 1
        current_value = attribute.value( at_frame )                #Get the attribute's value.
        #Show the current localvalue of the attribute.
        print( "CURRENT VALUE AT %s : %s"%( at_frame, current_value ) )
        new_value = random.uniform( attribute.minimum - current_value, attribute.maximum - current_value  )
        range = [ at_frame, scene.frame_count ]                    #The range will be from at_frame, to the last frame of the scene.
        attribute.offset_value( range, new_value )                 #Offset the attribute's value by the provided value
        new_value = attribute.value( at_frame )                    #Get the attribute's new localvalue, to check it for debug/example purposes
        print( "NEW VALUE AT %s : %s"%( at_frame, new_value ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(double_attribute_keyword) )
        ```
        """
        return
       
    def reset_localvalue(self):
        """
        Reset the attribute's localvalue to the default value.

        The value of an attribute has a default value when the node is initially created. This method will reset the localvalue to its initial default value.
        """
        return
    
    def reset_value(self):
        """
        Sets the attribute's local value as a double value.

        Sets the local value of the attribute to the provided double value. The local value is the non-animateable value of an attribute when no column is present. If the attribute can be linked and has a column linked to it, the value at a frame is provided by the column and the local value is ignored.

        Note
        Its generally better to reference the value over the localvalue. When no column is present, the value will also provide the localvalue – this is not true in reverse, if a column is present, the localvalue will still reference the ignored localvalue. Non-animateable attributes that cannot be linked will only provide the localvalue.
        Parameters
        value	- the double value to which the attribute should be set.


        Set a OMC::Color Localvalue
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        import random
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Peg"]                                 #Find the Peg node.
        double_attribute_keyword = "POSITION.X"                       #The path to a double attribute
        attribute = node.attributes[double_attribute_keyword]         #Get the attribute by name
        if attribute:
        current_value = attribute.localvalue()                     #Get the attribute's localvalue.
        #Show the current localvalue of the attribute.
        print( "CURRENT LOCALVALUE: %s"%( current_value ) )
        new_value = random.uniform( attribute.minimum, attribute.maximum )
        attribute.set_localvalue( new_value )                      #Set the attribute's local value to the new value
        new_value = attribute.localvalue()                         #Get the attribute's new localvalue, to check it for debug/example purposes
        print( "NEW LOCALVALUE: %s"%( new_value ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(double_attribute_keyword) )
        ```
        """
        return
    
    @property
    def minimum(self) -> float:
        """
        Get the minimum value of the attribute.

        Double attributes can have a minimum value that the attribute can provide. This minimum value is provided from the minimum property.
        """
        return 1.0
        
    @property
    def maximum(self) -> float:
        """
        Get the max value of the attribute.

        Double attributes can have a maximum value that the attribute can provide. This maximum value is provided from the maximum property.
        """
        return 1.0
        
    @property
    def step(self) -> float:
        """
        Get the incremental step-value of the attribute.

        In the layer properties panel of the GUI, the attribute will increment at the step-rate provided by this property.
        """
        return 1.0
        
    @property
    def default(self) -> float:
        """
        Get the default value of the attribute.

        Provides the default value of the attribute – this is the value that the attribute will use when it is reset.
        """
        return 1.0

class DrawingAttribute(Attribute):
    """
    The attribute wrapper.

    This object wraps a single attribute owned by a node. The Drawing attribute provides generic representation for either an Element Attribute when in Element Mode or a Timing Attribute otherwise.

    When in Element Mode (OMC::DrawingAttribute::element_mode == True), the drawing is provided by an element object and is sourced from a folder on disk within the project's element folder.
    The Element Attribute uses the attached column (OMC::ElementColumn) to provide an element ID and the timing for the drawings. The Element that is linked to the ElementColumn will provide a list of element drawings sourced from the element's folder. The OMC::ElementColumn then provides the timing of this Element's drawings (OMC::ElementDrawing).
    See OMC::ElementAttribute, OMC::ElementColumn, OMC::Element and OMC::ElementDrawing for more information.

    When in Timing Mode (OMC::DrawingAttribute::element_mode == Frue), the drawing is provided by a TimingAttribute that provides a location, size, suffix and timing for content sourced externally from the project. This content is not sourced from the project's elements folder, and the timing is used to simply target a different source elsewhere or disk.
    """
    def __init__(self):
        super().__init__()
    
    def value(self, frame:int) -> float:
        """
        Get the attribute's value.

        Get the attribute's value as a string representing a drawing's name at a given frame.

        Provides the value as a string that represents a drawing's name at a given frame.


        Retrieve a Drawing Name at a Frame
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Drawing"]                            #Find the Drawing node.
        drawing_attribute_keyword = "DRAWING"                        #The path to a double attribute
        attribute = node.attributes[drawing_attribute_keyword]       #Get the attribute by name
        if attribute:
        at_frame = 1
        current_value = attribute.value(at_frame)                       #Get the attribute's value at frame 1
        #Show the value of the attribute.
        print( "VALUE AT FRAME %s : %s"%( at_frame, current_value ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(drawing_attribute_keyword) )
        ```
        """
        return 1.0
    
    def set_localvalue(self, value):
        """
        Set the attribute's local value.

        The Drawing Attribute does not provide a local value – this method only exists as a macro for OMC::DrawingAttribute::set_value( 1, value )

        Parameters
            value	- the OMC::ElementDrawing or drawing name to which the attribute should be set at frame 1.
        """
        return
    
    def set_value(self, frame:int, drawing):
        """
        Set the attribute's value as a drawing value at a given frame.

        Sets the value of the attribute to the provided drawing value at the given frame.

        Parameters
            frame	- the frame at which the attribute is set.
            value	- the OMC::ElementDrawing or drawing name to which the attribute should be set.


        Set a Drawing Value at a Frame
        ```python
        import random
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Drawing"]                            #Find the Drawing node.
        drawing_attribute_keyword = "DRAWING"                        #The path to a double attribute
        attribute = node.attributes[drawing_attribute_keyword]       #Get the attribute by name
        if attribute:
        at_frame = 1
        current_value = attribute.value( at_frame )                #Get the attribute's value.
        #Show the current localvalue of the attribute.
        print( "CURRENT VALUE AT %s : %s"%( at_frame, current_value ) )
        element = attribute.element                                #The element associated with the drawing
        possible_drawings = element.drawings.list()                #Provides a list of available drawings for this element.
        new_value = random.choice( possible_drawings )
        attribute.set_value( at_frame, new_value )                                                      #Set the attribute's local value to the new value
        new_value = attribute.value( at_frame )                                                         #Get the attribute's new localvalue, to check it for debug/example purposes
        print( "NEW VALUE AT %s : %s"%( at_frame, new_value ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(drawing_attribute_keyword) )
        ```
        """
        return
    
    @property
    def drawing_type(self) -> str:
        """
        The drawing-type of the attribute.

        A read only property that provides the drawing-type as a string.
        """
        return ""
        
    @property
    def element_name(self) -> str:
        """
        The element name of the element connected to the attribute.

        The element associated with the DrawingAttribute (often provided via the OMC::Column attached to the attribute) has both a unique ID and a name. This element name is available either through the element property (OMC::DrawingAttribute::element::name) or with this property.

        List All Drawings Available
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Drawing"]                            #Find the Drawing node.
        drawing_attribute_keyword = "DRAWING"                        #The path to a double attribute
        attribute = node.attributes[drawing_attribute_keyword]       #Get the attribute by name
        if attribute:
        print( "Element Name : %s"%(attribute.element_name) )
        
        #Equivalent to . . . 
        element = attribute.element                                #The element associated with the drawing
        if element:
            print( "Element Name [from Object] : %s"%(element.name) )
        else:
        print( "Unable to find attribute by keyword: %s"%(drawing_attribute_keyword) )
        ```
        """
        return ""
        
    @property
    def timing_name(self) -> str:
        """
        The timing name of the drawing connected to the attribute.

        A read-only property that provides the timing name of the attribute. Different DrawingAttribute settings can result in different timing sources.
        """
        return ""
        
    @property
    def element_mode(self) -> bool:
        """
        Identifies whether this attribute is in element mode or not.

        When in Element Mode, the drawings will be sourced from the attached OMC::ElementColumn and its element ID. Otherwise, it is in timing mode and the drawings will be sourced from the attached OMC::TimingColumn and a reference elsewhere on disk.
        """
        return True
        
    @property
    def drawing(self) -> Attribute:
        """
        Provides either the element attribute or the custom-name attribute depending on the active mode.

        The drawing source can be provided from a different subattribute depending on the element attribute's mode. This property provides the corresponding attribute given the element's current settings.
        """
        return Attribute()
        
    @property
    def timing(self) -> Column:
        """
        Provides either the element attribute or the custom-name attribute depending on the active mode.

        The timing and exposure of the drawings can be provided from a different subattribute depending on the element attribute's mode. This property provides the corresponding attribute given the element's current settings.
        """
        return Column()

class DrawingTimingColumn(Column):
    """
    Represents and provides the methods for an timing column in a scene.

    The Timing column provides the timing for a DrawingAttribute (in Timing mode) or a TimingAttribute.
    """
    def __init__(self):
        super().__init__()
        
    def contains(self, drawing) -> bool:
        """Identifies if the list contains the drawing."""
        return True
    
    def drawing_duplicate(self, frameNumber:int):
        """
        Duplicates the drawing at the specified frame in the specified column.

        Parameters
            frame	: The frame number.
        """
        return
    
    def drawing_delete(self, frameNumber:int):
        """
        Deletes the drawing at the specified frame in the specified column.

        Parameters
            frame	: The frame number.
        """
        return
    
    def key_exposure_add(self, frameNumber:int):
        """
        Adds a key drawing exposure at the specified frame in the specified column.

        Parameters
            frameNumber	: The frame number.
        """
        return
    
    def key_exposure_remove(self, frameNumber:int):
        """
        Removes a key drawing exposure at the specified frame in the specified column.

        Parameters
            frameNumber	: The frame number.
            duplicateOnly	: If true, only remove duplicate/redundant key exposures.
        """
        return
    
    def fill_empty(self, startFrame:int, endFrame:int):
        """
        Fill with previous exposed drawings for the given range of frame.

        Parameters
            startFrame	: The starting frame.
            endFrame	: The ending frame, just after the last filled frame.
        """
        return
    
    def lineTestFill(self, startFrame:int, nbFrames:int, prefix:str, keyFramesOnly:bool):
        """
        Fills the drawings from startFrame to startFrame+nbFrames with drawing duplicates named with a prefix.

        Parameters
            startFrame	: The starting frame.
            nbFrames	: The desired length.
            prefix	: The desired prefix.
            keyFramesOnly	: It will perform this operation only on drawings marked as "K" if keyOnly is true.
        
        Returns
            Returns true if successful.
        """
        return

class EaseColumn(KeyframeableColumn):
    """
    A column providing an interpolated value from an easy curve defined by control points.

    Generate an Example Column
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    proj.history.begin( "Generating Test Column" )
    columns = scene.columns                                      #The overall node list of the scene.
    #Create the new Ease Column
    new_column = columns.create( "EASE", "NEW_EASE_COLUMN" )
    value_incremental = 0
    #Add a keyframe value every 10 frames.
    for frame in range(1,60)[::10]:
    print( "Setting Key Value at %s : %s"%(frame, value_incremental) )
    new_column[frame] = value_incremental
    value_incremental = value_incremental + 1
    proj.history.end()
    ```
    """
    def __init__(self):
        super().__init__()
    
    def create_point(self, frame:float, value:float, easeIn:float, angleEaseIn:float, easeOut:float, angleEaseOut:float, constSeg:bool, continuity:str):
        """
        Sets the values of a point on an Ease column.

        Parameters
            frame	: Frame number for the point.
            value	: Y value for the point.
            easeIn	: The number of frames in the ease-in.
            angleEaseIn	: The angle of the ease-in handle.
            easeOut	: The number of frames in the ease-out.
            angleEaseOut	: The angle of the ease-out handle.
            constSeg	: Boolean expression (with a true or false value) to indicate whether the segment is constant or interpolated.
            continuity	: String value for the continuity of the point. The string must be in all upper-case. The following are the acceptable values: STRAIGHT, SMOOTH and CORNER.
        """
        return
    
    @property
    def tension_ease(self) -> float:
        """The tension of the ease, 0 if the given column isn't an ease column."""
        return 1.0
    
    def __getitem__(self, idx:int):
        """
        The column object is is iterable and can provide values at given frames with the list operator. The frame value can be get and set from this interface.

        Print Column Values
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        columns = scene.columns                                      #The overall column list of the scene.
        bez_col = columns["EASE_COLUMN_NAME"]
        for n in range( 1, scene.frame_count ):
        print( "Value at %s : %s"%(n, bez_col[n].value ) )
        ```
        """
        return EaseColumnValue()

class EaseColumnValue(ColumnValue):
    def __init__(self):
        super().__init__()

    @property
    def key(self) -> bool:
        """True if the given frame is a keyframe."""
        return True
        
    @property
    def const_segment(self) -> bool:
        """Returns true to indicate that the point is on a constant segment, or false to indicate that the point is not on a constant segment."""
        return True
        
    @property
    def continuity(self) -> str:
        """Returns the continuity of the curve that follows the point. One of the following values will be returned, in upper-case: SMOOTH, CORNER or STRAIGHT."""
        return ""
        
    @property
    def ease_in(self) -> float:
        """Returns the number of frames in the ease-in."""
        return 1.0
        
    @property
    def ease_in_angle(self) -> float:
        """The angle of the ease-in handle."""
        return 1.0
        
    @property
    def ease_out(self) -> float:
        """The number of frames in the ease-out."""
        return 1.0
    
    @property
    def ease_out_angle(self) -> float:
        """The angle of the ease-out handle."""
        return 1.0
        
    @property
    def keyframe_previous(self):
        """The previous frame at which there is a keyframe present, this frame value object if its currently a keyframe."""
        return EaseColumnValue()
        
    @property
    def keyframe_next(self):
        """The next frame at which there is a keyframe present. If none are present, returns none."""
        return EaseColumnValue()
    
class EaseControlPoint(ControlPoint):
    """
    An object that represents the control point of ease column.

    Provided by OMC::EaseColumn::control_points. Provides the keyframes and keyframe options associated with a keyframeable bezier column.
    Look Through Ease Keyframes

    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    columns = scene.columns                                      #The overall column list of the scene.
    ease_col = columns["EASE_COLUMN_NAME"]
    keyframes = ease_col.control_points                          #This list provides EaseControlPoint objects.
    for keyframe in keyframes:
    print( "Key At: %s %s"%( keyframe.frame, keyframe.value )  )
    ```
    """
    def __init__(self):
        super().__init__()
    
    @property
    def const_segment(self) -> bool:
        """True to indicate that the point is on a constant segment, or false to indicate that the point is not on a constant segment."""
        return True
        
    @property
    def continuity(self) -> str:
        """The continuity of the curve that follows the point. One of the following values will be returned, in upper-case: CORNER or STRAIGHT."""
        return ""
        
    @property
    def ease_in(self) -> float:
        """The number of frames in the ease-in."""
        return 1.0
        
    @property
    def ease_in_angle(self) -> float:
        """The angle of the ease-in handle."""
        return 1.0
        
    @property
    def ease_out(self) -> float:
        """The number of frames in the ease-out."""
        return 1.0
        
    @property
    def ease_out_angle(self) -> float:
        """The angle of the east-out handle."""
        return 1.0
    
class Element(BaseObject):
    """
    Provides the methods and properties for an Element.

    An Element is a collection of ElementDrawing objects that are managed and sourced on disk relative to the project. The element's are referred to by their ID and name, and are linked to an ElementAttribute with a ElementColumn. The ElementColumn provides the exposure and order of the drawings when used in an ElementAttribute.

    All elements are owned by the project and are provided by the ElementList in the project's elements attribute (See OMH::HarmonyProject::elements).

    List All Elements in a Project
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    elems = proj.elements                                        #The element list of all elements in the project.
    print( "Element Count: %s"%(len(elems)) )
    for elem in elems:                                           #Expectation: All names of all scenes in the project printed.
    print( "Element Name: %s"%(elem.name) )
    ```

    Create a New Element with Some Drawings
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    elems = proj.elements                                        #The element list of all elements in the project.
    #Create the new Element
    new_element = elems.create( "NEW_ELEMENT_NAME", "COLOR", 12.0, "SCAN", "TVG"  )
    #Create some new drawings.
    new_drawing1 = new_element.drawings.create( "DRAWING_NAME_001", False, True )
    new_drawing2 = new_element.drawings.create( "DRAWING_NAME_002", False, True )
    new_drawing3 = new_element.drawings.create( "DRAWING_NAME_003", False, True )
    ```
    """
    def __init__(self):
        super().__init__()
    
    def lock(self):
        """Get the lock on the database."""
        return
    
    def release(self):
        """Release the lock on the database."""
        return
    
    def duplicate(self, elementName:str):
        """Duplicate the element."""
        return Element()
    
    @property
    def id(self) -> int:
        """Provides the id of the element in the project."""
        return 1
        
    @property
    def name(self) -> str:
        """Provides the name of the element in the project."""
        return ""
        
    @property
    def scan_type(self):
        """Provides and sets the scan type of the element in the project."""
        return
        
    @property
    def field_chart(self) -> float:
        """Provides the fieldchart of the element in the project."""
        return 1.0
        
    @property
    def vector_type(self) -> str:
        """
        Provides the vector type of the element in the project.

        This provides the vector type for the given element. For standard vector or Toon Boom bitmap drawing, the vector type will be TVG.
        """
        return ""
        
    @property
    def pixmap_format(self) -> str:
        """Provides the pixmap format for the provided element ID."""
        return ""
        
    @property
    def folder(self) -> str:
        """
        Provides the actual element folder.

        This is normally the element name (unless it has been renamed and the project is not saved) but may include the ".<element id>" in the name if multiple elements share the same name.
        """
        return ""
        
    @property
    def folder_complete(self) -> str:
        """
        Provides the complete element folder.

        This is normally the element name (unless it has been renamed and the project is not saved) but may include the ".<element id>" in the name if multiple elements share the same name.
        """
        return ""
        
    @property
    def drawings(self):
        """Provides the list of drawings contained in the element."""
        return ElementDrawingList()
        
    @property
    def physical_name(self) -> str:
        """
        Provide the actual name of the drawings.

        This is different that the element name if this one has been renamed and the changes have not yet been saved.
        """
        return ""
        
    @property
    def locked(self) -> bool:
        """Whether the element is currently locally locked by the session, and can be modified."""
        return True
        
    @property
    def temp_directory_located(self) -> bool:
        """Whether the element is currently located in the temp directory."""
        return True
        
    @property
    def deleted(self) -> bool:
        """Whether the element is deleted."""
        return True
        
    @property
    def linked(self) -> bool:
        """Whether the element is linked to a column."""
        return True
    
class ElementAttribute(Attribute):
    """
    The element attribute wrapper.

    This object wraps an element attribute – often provided by a DrawingAttribute when in element mode.

    When a DrawingAttribute is in in Element Mode (OMC::DrawingAttribute::element_mode == True), the drawing attribute receives its values from the underlying ElementAttribute.
    The element attribute provides drawings based on an attached column (OMC::ElementColumn) that provides an element ID and the timing for the drawings. The Element that is linked to the ElementColumn will provide a list of element drawings sourced from its folder. The OMC::ElementColumn then provides the timing of this Element's drawings (OMC::ElementDrawing).

    See OMC::ElementColumn, OMC::Element and OMC::ElementDrawing for more information.
    """
    def __init__(self):
        super().__init__()
    
    def value(self, frame:int) -> str:
        """Get the attribute's value at a given frame."""
        return ""
    
    def setValue(self, frame:int, value):
        """
        Get the attribute's value.

        Get the attribute's value at a given frame
        """
        return
    
    @property
    def element(self) -> Element:
        """Provides the element connected to the attribute."""
        return Element()
        
    @property
    def element_name(self) -> str:
        """The element name of the element connected to the attribute."""
        return ""

class ElementColumn(Column):
    """
    Represents and provides the methods for an element column in a scene.

    The Element column provides the timing and element ID for an ElementAttribute or DrawingAttribute. This element column is linked to an Element id, which sources its drawings from storage local to the scene. The column also provides a timing of these ElementDrawings, in order to expose certain ElementDrawings at certain times.
    """
    def __init__(self):
        super().__init__()
    
    def attach_new_element(self, name:str, scanType:str, fieldChart:float, fileFormat:str, vectorFormat:str) -> Element:
        """
        Insert and attach an element to the drawing column.

        Adds an element to the project, and attaches the element id to the column, overriding any other element that may already be assigned to it.
        """
        return Element()
    
    def drawing_duplicate(self, frameNumber:int):
        """
        Duplicates the drawing at the specified frame in the specified column.

        Parameters
            frameNumber	The frame number.
        """
        return
    
    def drawing_delete(self, framerange:int):
        """
        Deletes the drawing at the specified frame in the specified column.

        Parameters
            framerange	: The frame number or list of frames or a map of properties If a frame maps is provided, 2 properties from each of the following list must be provided: start frame list: "from", "start", "begin", "FROM", "START", "BEGIN" end frame list: "to", "end", "finish", "TO", "END", "FINISH"
        """
        return
    
    def drawing(self, atFrame:float):
        """
        Returns the element drawing object at the given frame.

        Parameters
            atFrame	: The frame number.
        
        Returns
            Returns the element drawing object at the given frame.
        """
        return ElementDrawing()
    
    def drawing_type(self) -> str:
        """
        Returns the drawing type in the drawing column at the given frame. K = key drawings, I = inbetween, B = breakdown
        Parameters
            atFrame	: The frame number.
        
        Returns
            Returns the drawing type in the drawing column at the given frame.
        """
        return ""
    
    def set_drawing_type(self, atFrame:int, drawingType:str):
        """
        Sets the drawing type at the given frame.

        K = key drawings, I = inbetween, B = breakdown

        Parameters
            atFrame	: The frame number.
            drawingType	: K = key drawings, I = inbetween, B = breakdown.
        """
        return
    
    def key_exposure_next(self, startFrame:float, flags) -> float:
        """
        Returns the next key drawing in a drawing column.

        Parameters
            startFrame	: The frame number that specifies the search start point.
            flags	: The flags to filter for when searching for the next exposure.
        
        Returns
            Returns the starting frame of the next key drawing in a drawing column.
        """
        return 1.0
    
    def key_exposure_add(self, frame:int):
        """
        Adds a key drawing exposure at the specified frame in the specified column.

        Parameters
            frame	: The frame number.
        """
        return
    
    def key_exposure_remove(self, frame:int):
        """
        Removes a key drawing exposure at the specified frame in the specified column.

        Parameters
            frame	: The frame number.
        """
        return
    
    def key_exposure_remove_duplicate(self, frameNumber:int):
        """
        Removes duplicate key drawing exposure at the specified frame in the specified column.

        Parameters
            frameNumber	: The frame number.
        """
        return
    
    def fill_empty(self, startFrame:int, endFrame:int):
        """
        Fill with previous exposed drawings for the given range of frame.

        Parameters
            startFrame	: The starting frame.
            endFrame	: The ending frame, just after the last filled frame.
        """
        return
    
    def drawing_version(self, name:str) -> int:
        """Get the version of the drawing being used in the drawing column."""
        return 1

    def __getitem__(self, idx:int):
        """
        The column object is is iterable and can provide values at given frames with the list operator. The frame value can be get and set from this interface.

        Print Column Values
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        columns = scene.columns                                      #The overall column list of the scene.
        bez_col = columns["ELEMENT_COLUMN_NAME"]
        for n in range( 1, scene.frame_count ):
        print( "Value at %s : %s"%(n, bez_col[n].name ) )
        ```
        """
        return ElementDrawing()
    
    @property
    def drawings(self):
        """Get the list of drawings belonging to the drawing column and its element."""
        return ElementDrawingList()

    @property
    def drawing_names(self) -> List[str]:
        """Get the list of drawing names belonging to the drawing column and its element."""
        return [""]
    
    @property
    def element(self) -> Element:
        """Get/set the element attached to the drawing column."""
        return Element()
    
class ElementDrawing(BaseObject):
    """
    Represents a drawing belonging to an element.

    Provides the methods needed to manipulate a drawing that is managed by an Element. These are the underlying drawings available to the element, and may contain more drawings that those that are exposed on the timeline.

    List All Drawings in All Elements
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    elems = proj.elements                                        #The element list of all elements in the project.
    print( "Element Count: %s"%(len(elems)) )
    for elem in elems:                                           #Expectation: All names of all scenes in the project printed.
    print( "Element Name: %s"%(elem.name) )
    element_drawings = elem.drawings
    print( "   Contains %s Drawings : "%(len(element_drawings)) )
    for element_drawing in element_drawings:
        print( "   %s"%(element_drawing.name) )
    ```

    Create a New Element with A Drawing
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    elems = proj.elements                                        #The element list of all elements in the project.
    #Create the new Element
    new_element = elems.create( "NEW_ELEMENT_NAME", "COLOR", 12.0, "SCAN", "TVG"  )
    print( "New Element Created: %s"%(new_element.id) )
    #Create a new drawing.
    new_drawing = new_element.drawings.create( "DRAWING_NAME_001", False, True )
    print( "New Drawing Created: %s"%(new_drawing.name) )
    ```
    """
    def __init__(self):
        super().__init__()
    
    def duplicate(self, newName:str, layer:str):
        """Duplicate the drawing and provide the new drawing in return."""
        return ElementDrawing()
    
    @property
    def id(self) -> str:
        """Provides the unique drawing id (same as OMC::ElementDrawing::name)."""
        return ""
        
    @property
    def name(self) -> str:
        """Provides the unique drawing name."""
        return ""
        
    @property
    def path(self) -> str:
        """Provides the path to the drawing."""
        return ""
        
    @property
    def deleted(self) -> bool:
        """Identifies if the drawing has been deleted."""
        return True
        
    @property
    def file_exists(self) -> bool:
        """Identifies if the drawing file exists."""
        return True
        
    @property
    def used(self) -> bool:
        """Identifies if the drawing is being used."""
        return True
        
    @property
    def element(self) -> Element:
        """Get the parent element that owns this drawing."""
        return Element()
        
    @property
    def type(self) -> str:
        """Identifies the drawing-type."""
        return ""
        
    @property
    def scale_factor(self) -> float:
        """Get/set the drawing scale factor."""
        return 1.0
        
    @property
    def version(self) -> int:
        """Get/set the drawing version."""
        return 1

class ElementDrawingList(ListObj, IterableObj):
    """
    Provides a list of ElementDrawings provided from a Element.

    An Element provides managed drawings from a source relative to the project. The ElementDrawingList provides the list of drawings that the given Element manages and provides. This list is also used to create, manage and remove the ElementDrawings from the Element.

    The ElementDrawingList is provided from OMC::Element::drawings.

    List All Drawings in All Elements
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    elems = proj.elements                                        #The element list of all elements in the project.
    print( "Element Count: %s"%(len(elems)) )
    for elem in elems:                                           #Expectation: All names of all scenes in the project printed.
    print( "Element Name: %s"%(elem.name) )
    element_drawings = elem.drawings
    print( "   Contains %s Drawings : "%(len(element_drawings)) )
    for element_drawing in element_drawings:
        print( "   %s"%(element_drawing.name) )
    ```

    Add and Remove an Element Drawing
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    elems = proj.elements                                        #The element list of all elements in the project.
    #Create the new Element
    new_element = elems.create( "NEW_ELEMENT_NAME", "COLOR", 12.0, "SCAN", "TVG"  )
    print( "New Element Created: %s"%(new_element.id) )
    #Create a new drawing.
    new_drawing = new_element.drawings.create( "DRAWING_NAME_001", False, True )
    print( "New Drawing Created: %s"%(new_drawing.name) )
    #Remove the new drawing.
    try:
    new_element.drawings.remove( new_drawing )
    print( "Successfully remove the drawing." )
    except:
    print( "Failed to remove the drawing." )
    ```
    """
    def __init__(self):
        super().__init__()
    
    def contains(self, name:str) -> bool:
        """Identifies if the list contains the attribute (or subattribute)."""
        return True
    
    def list(self) -> List[ElementDrawing]:
        """Converts the dynamic list into a concrete list of attribute objects."""
        return [ElementDrawing()]
    
    def create(self, name:str, fileExists:bool, storeInProjectFolder:bool=False) -> ElementDrawing:
        """
        Creates a new drawing inside an element.

        Create a new empty drawing inside the given element. The drawing file will physically exists in the temporary folder until the project is saved. Then, the file will reside in (scene folder)/elements/MyElement/ (where MyElement is the name of the element linked to the given elementId).

        Parameters
            name	The proposed drawing name.
            fileExists	Used to indicate that the drawing exists. By default, drawings exist in the temporary folder.
            storeInProjectFolder	Indicate that the drawing exits in the project folder, not in a temporary folder.
        
        Returns
            Returns the new drawing object that was created.
        """
        return ElementDrawing()
    
    def remove(self, drawing):
        """
        Removes an element drawing by its name/id.

        Returns
            Returns true if successfully removed.
        """
        return
    
    def __getitem__(self, idx:int) -> ElementDrawing:
        """
        Provides the ElementDrawing in the Element at the given index.

        Returns
            The OMC::ElementDrawing corresponding to the given index.
        
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        elems = proj.elements                                        #The element list of all elements in the project.
        print( "Element Count: %s"%(len(elems)) )
        for elem in elems:                                           #Expectation: All names of all scenes in the project printed.
        print( "Element Name: %s"%(elem.name) )
        element_drawings = elem.drawings                                  #The ElementDrawingList
        print( "   Contains %s Drawings : "%(len(element_drawings)) )     #Identifying the size of the list with len( list )
        for index in range(element_drawings):
            print( "   %s"%(element_drawings[index].name) )
        ```
        """
        return ElementDrawing

class ElementList(ListObj, IterableObj):
    """Provides a list of elements that are owned by the scene."""
    def __init__(self):
        super().__init__()
    
    def create(self, name:str, scanType:str, fieldChart:float, pixelFormat:str, vectorFormat:str) -> Element:
        """
        Creates a new element.

        Returns the newly added element if successful, otherwise null.
        """
        return Element()

class EnumAttribute(Attribute):
    """
    The enumerated attribute wrapper.

    This object wraps an attribute that provides a value from a pulldown list containing a enumerated list of available options. This is a non-animateable attribute, and the value of the attribute must be an option from within the list of options that the attribute supports.

    Show and Choose an Option from an EnumAttribute
    ```python
    import random
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    node = scene.nodes["Top/Drawing"]                            #Find the Drawing node.
    drawing_attribute_keyword = "USE_DRAWING_PIVOT"              #The path to an enum attribute [A Read Node's Drawing Pivot Setting]
    attribute = node.attributes[drawing_attribute_keyword]       #Get the attribute by name
    if attribute:
    options = attribute.options                                #Get Available options, which is a list of option types
    
    print( "Attribute Provides %s Options"%(len(options)) )   
    for option in options:                                     #Print available options.
        print( "Option: %s"%(option.name) )
    new_choice = random.choice( options )
    attribute.set_value( 1, new_choice )                       #Set the enum attribute to the random choice from available options.
    
    print( "Selected Option: %s"%(new_choice.name) )
    else:
    print( "Unable to find attribute by keyword: %s"%(drawing_attribute_keyword) )
    ```
    """
    def __init__(self):
        super().__init__()
    
    def localvalue(self):
        """
        Get the attribute's localvalue as a OMC::EnumAttributeOption value.

        Provides the localvalue as a OMC::EnumAttributeOption value. The local value is the non-animateable value of an attribute when no column is present. The Enum Attribute cannot be animated, and the localvalue and value at any frame should always be the same.

        Retrieve a OMC::EnumAttributeOption Localvalue
        ```python
        import random
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Drawing"]                            #Find the Drawing node.
        drawing_attribute_keyword = "USE_DRAWING_PIVOT"              #The path to an enum attribute [A Read Node's Drawing Pivot Setting]
        attribute = node.attributes[drawing_attribute_keyword]       #Get the attribute by name
        if attribute:
        value = attribute.localvalue()                             #The local value of the attribute, as an EnumAttributeOption
        
        #The human readable name, and the underlying value of the option.
        print( "Current Option: %s - %s"%(value.name, value.value) )
        
        value = attribute.value( 1 )                               #The local value and the value are the same, as its not animateable.
        print( "Current Option: %s - %s"%(value.name, value.value) )
        else:
        print( "Unable to find attribute by keyword: %s"%(drawing_attribute_keyword) )
        ```
        """
        return EnumAttributeOption()
    
    def set_localvalue(self, value):
        """
        Sets the attribute's local value as a OMC::EnumAttributeOption value.

        Sets the local value of the attribute to the provided OMC::EnumAttributeOption value. The value can either be the EnumAttributeOption directly, its name or its value.

        Parameters
            value	- the OMC::EnumAttributeOption value to which the attribute should be set.


        Show and Choose an Option from an EnumAttribute
        ```python
        import random
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Drawing"]                            #Find the Drawing node.
        drawing_attribute_keyword = "USE_DRAWING_PIVOT"              #The path to an enum attribute [A Read Node's Drawing Pivot Setting]
        attribute = node.attributes[drawing_attribute_keyword]       #Get the attribute by name
        if attribute:
        options = attribute.options                                #Get Available options, which is a list of option types
        print( "Attribute Provides %s Options"%(len(options)) )
        for option in options:                                     #Print available options.
            print( "Option: %s"%(option.name) )
        new_choice = random.choice( options )
        attribute.set_localvalue( 1, new_choice )                  #Set the enum attribute to the random choice from available options.
        print( "Selected Option: %s"%(new_choice.name) )
        else:
        print( "Unable to find attribute by keyword: %s"%(drawing_attribute_keyword) )
        ```
        """
        return
    
    def value(self, frame:int):
        """
        Get the attribute's value at a given frame.

        The OMC::EnumAttribute is not animateable, as such, this is equivalent to OMC::EnumAttribute::localvalue(). The method is available for consistency with other attribute types that can be animateable.

        See OMC::EnumAttribute::localValue for more information.

        Parameters
            frame	- this argument is ignored.
        """
        return EnumAttributeOption()
    
    def set_value(self, frame:int, value):
        """
        Set the attribute's value as a OMC::EnumAttributeOption at a given frame.

        The OMC::EnumAttribute is not animateable, as such, this is equivalent to OMC::EnumAttribute::set_localvalue( value ). The method is available for consistency with other attribute types that can be animateable.

        See set_localvalue( value ) for more information.

        Parameters
            frame	- this argument is ignored.
            value	- the OMC::EnumAttributeOption to which the attribute will be set.
        """
        return
    
    @property
    def options(self):
        """
        Get the available options of the enum attribute.

        The Enum Attribute only supports its available options. The options property will provide all available OMC::EnumAttributeOption objects that this attribute will support.

        Show Available Options
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Drawing"]                            #Find the Drawing node.
        drawing_attribute_keyword = "USE_DRAWING_PIVOT"              #The path to an enum attribute [A Read Node's Drawing Pivot Setting]
        attribute = node.attributes[drawing_attribute_keyword]       #Get the attribute by name
        if attribute:
        options = attribute.options                                #Get Available options, which is a list of option types
        
        print( "Attribute Provides %s Options"%(len(options)) )   
        for option in options:                                     #Print available options.
            print( "Option: %s"%(option.name) )
        else:
        print( "Unable to find attribute by keyword: %s"%(drawing_attribute_keyword) )
        ```
        """
        return [EnumAttributeOption()]
    
class EnumAttributeOption(BaseObject):
    """
    An option for the OMC::EnumAttribute attribute.

    This object wraps an option available in an OMC::EnumAttribute. These options are available as the value of an EnumAttribute, or as available options with OMC::EnumAttribute::options.

    See OMC::EnumAttribute for more information.
    """
    def __init__(self):
        super().__init__()
    
    @property
    def name(self) -> str:
        """Get the name of the enum option."""
        return ""
        
    @property
    def value(self) -> str:
        """Get the value of the enum option."""
        return ""
    
class ExpressionColumn(Column):
    """
    Represents and provides the methods for an expression column in a scene.

    An Expression Column provides a double value based on a javascript expression set on the column. This expression column can provide dynamic values based on other variables in the project.
    
    Create an Expression Column

    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    columns = scene.columns                                      #The overall column list of the scene.
    new_expr_col = columns.create( "EXPR", "EXPR_COL_NAME" )     #Create the expression column
    #A multiline expression -- in this case, a self-referential fibonacci sequence.
    expr = \"""
            function fibonacci( frame )
            {
                if( frame < 1 )
                    return 0;
                else if( frame == 1 )
                    return 1;
                return value( "%s", frame-2 ) + value( "%s", frame-1 );
            }
            fibonacci( currentFrame );
        \"""%( new_expr_col.name, new_expr_col.name )
    new_expr_col.text = expr
    #The first 10 frames of the fibonacci sequence
    for frame in range( 1, 10+1 ):
    print( "Frame %s: %s"%(frame, new_expr_col[frame] ) )
    ```
    """
    def __init__(self):
        super().__init__()

    @property
    def text(self) -> str:
        """Get/set the expression text in the identified column."""
        return ""

class FlatCable(BaseObject):
    """
    Represents a flat-cable that is agnostic of any waypoints or groups. Read-only.

    The flat-cable is a connection that does not consider groups or waypoints. It can be followed to and from each real node, without having to enter or exist groups.
    See OMC::Cable for more information.
    """
    def __init__(self):
        super().__init__()
    
    @property
    def source(self):
        """Get the source port from which this cable is connected."""
        return OutPort()

    @property
    def source_node(self) -> Node:
        """Get the source node from which this cable is connected."""
        return Node()

    @property
    def destination(self):
        """Get the destination port to which this cable is connected."""
        return InPort()

    @property
    def destination_node(self) -> Node:
        """Get the destination node to which this cable is connected."""
        return Node()

class FlatCableList(ListObj, IterableObj):
    """
    Represents a flattened cables connecting nodes in the node view, ignoring all groups and waypoints.

    A flat cable will automatically traverse through groups, and is useful when wanting to traverse the network without having any special logic for groups or multiports.
    This is provided from OutPort::cables_flat

    Note
    Flat cables are read only and cannot be modified. The corresponding (unflattened) cables need to be modified instead.

    List FlatCables Attached to a Node's Port
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    peg = scene.nodes["Top/Peg"]                                 #Find the peg node.
    out_port = peg.ports_out[0]                                  #The first Out Port of a node.
    cablelist_flat = out_port.cables_flat
    print( "Number of Flat Cables : %s"%len( cablelist_flat ) )            #Print the amount of cables attached to the port.
    for idx,cable in enumerate(cablelist_flat):
    print( "Flat Cable %s : %s"%(idx, cable.destination_node.path) )     #Print what the cable is connected to.
    ```
    """
    def __init__(self):
        super().__init__()
    
    def contains(self, Cable) -> bool:
        """Identifies if the list contains the cable."""
        return True
    
    def list(self) -> List[FlatCable]:
        """Converts the dynamic list into a concrete list of FlatCable objects."""
        return [FlatCable()]
    
    def __getitem__(self, idx:int) -> Cable:
        """Provides the cable at the given index."""
        return Cable()


class FrameOptions():
    """
    Frame options for when inserting and removing frames.

    See OMC::Scene::frame_insert() for more information.
    """
    def __init__(self, ripple_markers:bool=False, extend_exposure:bool=False):
        super().__init__()
        self.ripple_markers = ripple_markers
        self.extend_exposure = extend_exposure

class GroupNode(Node):
    """
    Represents and provides the methods for a group node.

    The group node behaves as a standard node, but also contains nodes internal to it. OMC::GroupNode::nodes provides node list access to its internal nodes. The scene itself contains a top-level group-node named 'Top', and is accessible from the OMC::Scene::top property.

    Identify All Nodes in the 'Top' group of the scene.
    ```python
    import json
    import time
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    nodes = scene.top.nodes                                      #The node list of the nodes contained within the 'Top' group.
    for node in nodes:
    print( "Node: %s (%s)"%(node.path, node.type) )
    #Note -- this list will identify all nodes directly within the group, and does not consider the contents recursively.
    #The node list will not show nodes contained within other groups interior to itself; to do this, a recursive approach should be considered.
    print( "\nNow -- Recursively . . ." )
    #Here is a recursive approach, a function that will do the work for us. . .
    def recursively_detail_group(group, depth):
    for node in group.nodes:                                         #Look through all if this group's contents.
        print( "%sNode: %s (%s)"%("   "*depth, node.path, node.type) ) #Print Information
        if node.type.upper() == "GROUP":                               #If its a group type, we recursive even further.
        recursively_detail_group( node, depth+1 )                    #Calling this same function will dive deeper into the next group.
    recursively_detail_group(scene.top, 0)                             #Start diving into the groups!
    ```
    """
    def __init__(self):
        super().__init__()
    
    def explode(self) -> list:
        """
        Explode a group into its parent group. This method is identical to the "Explode Selected Group" from the node view.

        Returns
            Returns the list of nodes that were removed from the group.
        
        Explode a Group
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene
        node = scene.nodes["Top/Group"]
        if node:
        exploded_nodes = node.explode()                            #Explode those nodes!
        for node in exploded_nodes:
            print( "New Node: %s"%(node.path) )
        ```
        """
        return []
    
    def parent_scene(self):
        """
        Getaaa the parent scene for the node.

        Every node belongs within a scene, this method provides the scene (OMC::Scene, or OMH::Scene) object to which this node belongs.

        Identify the Scene of the Current Node
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        nodes = scene.nodes                                          #Get the node list of the scene.
        try:
        first_node = nodes[0]                                      #Just using the first node as an example.
        except:
        first_node = False
        node_scene = first_node.parent_scene()                       #In this case, redundant as we already have the scene owner above.4
        print( "Same Scene: %s"%( node_scene == scene ) )            #Expectation: "Same Scene: True"
        ```
        """
        return Scene()
    
    def parent_group(self):
        """
        Gets the parent group for the node.

        Retrieves the group-object in which this node belong (OMC::GroupNode). Every node belongs within a group – even the top-level nodes belong to a transparent group named 'Top'. The 'Top' group node behaves in the same manner as any other group, but is not visible within the node view (See OMC::Scene::top).

        Identify the Group of a Random Node in the Scene
        ```python
        import random
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        nodes = scene.nodes                                          #Get the node list of the scene.
        try:
        random_node = nodes[random.randint(0,len(nodes))]          #Get a random node, and find its parent group.
        except:
        random_node = False
        node_group = random_node.parent_group()                      #In this case, redundant as we already have the scene owner above.4
        print( "Parent Group: %s"%(node_group) )
        ```
        """
        return GroupNode()
    
    def move_to(self, groupPath:str, x:int=0, y:int=0):
        """
        [1/2] - groupPath (str) + x + y

        Moves the node into a group.

        Similar to OMC::NodeList::move, moves this node from one group to another based on the provided group path – but the OMC::Node connection is maintained. Fails with an error if the move fails.
        
        Parameters
            groupPath	- The path to the group into which this node will be placed.
            x	- The x coordinate of the node in the node view.
            y	- The y coordinate of the node in the node view.
        
        Move a Group Node into the Top Scene Group
        ```python
        import random
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        nodes = scene.nodes                                          #Get the node list of the scene.
        original_node = nodes["Top/Group1/Node"]                     #Get a node by name.
        original_node.move_to( "Top" )                               #Move the node to the new path.
        print( "New Node Path: %s"%(original_node.path) )            #Print the new path for the node.
        ```
        ------------------------------------------------------------------------
        [2/2] - groupPath (GroupNode) + x + y

        Moves the node into a group.

        Similar to OMC::NodeList::move, moves this node from one group to another based on the provided group object (OMC::GroupNode) – but the OMC::Node connection is maintained. Fails with an error if the move fails.
        
        Parameters
            groupPath	- The path to the group into which this node will be placed.
            x	- The x coordinate of the node in the node view.
            y	- The y coordinate of the node in the node view.
        
        Move a Group Node into the Top Scene Group
        ```python
        import random
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        nodes = scene.nodes                                          #Get the node list of the scene.
        original_node = nodes["Top/Group1/Node"]                     #Get a node by name.
        original_node.move_to( scene.top )                           #Move the node to the new path.
        print( "New Node Path: %s"%(original_node.path) )            #Print the new path for the node.
        ```
        """
        return
    
    @property
    def multi_port_in(self) -> Node:
        """
        Returns existing or add a group multi port in node.

        Adds a multi port in node inside the group if one doesn't already exist. If there is already such type of node in the group, it will return it. NULL if it cannot add such node. You cannot add this type of node in the top group of a scene and there can only be a single such node per group.

        Create a New Group, Add a Multi Port In
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene
        nodes = scene.nodes
        proj.history.begin( "Colour Card in Group" )
        new_group = nodes.create( "GROUP", "GROUP001" )              #Creates a new Group
        mutliport_in  = new_group.multi_port_in                      #Creates a new multiport in node
        mutliport_out = new_group.multi_port_out                     #Creates a new multiport out node
        cc_node = new_group.nodes.create( "COLOR_CARD", "CC" )       #Creating inside of the group.
        cc_node.ports_in[0].link(mutliport_in)                       #Link the CC to the port multi-port-in
        cc_node.ports_out[0].link(mutliport_out)                     #Link the CC to the port multi-port-out
        proj.history.end()
        ```
        """
        return Node()
        
    @property
    def multi_port_out(self) -> Node:
        """
        Returns existing or add a group multi port out node.

        Adds a multi port out node inside the group if one doesn't already exist. If there is already such type of node in the group, it will return it. NULL if it cannot add such node. You cannot add this type of node in the top group of a scene and there can only be a single such node per group.

        See OMC::GroupNode::multi_port_in for an example.
        """
        return Node()
        
    @property
    def nodes(self):
        """
        Get nodes that exist within the group.

        A group's nodelist provides the list of all the nodes in the group. This will not include the nodes within the subgroups inside the node, these would require a recursive iterator. It can also be used to create and remove nodes within a group as needed.

        Print path of all Nodes in the Scene:
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        group_node = scene.nodes["Top/Group"]
        nodes = group_node.nodes                                     #The nodes within a group.
        for node in nodes:
        print( "Node: %s (%s)"%(node.path, node.type) )
        def recursiveNodeListing( nodelist, depth ):
        for node in nodelist:
            print( "%s %s"%( "   "*depth, node.path ) )
            if node.type.upper() == "GROUP":                         #This group may contain other groups.
            recursiveNodeListing( node.nodes, depth+1 )            #Use this same function to identify further nodes within groups.
        top_nodelist = scene.top.nodes                               #The 'top' group of a scene behaves as any other node.
        recursiveNodeListing( top_nodelist, 0 )                      #Start identifying nodes from the top group's content.
        ```
        """
        return NodeList()
    

class Harmony(Application):
    """
    The Harmony Application object.

    The top level object, representing the currently running instance of Harmony and provides access to the loaded project and its contents.
    """ 
    @property
    def notify_enabled(self) -> bool:
        """
        Get/set whether application notifications are enabled.

        Most actions in Harmony result in events that update the GUI and refresh the contents in the scene. Setting the notify_enabled to false will prevent these intermediate updates, and will often allow scripts to run faster. Once a script has completed, it is important that this be reenabled in order for the GUI to appropriately update with all expected changes.

        ```python
        import math
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        sess.notify_enabled = False                                  #Disable application events, so everything happens under-the-hood, quickly.
        proj = sess.project
        scn  = proj.scene
        top  = scn.top
        for n in range( 100 ):                                       #Create 100 pegs -- for fun!
        rad  = ( n / 100.0 ) * 2.0 * math.pi                       #Time to be fancy!
        dist = 100.0
        new_node = top.nodes.create( "PEG", "PEG_%04d"%(n) )
        new_node.position.x = math.cos( rad ) * dist
        new_node.position.y = math.sin( rad ) * dist
        sess.notify_enabled = True                                   #Reenable applicaiton events to see all 100 fancy new pegs (in record time!)
        ```
        """
        return ""

class HarmonyClipboard(Clipboard):
    """
    The specialized Clipboard class for Harmony.

    The Harmony Clipboard has some of its own specializations which are made available in this class. For more information see OMC::Clipboard.
    """
    def __init__(self):
        super().__init__()

class HarmonyProject(Project):
    """
    The project loaded within the application. The project provides access to functions and properties related to the active project within the instance of the application.
    """
    def __init__(self):
        super().__init__()
    
    def save_all(self):
        """
        Performs the "save all" command.

        Effectively, this saves the entire project and all modified files.

        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        #. . .  Modify the scene here.
        proj.save_all()
        ```
        """
        return
    
    def save_as_new_version(self, name:str, markAsDefault:bool=True):
        """
        Save the current project to the specified folder.

        Saves the project as a new version with the provided name and an option to make this version the default.

        Parameters
            name	- The name of the new version. This will become the file name for offline scenes.
            markAsDefault	- (Optional, default is true), Defines if this is the default version of the scene in the database.
        
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        #. . .  Modify the scene here.
        proj.save_as_new_version( "newVersionName", True )
        ```
        """
        return
    
    def save_as(self, pathname:str):
        """
        Save the current project to the specified folder.

        Save the current project to the specified folder. Folder must not exist. The current project is updated to use that folder. Any error or message is reported using the standard error logger (so, in non batch mode, user will see message popup). This API only works in standalone as you cannot 'Save As' in database.
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        #. . .  Modify the scene here.
        proj.save_as( "path/to/newProject/location" )                #Expectation: The project will be saved to path/to/newProject/location/location.xtage
        ```
        """
        return
    
    def create_render_handler(self):
        """
        Creates a render handler that can be used to render content in a scene.

        The render handler is a temporary object-type that provides render access to nodes in the scene. The render handler will not block the application and will require callbacks where needed.

        Returns
            The new OMH::HarmonyRenderHandler
        
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        render_handler = proj.create_render_handler()                #The new render handler that has been generated; will not have any changes from other handlers.
        render_handler.blocking = True                               #This handler will block the main application. Optional.
        scn = proj.scene
        node = scn.nodes["Top/Write"]                                #Get the Top/Write node by name.
        print( "Rendering : %s"%(node) )
        if node:
        render_handler.node_add( node )                            #The render handler will render any nodes added to it.
        render_handler.render()                                    #In the case of write nodes, the write node's parameters will define the settings of the exported frame.
        print( "COMPLETE!" )    
        ```
        """
        return HarmonyRenderHandler()
    
    @property
    def scene(self):
        """
        Provides the current project's top-level scene.

        In Harmony, this provides the top-level scene in the project; the main scene loaded when the project is loaded.
        Other scenes can exist as symbols in the library and are available in OMH::HarmonyProject::scenes.
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #The main scene in the project.
        print( "Scene Name: %s"%(scene.name) )                       #Expectation: "Top", the main scene in the project.
        ```
        """
        return HarmonyScene()
        
    @property
    def scenes(self):
        """
        Provides a list of all available scenes in the project. These scenes are used as templates in Harmony.

        Provides the list of all the scenes available in the project. This allows access to the scenes used within symbols.
        Note
        The first scene in the list is always the 'Top' primary scene provided by OMH::HarmonyProject::scene
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scenes = proj.scenes                                         #The scenelist of all scenes in the project.
        for scn in scenes:                                           #Expectation: All names of all scenes in the project printed.
        print( "Scene Name: %s"%(scn.name) )
        ```
        """
        return HarmonySceneList()
        
    @property
    def elements(self) -> ElementList:
        """
        Provides a list of all available elements in the project.

        Elements represent groups of related media that can be displayed in read nodes. These elements refer to symbols, folders and media on disk and contain element drawings.
        The element list is a list of all elements contained within a project, and is used to add and remove elements as needed.
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        elems = proj.elements                                        #The element list of all elements in the project.
        print( "Element Count: %s"%(len(elems)) )
        for elem in elems:                                           #Expectation: All names of all scenes in the project printed.
        print( "Element Name: %s"%(elem.name) )
        ```
        """
        return ElementList()
        
    @property
    def version_current(self) -> int:
        """The ID of the current version."""
        return 1
        
    @property
    def version_name(self) -> str:
        """The name or the number of the current scene version."""
        return ""
        
    @property
    def environment_name(self) -> str:
        """The name of the current environment."""
        return ""
        
    @property
    def environment_path(self) -> str:
        """The path of the current environment."""
        return ""
        
    @property
    def job_name(self) -> str:
        """The name of the current job."""
        return ""
        
    @property
    def job_path(self) -> str:
        """The path of the current job."""
        return ""
        
    @property
    def scene_name(self) -> str:
        """The name of the current scene."""
        return ""
        
    @property
    def project_path(self) -> str:
        """The current project path."""
        return ""
        
    @property
    def project_path_remapped(self) -> str:
        """For windows, the remapped path."""
        return ""
        
    @property
    def project_path_temp(self) -> str:
        """The temporary project path."""
        return ""
        
    @property
    def project_path_temp_remapped(self) -> str:
        """For windows, the remapped temporary project path."""
        return ""
        
    @property
    def palette_manager(self):
        """
        The palette manager for the project.

        Not yet implemented.
        """
        return PaletteManager()
        
    @property
    def dirty(self) -> bool:
        """
        Identifies if the project is currently in a dirty state (has it been modified).

        When an action modifies the project, the project is marked as dirty. Undoing the operations, or saving, will result in the project no longer being dirty.

        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        harmony.open_project( "path/to/project.xstage" )
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project
        history = proj.history
        print( "Dirty: %s"%proj.dirty )                              #Expecting "Dirty: False", since the scene was just opened above.
        scn  = proj.scene
        top  = scn.top
        new_node = top.nodes.create( "PEG", "PEG_001" )
        print( "Dirty: %s"%proj.dirty )                              #Expecting "Dirty: True", since a node was added.
        history.undo( len(history) )                                 #Undo everything in the history, to return to the start state.
        print( "Dirty: %s"%proj.dirty )                              #Expecting "Dirty: False", since everything was undone.
        ```
        """
        return True
        
    @property
    def dirty_previously(self) -> bool:
        """
        Identifies if the project has ever been in a dirty state (has it ever been modified).

        When an action modifies the project, the project is marked as dirty. Undoing the operations, or saving, will result in the project no longer being dirty.
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        harmony.open_project( "path/to/project.xstage" )
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project
        history = proj.history
        print( "Dirty: %s"%proj.dirty )                              #Expecting "Dirty: False", since the scene was just opened above.
        scn  = proj.scene
        top  = scn.top
        new_node = top.nodes.create( "PEG", "PEG_001" )
        print( "Dirty: %s"%proj.dirty )                              #Expecting "Dirty: True", since a node was added.
        proj.save_all()
        print( "Dirty: %s"%proj.dirty )                              #Expecting "Dirty: False", since everything was saved.
        print( "Dirty Prev: %s"%proj.dirty_previously )              #Expecting "Dirty Prev: True", since something was done at some point.
        ```
        """
        return True
        
    @property
    def history(self):
        """
        The undo history of the application. Can be used to undo and redo commands in the history.

        The history is useful for undoing, redoing, and creating undo-states in the application's history.

        Creating an Undo State:
        ```python
        import math
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        sess.notify_enabled = False                                  #Disable application events, so everything happens under-the-hood, quickly.
        proj    = sess.project
        scn     = proj.scene
        top     = scn.top
        history = proj.history
        history.begin( "Unnecessary Peg Spiral" )                    #All subsequent peg creation commands will be accumulated into this history item.
        times_around = 3.0
        for n in range( 1000 ):                                      #Create 1000 pegs -- for fun!
        perc = ( n / 1000.0 )
        rad  = perc * 2.0 * math.pi * times_around                 #Time to be fancy!
        dist = 300.0 * perc
        new_node = top.nodes.create( "PEG", "PEG_%04d"%(n) )
        new_node.position.x = math.cos( rad ) * dist
        new_node.position.y = math.sin( rad ) * dist
        history.end()                                                #This history item will be closed, and actions are no longer accumulated.
        sess.notify_enabled = True                                   #Reenable application events to see all 100 fancy new pegs (in record time!)
        ```

        Undoing the Last State:
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj    = sess.project
        history = proj.history
        history.undo() 
        ```
        """
        return History()
        
    @property
    def resolution(self):
        """
        Get the resolution properties of the scene.

        The OMC::ProjectResolution object allows for read/write access to the current project's resolution and related project settings. Setting a New Resolution:

        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj       = sess.project
        resolution = proj.resolution
        print( "Current Resolution: %s x %s"%(resolution.x, resolution.y) )
        resolution.x = 2578
        resolution.y = 1080
        print( "New Resolution: %s x %s"%(resolution.x, resolution.y) )   #Expected result: "New Resolution: 2578 x 1080"
        ```
        """
        return ProjectResolution

class RenderHandler(BaseObject):
    def __init__(self):
        super().__init__()

class HarmonyRenderHandler(RenderHandler):
    """
    The render-handler object for Harmony.

    The render handler is a temporary object-type that provides render access to nodes in the scene. The render handler will not block the application and will require callbacks where needed.

    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    render_handler = proj.create_render_handler()                #The new render handler that has been generated; will not have any changes from other handlers.
    render_handler.blocking = True                               #This handler will block the main application. Optional.
    scn = proj.scene
    node = scn.nodes["Top/Write"]                                #Get the Top/Write node by name.
    print( "Rendering : %s"%(node) )
    if node:
    render_handler.node_add( node )                            #The render handler will render any nodes added to it.
    render_handler.render()                                    #In the case of write nodes, the write node's parameters will define the settings of the exported frame.
    print( "COMPLETE!" )                                       #Prints only when complete, due to blocking above--
    ```
    """
    def __init__(self):
        super().__init__()
    
    def frame_ready(self, Node:Node, frame:int, frameImage:Cel):
        """Signal that is emit when a frame is ready from the actively rendering job."""
        return
    
    def render_state_changed(self):
        """Signal that is emit when the state of the actively rendering job is changed."""
        return
    
    def progress(self, prog:int):
        """Signal that is emit when the progress of the job changes."""
        return
    
    def reset_resolution(self):
        """Resets the resolution to the scene's default values."""
        return
    
    def nodes(self) -> List[Node]:
        """Provides the list of nodes that will be rendered."""
        return [Node]
    
    def node_add(self, node:Node):
        """Add a node to a list of nodes to render."""
        return
    
    def node_remove(self, node:Node):
        """Remove a node from the list of nodes to render."""
        return
    
    def node_clear(self):
        """Remove a node from the list of nodes to render."""
        return
    
    def render(self, fromFrame:int, toFrame:int):
        """
        Render the entire scene.
        Render a part of the scene.
        """
        return
    
    def cancel(self):
        """Cancel the rendering scene."""
        return
    
    def block_until_complete(self):
        """
        Blocks script execution until the job has completed.

        Parameters
            timeout	- Time in seconds to wait before timing out and unblocking
        """
        return
    
    @property
    def combine(self) -> bool:
        """Set if rendered frames sets should be combined and in which order. Specify these options if you are rendering in PAL or NTSC format."""
        return True
        
    @property
    def second_field_first(self) -> bool:
        """Sets the order in which the fields should be ordered."""
        return True
        
    @property
    def field_type(self) -> str:
        """
        Sets the frame output format.

        Parameters
            type	- frame output format: None, NTSC, PAL
        """
        return ""
        
    @property
    def background(self) -> Colour:
        """Set the background color to use when rendering in scene machine mode."""
        return Colour()
        
    @property
    def resolution(self) -> Rect2DI:
        """Get and set the render resolution."""
        return Rect2DI()
        
    @property
    def resolution_name(self) -> str:
        """Set the render resolution by name."""
        return ""
        
    @property
    def thumbnail_cropping(self) -> bool:
        """Enable or disable thumbnail cropping for the render. Mainly used when rendering thumbnails."""
        return True
        
    @property
    def blocking(self) -> bool:
        """
        Defines whether this render handler blocks or does not.

        Note, if the render handler does not block and it is being handled in an external Python interpreter – the rendering threads need to be processed intermittently to properly synchronize with the main python thread. In order to do this, please see process_messages().
        """
        return True
        
    @property
    def blocking_time(self) -> int:
        """Defines how long to block in scripting when rendering (how long until render times out)"""
        return 1
        
    @property
    def state(self) -> str:
        """Identifies if Harmony is actively rendering."""
        return ""
        
    @property
    def formats_available(self) -> List[str]:
        """View available formats for the cel conversion at render."""
        return [""]
        
    @property
    def frame_ready_callback(self) -> PythonFunction:
        """
        Provide a callback function for the frame-ready event.

        If a callback function is provided, it will be called every time a frame is ready. This callback function should be in the form:

        def frame_ready_callback( node, frame, cel )
        """
        return
        
    @property
    def render_state_changed_callback(self) -> PythonFunction:
        """
        Provide a callback function for the render-state-changed event.

        If a callback function is provided, it will be called every time the render state changes for this render handler's job.

        def render_state_changed_callback( )
        """
        return True
        
    @property
    def progress_callback(self) -> PythonFunction:
        """
        Provide a callback function for the progress event.

        If a callback function is provided, it will be called every time the progress of the job updates. The value is provided as an integer representing the percent completion.

        def progress_callback( )
        """
        return True

class History(BaseObject):
    """
    Undo History for the Application.

    The undo history for the application. Allows access to the command history and provides the ability to create new undo accumulations from scripts being run in the Object Model.
    Provided via the project attribute OMC::Project::history.

    Create an Action and Undo It.
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project
    history = proj.history
    history.begin( "Accumulate Actions" )                        #Accumulate all Actions Between begin and end.
    scn  = proj.scene                                            #Get the main scene.
    top  = scn.top                                               #Get the top group of the main scene.
    new_node = top.nodes.create( "PEG", "PEG_001" )              #Action 1 - In history.
    new_node = top.nodes.create( "PEG", "PEG_002" )              #Action 2 - In history.
    new_node = top.nodes.create( "PEG", "PEG_003" )              #Action 3 - In history.
    history.end()                                                #This closes the block of actions, the history will only show the one action.
    #Print all actions in History.
    print( "Items in History: %s"%(len(history)) )
    for idx in range( len(history) ):
    print( "History Item %s : %s"%(idx, history[idx]) )
    history.undo()                                               #Undo this first action.
    history.undo( len(history) )                                 #Undo everything in the history.
    print( "Actions Executed : %s"%(history.size_executed) )     #How many actions have been executed? Expecting 0, as we've undone everything.
    print( "Actions Unexecuted : %s"%(history.size_unexecuted) ) #How many actions have been unexecuted (and can be redone)?
    ```
    """
    def __init__(self):
        super().__init__()
    
    def begin(self, commandName:str):
        """Begin accumulating actions into a single history item. This function starts the accumulation of all of the functions between it and the endUndoRedoAccum function as one command that will appear in the undo/redo list."""
        return
    
    def end(self):
        """Ends the accumulation of actions into a single history item. This function ends the accumulation all of the functions between it and the beginUndoRedoAccum function as one command that will appear in the undo/redo list."""
        return
    
    def cancel(self):
        """Cancels the currently accumulating history item. This function cancels the accumulation of undo/redo commands. No command will be added to the undo/redo list and all commands that have already been executed will be rolled-back (undone)"""
        return
    
    def undo(self, depth:int=1):
        """Undo events in the history. Undoes the last n operations. If n is not specified, it will be 1."""
        return
    
    def redo(self, depth:int=1):
        """Redo events in the history. Redoes the last n operations. If n is not specified, it will be 1."""
        return
    
    def clear(self):
        """Clears the history. Clears the command history. The events are not undone, but the history is cleared."""
        return
    
    def size(self):
        """Returns the size of history items that have been performed, and not undone."""
        return

class Port(BaseObject):
    """
    Represents and provides the methods for a node's port.

    The base class for ports – ports are used when connecting one node to another via the Port. All ports are owned from by their respective Node, and are provided via the node's PortList. The node is either a InNode at the top of the node and accepts incoming connections, or an OutNode at the bottom of a Node and connects Cables to other nodes.

    For more information, see OMC::InPort, OMC::OutPort, OMC::Node::ports_in, or OMC::Node::ports_out.
    """
    def __init__(self):
        super().__init__()
    
    @property
    def id(self) -> int:
        """The internal ID of the port."""
        return 1
        
    @property
    def type(self) -> str:
        """The type of the port."""
        return ""
        
    @property
    def index(self) -> int:
        """The index of the port on the node."""
        return 1
        
    @property
    def node(self) -> Node:
        """The node that owns this port."""
        return Node()
        
    @property
    def node_related(self) -> Node:
        """The node that this port leads to for multiport nodes and groups - the owner node for most node-types, but the the multi-port node for a group, or vice versa."""
        return Node()
        
    @property
    def inport(self) -> bool:
        """Whether the port is an inport."""
        return True
        
    @property
    def outport(self) -> bool:
        """Whether the port is an outport."""
        return True
        
    @property
    def port_related(self):
        """The port that this port relates to – itself for most node-types, but the corresponding port on the multi-port node for groups, or vice versa."""
        return Port()
    
class PortList(ListObj, IterableObj):
    """
    A list of ports on a node.

    The PortList is provided from a Node – and can either be the InPortList or PortList depending if it is intended for In or Out ports. Certain types of OMC::Node provide a PortList that can have ports added dynamically, and a MultiPortList or MultiInPortList will be provided to support the dynamic addition and removal of these ports. The port lists are iterable, provide a size and can be accessed with the list[] operator.
    The generic PortList – see also OMC::InPortList, OMC::MultiPortList, and OMC::MultiInPortList. Also see OMC::Node::ports_in and OMC::Node::ports_out.

    Identify all In Ports on a Node
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    peg = scene.nodes["Top/Peg"]                                 #Find the peg node.
    #Identify all In-Ports on a Peg
    ports_in = peg.ports_in                                      #The in-port list for the node.
    for idx,port in enumerate(ports_in):
    connection = "NONE"
    if port.source_node:                                       #Check if this port is connected to anything.
        connection = port.source_node.path
    print( "Port %s : %s"%(idx, connection) )
    ```
    
    Identify all Out-Ports on a Node
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    peg = scene.nodes["Top/Peg"]                                 #Find the peg node.
    #Identify all Out-Ports on a Peg
    ports_out = peg.ports_out                                    #The out-port list for the node.
    for idx,port in enumerate(ports_out):
    destination_nodes = port.destination_nodes
    print( "Port %s :"%(idx) )
    for idx2,node in enumerate(destination_nodes):
        print( "  %s : %s"%(idx2, node.path) )
    ```
    """
    def __init__(self):
        super().__init__()
    
    def list(self) -> List[Port]:
        """Converts the dynamic list into a concrete list of Port objects."""
        return [Port()]
    
    def __getitem__(self, idx:int) -> Port:
        """Provides the Port at the given index."""
        return Port()
    
    @property
    def dynamic(self) -> bool:
        """Identifies if ports can be created on this portlist and the node."""
        return True

class InPort(Port):
    """
    Represents and provides the methods for a node's in port.

    The InPort is a port at the top of a node that accepts incoming connections from another node's OutPort. These are used in order to define a node-graph path between nodes and is the basis of rigging within the application.

    Identify all In Ports on a Node
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    peg = scene.nodes["Top/Peg"]                                 #Find the peg node.
    #Identify all In-Ports on a Peg
    ports_in = peg.ports_in                                      #The in-port list for the node.
    for idx,port in enumerate(ports_in):
    connection = "NONE"                                        
    if port.source_node:                                       #Check if this port is connected to anything.
        connection = port.source_node.path
    print( "Port %s : %s"%(idx, connection) )
    ```

    Connect Some Nodes
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    top = scene.top                                              #The top group.
    proj.history.begin( "Test Node Connection" )
    peg  = top.nodes.create( "PEG", "PEG001" )
    read = top.nodes.create( "READ", "DRAWING001" )
    #Connect the ports!
    read.ports_in[0].source = peg.ports_out[0]                   #Connecting the in port of the read to the outport of the peg. 
    proj.history.end()
    ```
    """
    def __init__(self):
        super().__init__()
    
    def link(self, outPort) -> Cable:
        """
        Connects this in port, to the outport of another node.

        Returns
            The cable that connects the nodes, if successful.
        """
        return Cable()
    
    def unlink(self):
        """Disconnects this port from another other port."""
        return
    
    @property
    def linked(self) -> bool:
        """True if the port is a dynamic port."""
        return True

    @property
    def matte_port(self) -> bool:
        """Identifies if the port is a matte port."""
        return True
        
    @property
    def cable(self) -> Cable:
        """Provide the cable connected to a port."""
        return Cable()
        
    @property
    def cable_flat(self) -> Cable:
        """Provide the flattened, read-only cable connected to a port. Ignoring all mutli-port modules and groups."""
        return Cable()
        
    @property
    def source(self) -> Port:
        """Get and set the source port that is connected to this port."""
        return Port()
    
    @property
    def source_node(self) -> Node:
        """Get and set the source node that is connected to this port."""
        return Node()
        
    @property
    def source_flat(self) -> Port:
        """Get the flat source port that is connected to this port."""
        return Port()
        
    @property
    def source_node_flat(self) -> Node:
        """Get the flat source node that is connected to this port."""
        return Node()

class InPortList(PortList):
    """
    A port list specific for InPort lists on nodes.

    This list will provide a list of OMC::InPort belonging to a node and is provided from OMC::Node::ports_in.
    For more information see OMC::PortList.
    """
    def __init__(self):
        super().__init__()
    
    @property
    def matte_port(self) -> Port:
        """The matte port in the list."""
        return Port()
    
class IntAttribute(Attribute):
    """
    The int attribute wrapper.

    This object wraps a int attribute owned by a node. The int attribute is an attribute that provides a integer number value and can be animateable.
    """
    def __init__(self):
        super().__init__()
    
    def localvalue(self) -> int:
        """
        Get the attribute's localvalue as a int value.

        Provides the localvalue as a int value. The local value is the non-animateable value of an attribute when no column is present. If the attribute can be linked and has a column linked to it, the value at a frame is provided by the column and the local value is ignored.

        Note
        Its generally better to reference the value over the localvalue. When no column is present, the value will also provide the localvalue – this is not true in reverse, if a column is present, the localvalue will still reference the ignored localvalue. Non-animateable attributes that cannot be linked will only provide the localvalue.


        Retrieve a int Localvalue
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Drawing"]                            #Find the Peg node.
        int_attribute_keyword = "OPACITY"                            #The path to a int attribute
        attribute = node.attributes[int_attribute_keyword]           #Get the attribute by name
        if attribute:
        current_value = attribute.localvalue()                     #Get the attribute's localvalue.
        #Show the localvalue of the attribute.
        print( "LOCALVALUE: %s "%( current_value ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(int_attribute_keyword) )
        ```
        """
        return
    
    def value(self, frame:int) -> int:
        """
        Get the attribute's value as a int value at a given frame.

        Provides the value as a int value. If the attribute can be linked and has a column linked to it, the value at a frame is provided by the column and the local value is ignored.


        Retrieve a int Value
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Drawing"]                            #Find the Peg node.
        int_attribute_keyword = "OPACITY"                            #The path to a int attribute
        attribute = node.attributes[int_attribute_keyword]           #Get the attribute by name
        if attribute:
        at_frame = 1
        current_value = attribute.value(at_frame)                       #Get the attribute's value at frame 1
        #Show the value of the attribute.
        print( "VALUE AT FRAME %s : %s"%( at_frame, current_value ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(int_attribute_keyword) )
        ```
        """
        return
    
    def set_localvalue(self, value:int):
        """
        Sets the attribute's local value as a int value.

        Sets the local value of the attribute to the provided int value. The local value is the non-animateable value of an attribute when no column is present. If the attribute can be linked and has a column linked to it, the value at a frame is provided by the column and the local value is ignored.

        Note
        Its generally better to reference the value over the localvalue. When no column is present, the value will also provide the localvalue – this is not true in reverse, if a column is present, the localvalue will still reference the ignored localvalue. Non-animateable attributes that cannot be linked will only provide the localvalue.
        
        Parameters
            value	- the int value to which the attribute should be set.


        Set a OMC::Color Localvalue
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        import random
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Drawing"]                            #Find the Peg node.
        int_attribute_keyword = "OPACITY"                            #The path to a int attribute
        attribute = node.attributes[int_attribute_keyword]           #Get the attribute by name
        if attribute:
        current_value = attribute.localvalue()                     #Get the attribute's localvalue.
        #Show the current localvalue of the attribute.
        print( "CURRENT LOCALVALUE: %s"%( current_value ) )
        new_value = random.randint( attribute.minimum, attribute.maximum )
        attribute.set_localvalue( new_value )                      #Set the attribute's local value to the new value
        new_value = attribute.localvalue()                         #Get the attribute's new localvalue, to check it for debug/example purposes
        print( "NEW LOCALVALUE: %s"%( new_value ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(int_attribute_keyword) )
        ```
        """
        return
    
    def set_value(self, frameOrRange, value:int):
        """
        Set the attribute's value as a int value at a given frame.

        Sets the value of the attribute to the provided int value at the given frame. If the attribute can be linked and has a column linked to it, the value is set on the column – otherwise, it is set on the localvalue of the attribute.

        Note
        If no column is present, setting an animateable column's value on the attribute will result in the creation of a new column.
        
        Parameters
            frame	- the frame at which the attribute is set.
            value	- the int value to which the attribute should be set.


        Set a int Value at a Frame
        ```python
        import random
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Drawing"]                            #Find the Peg node.
        int_attribute_keyword = "OPACITY"                            #The path to a int attribute
        attribute = node.attributes[int_attribute_keyword]           #Get the attribute by name
        if attribute:
        at_frame = 1
        current_value = attribute.value( at_frame )                #Get the attribute's value.
        #Show the current localvalue of the attribute.
        print( "CURRENT VALUE AT %s : %s"%( at_frame, current_value ) )
        new_value = random.uniform( attribute.minimum, attribute.maximum )
        attribute.set_value( at_frame, new_value )                                                      #Set the attribute's local value to the new value
        new_value = attribute.value( at_frame )                                                         #Get the attribute's new localvalue, to check it for debug/example purposes
        print( "NEW VALUE AT %s : %s"%( at_frame, new_value ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(int_attribute_keyword) )
        ```
        """
        return
    
    def offset_value(self, frameOrRange, value:int):
        """
        Offsets the attribute's value at a given frame or frame range.

        Provided a OMC::Colour object, will offset the existing value (either the animated value, or local value if none exists) by the color argument's value.

        Parameters
            frameOrRange	- A frame range provided by a list in form [startFrame, endFrame]
            value	- The OMC::Colour object to by which the attribute is offset.

        Offset a Color Attribute
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Drawing"]                            #Find the Peg node.
        int_attribute_keyword = "OPACITY"                            #The path to a int attribute
        attribute = node.attributes[int_attribute_keyword]           #Get the attribute by name
        if attribute:
        at_frame = 1
        current_value = attribute.value( at_frame )                #Get the attribute's value.
        #Show the current localvalue of the attribute.
        print( "CURRENT VALUE AT %s : %s"%( at_frame, current_value ) )
        new_value = random.uniform( attribute.minimum - current_value, attribute.maximum - current_value  )
        range = [ at_frame, scene.frame_count ]                    #The range will be from at_frame, to the last frame of the scene.
        attribute.offset_value( range, new_value )                 #Offset the attribute's value by the provided value
        new_value = attribute.value( at_frame )                    #Get the attribute's new localvalue, to check it for debug/example purposes
        print( "NEW VALUE AT %s : %s"%( at_frame, new_value ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(int_attribute_keyword) )
        ```
        """
        return

    @property
    def minimum(self) -> int:
        """
        Get the minimum value of the attribute.

        Int attributes can have a minimum value that the attribute can provide. This minimum value is provided from the minimum property.
        """
        return 1
    
    @property
    def maximum(self) -> int:
        """
        Get the max value of the attribute.

        Double attributes can have a maximum value that the attribute can provide. This maximum value is provided from the maximum property.
        """
        return 1
    
    @property
    def step(self) -> int:
        """
        Get the incremental step-value of the attribute.

        In the layer properties panel of the GUI, the attribute will increment at the step-rate provided by this property.
        """
        return 1

class IterableQVar():
    def __init__(self):
        super().__init__()

class ListQVar():
    def __init__(self):
        super().__init__()

class JavascriptObject(ListQVar, IterableQVar):
    """
    An object that represents a loaded javascript object and its global context.

    This object is already loaded in memory and is persistent as long as the Python object exists.

    A Simple Example - Creating a Python-JS Interface
    ```python
    from ToonBoom import harmony
    sess = harmony.session()
    js = sess.javascript
    js_string = \"""
    function frame_next()
    {
        frame.setCurrent( frame.current()+1 );
    }
    function frame_last()
    {
        frame.setCurrent( frame.current()-1 );
    }
    function frame_set( target_frame )
    {
        frame.setCurrent( target_frame );
    }
    function frame_current()
    {
        return frame.current();
    }
    \"""
    frame_helper = js.load_string( js_string )
    #Using javascript to change frames and access the frame handler in JS.
    #Go to the next frame
    frame_helper["frame_next"].call()
    print( "Now on frame: %s"%( frame_helper["frame_current"].call() ) )
    frame_helper["frame_last"].call()
    print( "Now on frame: %s"%( frame_helper["frame_current"].call() ) )
    frame_helper["frame_set"].call( [10] )
    print( "Now on frame: %s"%( frame_helper["frame_current"].call() ) ) #10
    ```

    Javascript Object can be Incrementally Extended
    ```python
    from ToonBoom import harmony
    sess = harmony.session()
    js = sess.javascript
    #Note- the first trace will result in error since the variable is missing.
    js_string = \"""
    function testFunction()
    {
        MessageLog.trace( initiallyMissingVariable );
    }
    \"""
    js_obj = js.load_string( js_string )
    try:
    js_obj["testFunction"].call()
    except:
    print( "Variable is missing -- as expected." )
    print( "Adding missing variable" )
    js_obj["initiallyMissingVariable"] = "No longer missing"
    js_obj["testFunction"].call()
    ```
    """
    def __init__(self):
        super().__init__()
    
    def contains(self, propName) -> bool:
        """
        Checks the if the object contains a given property at key or at value if the object is an array.

        Introspecting a JS Object
        ```python
        from ToonBoom import harmony
        sess = harmony.session()
        js = sess.javascript
        js_string = \"""
        var objectExists = "Exists";
        \"""
        js_obj = js.load_string( js_string )
        if js_obj.contains( "objectExists" ):
        print( "Exists as expected." )
        if not js_obj.contains( "objectDoesntExist" ):
        print( "Doesn't exist, as expected." )
        ```
        Returns
            True if contains the property.
        """
        return True
    
    def remove(self, propValue):
        """Removes a property from the object at key or at value if the object is an array. For removing at index on arrays, use pop() method instead."""
        return
    
    def pop(self, propIdx:int):
        """
        Pops a property from the array object at index.

        Returns
            The popped value.
        """
        return
    
    def insert(self, propIdx:int, propValue):
        """Inserts a property in the middle of arrays."""
        return
    
    def clear(self):
        """Clears the object of any property."""
        return
    
    def append(self, propValue):
        """Appends a property to the end of an array."""
        return
    
    def call(self, arguments, selfValue):
        """
        Calls the javascript function with the provided arguments and an object representing the object bound to the self at the function's execution.

        Parameters
            arguments	- A list of arguments provided to the function being called. If the function is defined with named-arguments, the arguments will use those names.
            selfValue	- An object that is bound to the function when called. This object is available with the 'this' object in the context of the function.
        
        Calling a function with 'this' object bound
        ```python
        from ToonBoom import harmony
        sess = harmony.session()
        js = sess.javascript
        js_string = \"""
        function functionWithThisBound()
        {
            if( this.contextExists )
            {
            return true;
            }
            return false;
        }
        \"""
        js_obj = js.load_string( js_string )
        results = js_obj["functionWithThisBound"].call( [] )
        print( "%s : Expecting False -- no context provided."%(results) )
        results = js_obj["functionWithThisBound"].call( [], { "contextExists":True } )
        print( "%s : Expecting True -- context provided."%(results) )
        ```

        Returns
            Returns the javascript function return value.
        """
        return
    
    @property
    def source(self) -> str:
        """The source of the javascript object – the file path if loaded from a file, otherwise from memory."""
        return ""
        
    @property
    def type(self) -> str:
        """Identifies the type of this object as a string value."""
        return ""
    
class JavascriptRootObject(JavascriptObject):
    """
    An object that represents the root javascript object and its global context, as well as information about its original script's source.

    The root Javascript object is the initial Javascript object that is loaded from a string or file source. This evaluated root is often the global object and provides the context for other objects in ts context.

    The Javascript root object provides utilities for reloading the file or script as needed, and maintains a cached copy of the script at the time it is run.
    It is best to avoid re-evaluating the scripts constantly – this will help avoid unnecessary processing and allows for a more persistent scripting environment.

    Loading a Javascript Root Object
    The following is more of a proof of concept for the interoperability between Javascript and Python – the whole UI can be generated directly in Python/PySide instead.
    ```python
    from ToonBoom import harmony
    sess = harmony.session()
    js = sess.javascript
    js_string = \"""
    function setupUI( pythonFunc )
    {
        var mainWidget = new QWidget();
        var button = new QPushButton( mainWidget );
        var layout = new QHBoxLayout();
        mainWidget.setLayout(layout);
        layout.addWidget(button, 1, 0);
        button.text = "Hello World"
        button.pressed.connect( pythonFunc.call );
        mainWidget.show();
        return mainWidget;
    }
    \"""
    def myCallbackFunction():
    print( "Hello Python World" )
    js_obj = js.load_string( js_string )
    #Initialize the JS UI with a Python callback function.
    js_obj["setupUI"].call( myCallbackFunction )
    #Clicking the button will result in the Python Function to be called.
    ```
    """
    def __init__(self, javascript:str, filePath:str):
        super().__init__()

    def reload(self, fromDisk=False):
        """
        Reevaluates the javascript object from the original string, or from the original file's path.

        If optional fromDisk is true, the javascript object is loaded from its original path and not from its cached string.

        Parameters
            fromDisk	- In the event that the object was loaded from a file, setting fromDisk to true will reload it from that same file. Otherwise, reloads it from a local cache.
        """
        return
    
    @property
    def path(self) -> str:
        """Provides the path to the loaded javascript content, if provided from a path."""
        return ""
        
    @property
    def script(self) -> str:
        """
        Get and set the script's string.

        This string is used for the evaluation of the script. If this value is changed, the script needs to be reevaluated.

        Changing a root objects script and reevaluating
        ```python
        from ToonBoom import harmony
        sess = harmony.session()
        js = sess.javascript
        js_string_001 = \"""
        function hello()
        {
            MessageLog.trace( "Hello" );
        }
        \"""
        js_string_002 = \"""
        function world()
        {
            MessageLog.trace( "World" );
        }
        \"""
        js_obj = js.load_string( js_string_001 )
        js_obj["hello"].call( [] )  #MessageLog -- "Hello"
        js_obj.script = js_string_002
        js_obj.reload() #Reload the script, now that it is changed.
        js_obj["world"].call( [] )  #MessageLog -- "World"
        ```
        """
        return ""
        
    @property
    def loaded(self) -> bool:
        """Identifies if the script has been successfully loaded into the script interface."""
        return True
    
class Matrix(BaseObject):
    """Provides a 3D transformation matrix (4x4)."""
    def __init__(self):
        super().__init__()
    
    def matrix_rotation(self):
        """Returns rotation component of this matrix (3x3 block)."""
        return Matrix()
    
    def reset(self):
        """Resets the matrix to the identity matrix."""
        return
    
    def normalize(self):
        """Normalizes the matrix."""
        return
    
    def apply(self, variant):
        """Applies the matrix to the incoming variant type – returning the result."""
        return
    
    def multiply(self, matrix):
        """Compounds this matrix with m, same as = (*this) * m. The matrix object is modified in place."""
        return
    
    def translate(self, vector, deltaX:int=0.0, deltaY:int=0.0, deltaZ:int=0.0):
        """
        Translates the local coordinate system represented by this tranformation matrix by the given vector. The matrix object is modified in place.
        """
        return
    
    def scale(self, scaleX:int=1.0, scaleY:int=1.0, scaleZ:int=1.0):
        """Scales the local coordinate system represented by this tranformation matrix by the given factors. The matrix object is modified in place."""
        return
    
    def rotate_radians(self, rads:float, vector):
        """Rotates the local coordinate system represented by this tranformation matrix by the given angle (expressed in radian) around the given vector. The matrix object is modified in place."""
        return
    
    def rotate_degrees(self, degs:float, vector):
        """Rotates the local coordinate system represented by this tranformation matrix by the given angle (expressed in degree) around the given vector. The matrix object is modified in place."""
        return
    
    def skew(self, skew:float):
        """Skews the local coordinate system represented by this tranformation matrix by the given angle (expressed in degree). The matrix object is modified in place."""
        return
    
    def orthogonal_project(self, left:float, right:float, bottom:float, top:float, zNear:float, zFar:float):
        """Applies an orthogonal projection to the local coordinate system represented by this tranformation matrix. The matrix object is modified in place."""
        return
    
    def perspective_project(self, left:float, right:float, bottom:float, top:float, zNear:float, zFar:float, verticalFieldOfViewInDegrees:float, widthOverHeightAspectRatio:float):
        """Applies a perspective projection to the local coordinate system represented by this tranformation matrix. The matrix object is modified in place."""
        return
    
    def look_at(self, eye, center, upDirection):
        """Replaces this by a lookAt matrix. The matrix object is modified in place."""
        return
    
    def extract_parameters_2d(self, sxPos:bool, syPos:bool, pivot):
        """
        Extracts the individual transformation parameters from the matrix.

        Parameters
            sxPos	- Resolve x axis scale sign ambiguity.
            syPos	- Resolve y axis scale sign ambiguity.
            pivot	- Pivot position.
        
        The return is provided in a list of individual paramaters in the order: [ OMC::Point3d - Translation, OMC::Vector2d - Scale, double - angle (around z-axis) in degrees double - skew ]
        """
        return
    
    def extract_parameters_3d(self, pivot):
        """
        Extract 3d matrix parameters using 3d pivot value.

        Parameters
            pivot	- Pivot position.
        
        The return is provided in a list of individual paramaters in the order: [ OMC::Point3d - Translation, OMC::Vector3d - Scale, OMC::Vector3d - angle around each axis in degrees
        """
        return
    
    def inverse(self):
        """Inverse the current matrix."""
        return
    
    def get_inverse(self):
        """
        Provides the inverted matrix and leaves the current one unaffected.

        Returns
            The inverted Matrix.
        """
        return Matrix()
    
    def transpose(self):
        """Transposes this matrix."""
        return
    
    def print(self, string:str):
        """Prints the matrix' details to the application's stdout."""
        return
    
    @property
    def has_nan(self) -> bool:
        """True if the matrix has a NaN in any value."""
        return True
        
    @property
    def has_infinity(self) -> bool:
        """True if the matrix has infinity in any value."""
        return True
        
    @property
    def axis_x(self):
        """Get and set the x axis of the matrix."""
        return Vector3d()
        
    @property
    def axis_y(self):
        """Get and set the y axis of the matrix."""
        return Vector3d()
        
    @property
    def axis_z(self):
        """Get and set the z axis of the matrix."""
        return Vector3d()
        
    @property
    def origin(self):
        """Get and set the origin of the matrix."""
        return Point3d()
        
    @property
    def identity(self) -> bool:
        """Get and set whether the matrix is an identity matrix. Setting to true will reset the matrix."""
        return True
        
    @property
    def singular(self) -> bool:
        """True if the matrix is singular."""
        return True
        
    @property
    def truck_factor(self) -> float:
        """The truck factor is a compensation factor due to the zooming of the camera. It is inherent to the transformations of a matrix."""
        return 1.0
        
    @property
    def scale_factor(self) -> float:
        """The scale-factor inherent in the matrix."""
        return 1.0
        
    @property
    def rotation_exists(self) -> bool:
        """True if this matrix has a rotation or shear component (2D or 3D). False otherwise, in which case the matrix can only have scaling, perspective and translation components."""
        return True
        
    @property
    def constant_z(self) -> bool:
        """True if transforming a constant Z plane yields another constant Z plane."""
        return True
        
    @property
    def transform_2d(self) -> bool:
        """True if this matrix can be converted to a 3x2 matrix representing a 2d transformation, false otherwise."""
        return True
        
    @property
    def perspective(self) -> bool:
        """True if any of the matrix's three projection terms are non-zero."""
        return True

class MetaDataHandler(ListQVar, IterableQVar):
    """
    Provides access to the metadata of a specific object – a node, or a scene.

    The MetaDataHandler is used to provide generic metadata from a Node or a Scene. The metadata is created as a key-value pair, and is persistent; it can be saved and loaded as needed with the project.
    The MetaDataHandler is iterable and can be accessed with the map[string] operator.

    For Scene metadata, see OMH::Scene::metadata.

    Print all Metadata in the scene.
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    for metadata in scene.metadata:
    print( "Key : %s"%(metadata.key) )
    print( "  Value : %s"%(metadata.value) )
    print( "  Type : %s"%(metadata.type) )
    ```

    Create Some Metadata
    ```python
    import json
    import time
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    metadata = scene.metadata                                    #The metadata handler.
    production_data = { 
                        "artist"   : "John Doe",
                        "scene_id" : "TB_001_0010",
                        "date"     : int(time.time())
                    }
    metadata["production_data"] = json.dumps( production_data )
    print( "Set Production Data" )
    json_data = metadata["production_data"].value
    retrieved_data = json.loads( json_data )
    for x in retrieved_data:
    print( "%s : %s"%(x, retrieved_data[x]) )
    #The metadata will be saved and available within the scene in subsequent instances of Harmony. This is useful for saving
    #generic data related to scenes or nodes.
    ```

    For Node Metadata, see OMC::Scene::metadata.
    Print all Metadata in the node.
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    node = scene.nodes["Top/Drawing"]                            #The node that is being checked for metadata.
    if len(node.metadata) == 0:
    print( "Node has no Metadata" )
    for metadata in node.metadata:
    print( "Key : %s"%(metadata.key) )
    print( "  Value : %s"%(metadata.value) )
    print( "  Type : %s"%(metadata.type) )
    ```
    
    Create Some Metadata
    ```python
    import json
    import time
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    node = scene.nodes["Top/Drawing"]                            #The node that is being checked for metadata.
    metadata = node.metadata                                     #The metadata handler.
    production_data = {
                        "artist"   : "John Doe",
                        "scene_id" : "TB_001_0010",
                        "date"     : int(time.time())
                    }
    metadata["production_data"] = json.dumps( production_data )
    print( "Set Production Data" )
    json_data = metadata["production_data"].value
    retrieved_data = json.loads( json_data )
    for x in retrieved_data:
    print( "%s : %s"%(x, retrieved_data[x]) )
    #The metadata will be saved and available within the scene in subsequent instances of Harmony. This is useful for saving
    #generic data related to scenes or nodes.
    ```
    """
    def __init__(self):
        super().__init__()
    
    def __getitem__(self, name:str):
        """
        Get and set the metadata value.

        The map operator is used to get a value by name, and subsequently set it by name.
        """
        return
    
    def contains(self, name:str) -> bool:
        """
        Checks if the provided metadata name exists in the metadata-list.

        Checks the list for the provided item. Will return true if the list contains that item. This is also available via the Python built-in check for list object [ contained = object in list ].
        """
        return True
    
    def map(self):
        """Converts the dynamic map to a concrete map of names and metadata values ."""
        return
    
    def list(self) -> list:
        """Provide a list of metadata key values."""
        return []
    
    def remove(self, name:str):
        """Remove a metadata item from the object by name."""
        return

class MetaDataPair(BaseObject):
    """
    The key,value pair of the metadata object.

    The MetaDataPair is provided from the OMC::MetaDataHandler::map[QString] operator. Provides the key, value and various properties related to the specific metadata item.
    """
    def __init__(self):
        super().__init__()
    
    @property
    def key(self) -> str:
        """Gets the metadata's key value."""
        return ""
        
    @property
    def type(self) -> str:
        """Gets the metadata's type."""
        return ""
        
    @property
    def value(self):
        """Gets the metadata's value."""
        return
        
    @property
    def version(self) -> str:
        """Gets the metadata's version."""
        return ""
        
    @property
    def creator(self) -> str:
        """Gets the metadata's creator."""
        return ""
        
    @property
    def exists(self) -> bool:
        """True if the metadata value exists."""
        return True

class MultiPortList(PortList):
    def __init__(self):
        super().__init__()
    
    def create(self, type:str, port:Port, index:int, before:bool=True) -> Port:
        """
        [1/3] - type : Add a port to the node at the left of the existing ports.
        
        [2/3] - type + port + before : Add a port to the node, in reference to another port.
        
        [3/3] - type + index : Add a port to the node.
        """
        return Port()
    
    def remove(self):
        """
        [1/2] - index 

        Remove a port from the node.

        Returns
            True if the port was succesfully removed.
        ------------------------------------------------------------------------
        [2/2] - port

        Remove a port from the node.

        Returns
            True if the port was succesfully removed.
        """
        return

class MultiInPortList(MultiPortList):
    """
    A dynamic list of InPort objects belonging to a node.

    This object provides a list of OMC::InPort objects belonging to a node and is provided by modules that allow for dynamic port creation. The list operator[] provides access existing ports and allows for the creation and removal of ports as needed.
    """
    def __init__(self):
        super().__init__()
    
    @property
    def matte_port(self) -> Port:
        """The matte port in the list."""
        return Port()

class MultiPortNode(Node):
    """
    Represents and provides the methods for a multiport node.

    This is the base class for a Multiport Node. This class provides the functionality for nodes that can have ports dynamically created or removed. These types of nodes may provide a MultiPortList from either its Node::ports_in or Node::ports_out attribute.

    For more specific information, see OMC::MultiPortInNode and OMC::MultiPortOutNode.
    """
    def __init__(self):
        super().__init__()
    
    def add_port(self, portdIdx:int, port:Port, before:bool=True) -> InPort:
        """
        [1/2] - portdIdx + before
        
        Adds a port to the node.

        Parameters
            portdIdx	- the relative index used when creating a new port.
            before	- Whether the node is inserted before the relatived port index. Adds a port to the node, based on the provided index and the before option.
        
        Returns
            The port that was inserted.
        
        ------------------------------------------------------------------------
        [2/2] - port + before
        
        Adds a port to the node.

        Parameters
            port	- the relative port used when creating a new port.
            before	- Whether the node is inserted before the relatived port index. Adds a port to the node, based on the provided index and the before option.
        
        Returns
            The port that was inserted.
        """
        return InPort()
    
    def remove_port(self, portdIdx:int, port:Port):
        """
        [1/2] - portdIdx
        
        Removes a port from the node.

        Parameters
            portdIdx	- the relative port used when creating a new port.
        
        Returns
            The port that was inserted.
        
        ------------------------------------------------------------------------
        [2/2] - port
        
        Removes a port from the node.

        Parameters
            port	- the port object to remove.
        
        Returns
            The port that was inserted.
        """
        return

class MultiPortInNode(MultiPortNode):
    """
    Represents and provides the methods for a multiport-in node.

    The MultiPortInNode is a Node that allows for dynamic InPort creation. In-Ports can be added and removed as needed, and in some cases, the ports will be added automatically when connected to other nodes.
    """
    def __init__(self):
        super().__init__()

class MultiPortOutNode(MultiPortNode):
    """
    Represents and provides the methods for a multiport-out node.

    The MultiPortOutNode is a Node that allows for dynamic OutPort creation. Out-Ports can be added and removed as needed, and in some cases, the ports will be added automatically when connected to other nodes.
    """
    def __init__(self):
        super().__init__()

class NodeList(ListObj, IterableObj):
    """
    A class representing a list of nodes, providing utilities to modify, filter, and search the list.

    The Node List is an iterable object, with indexed-access. This means it can be iterated with a for-loop, provides a length/size method and can be accessed with a list index.

    Iterable Object-Type
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    nodes = scene.nodes                                          #Get the node list of the scene.
    #Iterating on the node list with a for-loop
    for node in node:                                            #For loop on the node list.
    print( "Node : %s"%(node.path) )
    ```

    Iterating with Index Accessor
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    nodes = scene.nodes                                          #Get the node list of the scene.
    node_size = len(nodes)                                       #Gets the size of the node list. This is a standard method for iterable list object-types.
    #Iterating on the node list with a ranged for-loop
    for node_idx in range(node_size):                            #For loop on a range based on node list's size.
    node = nodes[node_idx]                                     #Get the node from the node_idx currently being looped.
    print( "Node : %s - %s"%(node_idx, node.path) ) 
    ```

    The Node List also allows for name/path accessing. This is useful when accessing nodes based on the absolute path in the scene, or when relative to a group. If this nodelist is provided by the scene from OMC::Scene::nodes, the paths are not relative to any specific groups and needs to be provided as an absolute path name. If this nodelist is provided by a group, even the 'Top' group of the scene, the paths are relative to that group and can be provided with a name relative to that group's path.

    Accessing a Node by its Path:
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    nodes = scene.nodes                                          #Get the node list of the scene.
    desired_node = nodes["Top/Peg"]                              #Find the node by the requested path : "Top/Peg"
    if desired_node:
    print( "Found Node: %s"%(desired_node) )
    else:
    print( "No Node found by the requested name." )
    ```
    """
    def __init__(self):
        super().__init__()
    
    def size(self):
        """
        Provides the list's size.

        The size of the list is available from the size-method, but also available from the built-in utilities in Python [ len( Object ), Object.__len__ ]
        See referencing from an list index.
        """
        return
    
    def contains(self) -> bool:
        """
        Checks if the provided node name exists in the node-list.

        Checks the list for the provided item. Will return true if the list contains that item. This is also available via the Python built-in check for list object [ contained = object in list ].
        """
        return True
    
    def list(self) -> List[Node]:
        """
        Converts the dynamic list to a concrete list of nodes.

        By default, the nodelist object is a dynamic list-type. This means that the object does not contain a persistent list, but behaves dynamically when a node is requested from it. Sometimes, a static list is preferred and this method will generate a static list of OMC::Node objects. Note, although the list is static, the objects within the list remain dynamic and refer to a node within the project.
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene
        dynamic_nodelist = scene.nodes                               #The dynamic node list.
        static_nodelist  = scene.nodes.list()                        #Covnerted the dynamic node list to a static list.
        top = scene.top                                              #The top group.
        new_node_count = 5
        for n in range(new_node_count):
        top.nodes.create( "PEG", "NewPeg_%05d"%(n) )
        print( "Dynamic Size: %s"%(len(dynamic_nodelist)) )          #Expecting that the dynamic node list contains 5 more pegs.
        print( "Static Size: %s"%(len(static_nodelist)) )
        #Another handy factor of the static list is Python's list comprehension and iteration:
        static_nodelist = scene.nodes.list()                         #Update the static list.
        for node in static_nodelist[::2]:
        print( "Every second node: %s"%(node.path) )
        for node in static_nodelist[::-1]:
        print( "Nodes backwards: %s"%(node.path) )
        ```
        """
        return [Node()]
    
    def create(self, type:str, name:str, path:str) -> Node:
        """
        [1/2] - type + name

        Creates a new node in the scene.

        Parameters
            name	- The required name of the node to be added to the group – if the name is already in use, it will be incremented with an integer.
            type	- The type of the node.
        
        Returns
            The Node object that was added to the group or scene.
        
        /anchor node_create1 Creates a node (represented by a OMC::Node object) in the scene or group, depending on the source of this nodelist. When creating a node in the scene's node list (OMC::Scene::nodes), the name expects an absolute path for the node, containing any group in which the node should be created. When creating a node in the group's node list, the name can be a name within that group, a relative path to the group or an abosolute path.

        Creating a Node:
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene
        #Create a node in the scene list.
        scene_node_list = scene.nodes
        new_group = scene_node_list.create( "GROUP", "GROUP001" )
        print( "NEW SCENE-LIST GROUP: %s"%(new_group.path) )
        #Create a node in the group list, using the newly created Group.
        group_node_list = new_group.nodes
        new_node1 = group_node_list.create( "PEG", "PEG001" )       #Note, since this node is created from the new group's object, it will be created in a path relative to it.
        print( "NEW GROUP-LIST NODE 1: %s"%(new_node1.path) )
        new_node2 = group_node_list.create( "PEG", "Top/GROUP001/PEG002" )  #This is also acceptable, since the absolute path is within the group thats being created.
        print( "NEW GROUP-LIST NODE 2: %s"%(new_node2.path) )
        try:
        new_node3 = group_node_list.create( "PEG", "Top/DIFFERENTGROUP/PEG002" )  #This is not acceptable, as the different group isn't the same as the generating group on which this was run.
        except:
        print( "This should fail! Since the group doesn't have access to the path as noted." )
        ```
        ------------------------------------------------------------------------
        [2/2] - type + path + name

        Creates a new node in the scene.

        Parameters
            type	- The type of the node.
            path	- The group at which the node is added.
            name	- The required name of the node to be added to the group – if the name is already in use, it will be incremented with an integer.
        
        Returns
            The Node object that was added to the greoup.
        
        Similar to the OMC::Node::create without path access – this is an overloaded method that provides a utility for providing a separate path and name.
        See related method.
        """
        return Node()
    
    def move(self, node:Node, x:int=0, y:int=0):
        """
        Moves an existing node to the group. Fails with an error if the move is not possible.

        Parameters
            path	- The path of the node to move into this group.
            x	- The x coordinate of the node in the node view.
            y	- The y coordinate of the node in the node view.
        
        This is used primarily in group node lists and is useful for moving a node from one group into another group.

        Moving a Node into a Group
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene
        #Create a node in the scene list.
        scene_node_list = scene.nodes
        new_group = scene_node_list.create( "GROUP", "GROUP001" )
        print( "NEW SCENE-LIST GROUP: %s"%(new_group.path) )
        new_node1 = scene_node_list.create( "PEG", "PEG001" )       #This is created in the TOP group, as its the default location for the Scene's nodelist.
        print( "NEW GROUP-LIST NODE 1: %s"%(new_node1.path) )
        #Now, lets move the newly created node into the new group.
        target_group_list = new_group.nodes                         #The new group's node list, this is the target for new_node1.
        new_node2 = target_group_list.move( new_node1 )
        print( "The node has been moved: %s"%(new_node2) )        
        try:
        print( "This will fail: %s"%(new_node1.path) )            #Note, since the original node object was moved -- it no longer retains the link to the node in the scene.
        except:                                                     #The move method will provide a new node object that links to the node[s] in the new group.
        print( "As expected, new_node1 no longer exists and is not valid, use new_node2 instead." )
        ```
        """
        return
    
    def remove(self, path, delElems:bool=False, delTVs:bool=False):
        """Removes the node at the path from the list (group, scene, ect)"""
        return
    
    def validate(self):
        return

class Node_Colour(BaseObject):
    """Represents and provides the methods for the colour of a node."""
    def __init__(self):
        super().__init__()
    
    def reset(self):
        """Resets the colour of the node back to its default value."""
        return
    
    def __str__(self):
        """Converts the node into a string."""
        return
    
    def validate(self):
        return

    @property
    def r(self) -> int:
        """Get and set the red value of the node 0-255."""
        return 1
    
    @property
    def g(self) -> int:
        """Get and set the greeb value of the node 0-255."""
        return 1
    
    @property
    def b(self) -> int:
        """Get and set the blue value of the node 0-255."""
        return 1
    
    @property
    def hex(self) -> str:
        """Get and set the hex value of the node in form #FFFFFF."""
        return ""
    
class Node_Coordinates(BaseObject):
    """
    Represents and provides the methods for the coordinates of a node in the node view.

    The node coordinates refer to the placement of the node within the node view. Each group in the node view contains its own node-graph, and the position of these nodes are dictated by the position of the node (OMC::Node::position).
    
    Aligning Nodes
    ```python
    import random
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    proj.history.begin( "Ordering Nodes" )
    horizontal_separation = 225
    vertical_separation   = 125
    generator_types = [ "READ", "COLOURCARD", "GROUP", "GRADIENT"]
    #A recursive method used to identify all generator type-nodes. We'll only keep the topmost generator found in any path.
    def recursive_collector( node, previous_collector, collector, depth ):
    if node.type.upper() in generator_types:                   #Is the node a 'generator' type? We will organize around these node types.
        if previous_collector:
        collector["generators"].remove( previous_collector )
        if not node in collector["generators"]:
        collector["generators"].append( node )
        previous_collector = node
    srcnodes = 0
    for port in node.ports_in:
        srcnode = port.source_node
        if srcnode:
        collector = recursive_collector( srcnode, previous_collector, collector, depth+1 )
        srcnodes = srcnodes + 1
    if previous_collector:
        try:
        collector["controller_count"][ previous_collector.path ] = max( srcnodes, collector["controller_count"][ previous_collector.path ] )
        except:
        collector["controller_count"][ previous_collector.path ] = srcnodes
    #Gather some information on these nodes.
    collector["x"]           = collector["x"]+node.position.x
    collector["y"]           = collector["y"]+node.position.y
    collector["maxx"]        = max( collector["maxx"], node.position.x)
    collector["count"]       = collector["count"]+1
    collector["max_effects"] = max(depth, collector["max_effects"])
    return collector
    #Align controllers above in a recursive fashion.
    def recursive_align( node, aligned ):
    tposition = node.position
    for x,port in enumerate(node.ports_in):
        srcnode = port.source_node
        if srcnode:
        srcnode.position.y = min( srcnode.position.y, tposition.y - vertical_separation )
        if not srcnode.path in aligned:
            srcnode.position.x = tposition.x + ( x * horizontal_separation )
            collector = recursive_align( srcnode, aligned )
        aligned[srcnode.path] = True
    return aligned
    #Align FX below the generators by centering them on their sources.
    def recursive_align_fx( node, aligned, generators ):
    tposition = node.position
    src_average = 0
    src_count   = 0
    for x,port in enumerate(node.ports_in):
        srcnode = port.source_node
        if srcnode:
        if not srcnode.path in aligned and not srcnode in generators:
            collector = recursive_align_fx( srcnode, aligned, generators )
        src_average = src_average + srcnode.position.x
        src_count   = src_count+1
    if not node.path in aligned:
        node.position.x = src_average/src_count
        node.position.y = tposition.y - vertical_separation
        aligned[node.path] = True
    return aligned
    display_node = scene.display
    #Working from the current display, organize around that.
    if display_node:
    #Collect the Generator Details
    collector = {"x":0, "y":0, "maxx":0, "count":0, "generators":[], "controller_count":{}, "max_effects":0 }
    collector = recursive_collector( display_node, None, collector, 0 )
    average_x = collector["x"] / collector["count"]
    average_y = collector["y"] / collector["count"]
    aligned_list = {}
    next_offset = 0
    #Align the generators.
    for x,node in enumerate( collector["generators"] ):
        node.position.x = collector["maxx"] - next_offset
        node.position.y = average_y
        next_offset = next_offset + ( max( collector["controller_count"][node.path]-1, 0) * horizontal_separation ) + horizontal_separation
        #Align the controls above the generators.
        aligned_list = recursive_align( node, aligned_list )
    display_node.position.x = average_x
    display_node.position.y = average_y + ( collector["max_effects"] * vertical_separation )
    #Align the FX below the generations
    recursive_align_fx( display_node, aligned_list, collector["generators"] )
    #Move all siblings to the display
    src_port = display_node.ports_in[0].source
    for x,destination_node in enumerate(src_port.destination_nodes):
        if not destination_node == display_node:
        destination_node.position.x = display_node.position.x - ( (x+1)*horizontal_separation/2.0 )
        destination_node.position.y = display_node.position.y
    else:
    print( "No Active Display" )
    proj.history.end()
    ```
    """
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return

    @property
    def x(self) -> int:
        """Get and set the horizontal coordinate of the node in the node view."""
        return 1
    
    @property
    def y(self) -> int:
        """Get and set the vertical coordinate of the node in the node view."""
        return 1
    
    @property
    def z(self) -> int:
        """Get and set the depth coordinate of the node in the node view."""
        return 1
    
class OutPort(Port):
    """
    Represents and provides the methods for a node's out port.

    An out port can provide multiple connections to different nodes. These connections are made through the CableList provided by OMC::OutPort::cables. The OutPort must be connected to an InPort of another node. An Outport also maintains the Transformation provided by that port with its transformation( int frame ) method and is useful for transformation-related scripts.

    Identify all Out-Ports on a Peg
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    peg = scene.nodes["Top/Peg"]                                 #Find the peg node.
    #Identify all Out-Ports on a Peg
    ports_out = peg.ports_out                                    #The out-port list for the node.
    for idx,port in enumerate(ports_out):
    destination_nodes = port.destination_nodes
    print( "Port %s :"%(idx) )
    for idx2,node in enumerate(destination_nodes):     
        print( "  %s : %s"%(idx2, node.path) )
    ```
        
    Connect Some Nodes
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    top = scene.top                                              #The top group.
    proj.history.begin( "Test Node Connection" )
    peg  = top.nodes.create( "PEG", "PEG001" )
    read = top.nodes.create( "READ", "DRAWING001" )
    #Connect the ports!
    peg.ports_out[0].link( read.ports_in[0] )
    proj.history.end()
    ```

    Get the Transformation of a Port
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    peg = scene.nodes["Top/Peg"]                                 #Find the peg node.
    #Identify all Out-Ports on a Peg
    ports_out = peg.ports_out                                    #The out-port list for the node.
    transform = ports_out[0].transformation(1)                   #The outport can provide a transformation.
    print( transform.matrix )
    ```
    """
    def __init__(self):
        super().__init__()
    
    def link(self, inPort:InPort):
        """Connect this port to another port."""
        return Cable
    
    def unlink(self, cable:Cable, port:InPort, node:Node):
        """
        [1/3] - cable

        Disconnects the provided cable object from the port.

        Returns
            True if the cable was properly disconnected.
        
        ------------------------------------------------------------------------
        [2/3] - port

        Disconnects this port from the provided port.

        Returns
            True if the cable was properly disconnected.
        
        ------------------------------------------------------------------------
        [3/3] - node

        Disconnects this port from the provided node.

        Returns
            True if the cable was properly disconnected.
        """
        return
    
    def transformation(self, frame:int):
        """Gets the transformation that is provided by the outport at the provided frame."""
        return Transformation()

    @property
    def cables(self) -> CableList:
        """Provide the list of cables connected to a port."""
        return CableList()
    
    @property
    def cables_flat(self) -> CableList:
        """Provide the list of cables connected to a port."""
        return CableList()
    
    @property
    def destinations(self) -> Port:
        """Get the destination ports that are connected to this port."""
        return Port()
    
    @property
    def destination_nodes(self) -> Node:
        """Get the destination nodes that are connected to this port."""
        return Node()
    
    @property
    def destinations_flat(self) -> Port:
        """Get the flat destination ports that are connected to this port."""
        return Port()
    
    @property
    def destination_nodes_flat(self) -> Node:
        """Get the flat destination nodes that are connected to this port."""
        return Node()

class PasteActionOptions(BaseObject):
    """Paste Actions options used in OMC::Clipboard::paste_action_template."""
    def __init__(self):
        super().__init__()
    
    @property
    def groups(self) -> bool:
        return True
        
    @property
    def effects(self) -> bool:
        return True
        
    @property
    def composites(self) -> bool:
        return True
    
class PasteOptions(BaseObject):
    """Paste options used in pasting with OMC::Clipboard."""
    def __init__(self, options):
        super().__init__()
    
    @property
    def use_paste_special(self) -> bool:
        """Enables Paste Special mode that employs special paste options."""
        return True
        
    @property
    def usePasteSpecial(self) -> bool:
        """
        
        """
        return True
        
    @property
    def extend_scene(self) -> bool:
        """
        Extends the scene based on pasted content.

        Extend the scene based on the length of the incoming pasted content. Default is false.
        """
        return True
        
    @property
    def extendScene(self) -> bool:
        return True
        
    @property
    def create_new_column(self) -> bool:
        """
        Create new columns for the pasted content. Default is false.
        """
        return True
        
    @property
    def createNewColumn(self) -> bool:
        return True
        
    @property
    def element_timing_column_mode(self) -> str:
        """
        PasteSpecial Structure value. Default value is ELEMENT_AS_ELEMENT_AND_TIMING_AS_TIMING.

        Sets the paste special elementtiming mode for calls to pasteTemplateIntoScene Acceptable strings are:

        ELEMENT_AS_ELEMENT_AND_TIMING_AS_TIMING ALL_DRWGS_AS_ELEMENTS ALL_DRWGS_LINKED_THRU_TIMING_COLS
        """
        return ""
        
    @property
    def add_remove_motion_keyframe(self) -> bool:
        """PasteSpecial Structure value. Default value is true."""
        return True
        
    @property
    def add_remove_velocity_keyframe(self) -> bool:
        """PasteSpecial Structure value. Default value is true."""
        return True
        
    @property
    def add_remove_angle_keyframe(self) -> bool:
        """PasteSpecial Structure value. Default value is true."""
        return True
        
    @property
    def add_remove_skew_keyframe(self) -> bool:
        """PasteSpecial Structure value. Default value is true."""
        return True
        
    @property
    def add_remove_scaling_keyframe(self) -> bool:
        """PasteSpecial Structure value. Default value is true."""
        return True
        
    @property
    def force_beginning_end_keyframe(self) -> bool:
        """PasteSpecial Structure value. Default value is true."""
        return True
        
    @property
    def offset_keyframes(self) -> bool:
        """PasteSpecial Structure value. Default value is false."""
        return True
        
    @property
    def replace_expression_columns(self) -> bool:
        """PasteSpecial Structure value. Default value is true."""
        return True
        
    @property
    def tv_preserve_name(self) -> bool:
        """Set to true to keep timed values names intact, even if cloned i.e. Drawing(3)."""
        return True
        
    @property
    def match_node_name(self) -> bool:
        """
        Use this when you want to paste a template and use the actual node names for matching nodes instead of basic algorithm of composition order.

        In this mode, it is important to make sure that all nodes of the template are found in the destination's group.
        """
        return True
        
    @property
    def full_transfer(self) -> bool:
        """
        Use this when you want to control the paste of all non animate attributes and all local values of a node.

        The default is true.
        """
        return True
        
    @property
    def drawing_action(self) -> str:
        """
        PasteSpecial Structure value. Default value is ADD_OR_REMOVE_EXPOSURE.

        Drawings action Acceptable Strings are: DO_NOTHING ADD_OR_REMOVE_EXPOSURE UPDATE_PIVOT
        """
        return ""
        
    @property
    def drawing_file_mode(self) -> str:
        """
        PasteSpecial Structure value. Default value is ALWAYS_CREATE if LIBRARY_PASTE_CREATE_NEW_DRAWING is set, otherwise it is ONLY_CREATE_IF_DOES_NOT_EXIST.

        Sets the drawing file mode - only used if the DrawingAction is set to ADD_OR_REMOVE_EXPOSURE Acceptable Strings are: NEVER_CREATE ONLY_CREATE_IF_DOES_NOT_EXIST ALWAYS_CREATE ALWAYS_CREATE_AND_VERSION_IF_NECESSARY REPLACE_EXISTING
        """
        return ""
        
    @property
    def keyframe_mode(self) -> bool:
        """PasteSpecial Structure value. Default value is true."""
        return True
        
    @property
    def color_palette_mode(self) -> str:
        """
        PasteSpecial Structure value. Default value is REUSE_PALETTES.

        Acceptable Strings are: DO_NOTHING REUSE_PALETTES COPY_AND_OVERWRITE_EXISTING_PALETTES COPY_AND_CREATE_NEW_PALETTES COPY_AND_CREATE_NEW_PALETTES_IN_ELEMENT_FOLDER COPY_PALETTE_AND_MERGE_COLOURS COPY_PALETTE_AND_UPDATE_COLOURS LINK_TO_ORIGINAL COPY_SCENE_PALETTE_AND_MERGE_COLOURS COPY_SCENE_PALETTE_AND_UPDATE_COLOURS
        """
        return ""
        
    @property
    def write_mode(self) -> str:
        """set the write mode. Value strings: INSERT,OVERWRITE, DO_NOTHING. Default: OVERWRITE )"""
        return ""
        
    @property
    def delete_mode(self) -> str:
        """set the delete mode. Value strings : REMOVE, EMPTY, DELETE_NOTHING. Default: DELETE_NOTHING )"""
        return ""
        
    @property
    def camera_name_transfer(self) -> bool:
        """PasteSpecial Structure value. Default value is false."""
        return True
        
    @property
    def copy_modelling_dir(self) -> bool:
        """Set to true to copy the modeling directory into the template."""
        return True
        
    @property
    def copy_scan_files(self) -> bool:
        """Set to true to copy the scan files associated to the selected drawings."""
        return True
        
    @property
    def start_frame_src(self) -> int:
        """
        When pasting an external template or local content, this functions controls the start frame of the content that will be pasted.

        The default start frame is 1, which means that it will be pasting starting from the first frame of the copied content. Set this to a value >= 1 to specific the frame to use as a starting frame. Must be using the paste special mode.
        """
        return 1
        
    @property
    def num_frame_src(self) -> int:
        """
        When pasting an external template or local content, this functions controls the number of frames of the content that will be pasted.

        The default number of frames is 0, which effectively turn off this override feature and make it paste the entire copied content length. Set this length to anything >0 to override the number of frames pasted.

        Must be using the paste special mode.
        """
        return 1
        
    @property
    def drawing_extend_exposure(self) -> bool:
        """
        Set to true to copy the modeling directory into the template.
        """
        return True
        
    @property
    def drawing_subsitution(self) -> bool:
        """Set to true to copy the scan files associated to the selected drawings."""
        return True
        
    @property
    def action_template(self) -> bool:
        """Identify if the paste is using the action-template mode."""
        return True
    
class Path3DColumn(KeyframeableColumn):
    """
    A Column type that provides an interpolated 3D point as a value.

    Generally used with Position3DAttribute, the column provides an interpolated path value with keyframes, control point positions and a velocity column.
    """
    def __init__(self):
        super().__init__()
    
    def convert_to_separate(self, conversionAlgo:str):
        """
        Converts a 3D Path to a Separate, tuple of three beziers, and select it.

        The example below converts a 3D Path to a Separate with the chosen algorithm. Then links to the Separate beziers (node.linkAttr).

        ```javascript
        function TB_ConvertToSeparate()
        {
        var conversionAlgo = "TRANSFORM_MATRIX";
        var selectedNode = selection.selectedNode(0);
        if(selectedNode == "" || node.type(selectedNode) != "READ")
            return;
        var path3dColumn = node.linkedColumn(selectedNode, "offset.attr3dpath");
        scene.beginUndoRedoAccum("Convert 3D Path to Separate with " + conversionAlgo);
        var beziers = func.convertToSeparate(path3dColumn, conversionAlgo);
        var offsetAttrType = node.getAttr(selectedNode, frame.current, "offset.separate");
        offsetAttrType.setValueAt(true, frame.current);
        if (offsetAttrType.boolValue())
        {
            node.unlinkAttr(selectedNode, "offset.x");
            node.unlinkAttr(selectedNode, "offset.y");
            node.unlinkAttr(selectedNode, "offset.z");
        }
        node.linkAttr(selectedNode, "offset.x", beziers[0]);
        node.linkAttr(selectedNode, "offset.y", beziers[1]);
        node.linkAttr(selectedNode, "offset.z", beziers[2]);
        scene.endUndoRedoAccum();
        }
        ```

        With conversionAlgo = "TRANSFORM_MATRIX" : returns a identical spline except for the frame rate, i.e. there will be a slight change on frame's positions on the spline. When using "TRANSFORM_MATRIX" the velocity information is not preserved. With conversionAlgo = "BEZIER_FITTER" : Prioritize frame rate and velocity changes over spline's integrity.

        Parameters
            conversionAlgo	: The name of the conversion method used. Either "TRANSFORM_MATRIX" or "BEZIER_FITTER".
        
        Returns
            Returns a list of the names of the resulting functions as separated beziers.
        """
        return Column()
    
    def create_point(self, frame:float, x:float, y:float, z:float, tension:float, continuity:float, bias:float):
        """
        Adds a keyframe to a 3D Path and sets the X, Y and Z value, as well as the tension, continuity and bias.

        Parameters
            frame	: Frame number for the point.
            x	: X value for the point.
            y	: Y value for the point.
            z	: Z value for the point.
            tension	: The tension value of the keyframe.
            continuity	: The continuity value of the keyframe.
            bias	: The bias value of the keyframe.
        """
        return
    
    def remove_point(self, pointIndex:int):
        """
        Used to remove either a key frame, or a control point.

        Parameters
            point	: The number of the point on the curve, from 0 to n-1, where n is the total number of points.
        """
        return
    
    def __getitem__(self, idx:int):
        """The column object is is iterable and can provide values at given frames with the list operator. The frame value can be get and set from this interface."""
        return

    @property
    def velocity_column(self) -> Column:
        """Get the velocity column of the 3D Path."""
        return Column()

class Path3DColumnValue(ColumnValue):
    """The value provided by the list[idx] operator or iterator of a Path3DColumn."""
    def __init__(self):
        super().__init__()
    
    @property
    def key(self) -> bool:
        """Defines whether or not the frame represents a key. Setting this to true will create a key."""
        return True
        
    @property
    def const(self):
        return
        
    @property
    def tension(self) -> float:
        """The tension of the keyframe at the given frame if it exists, or the previous keyframe otherwise."""
        return 1.0
        
    @property
    def continuity(self) -> float:
        """The continuity of the keyframe at the given frame if it exists, or the previous keyframe otherwise."""
        return 1.0
        
    @property
    def bias(self) -> float:
        """The bias of the keyframe at the given frame if it exists, or the previous keyframe otherwise."""
        return 1.0
        
    @property
    def keyframe_previous(self) -> BezierColumnValue:
        """The previous frame at which there is a keyframe present, this frame value object if its currently a keyframe."""
        return BezierColumnValue()

    @property
    def keyframe_next(self) -> BezierColumnValue:
        """The next frame at which there is a keyframe present. If none are present, returns none."""
        return BezierColumnValue()

class Path3DControlPoint(ControlPoint):
    """
    The 3D Path Control Point provided by a Path3DColumn.

    The 3D Path Control Point is provided by the ControlPointList from OMC::Path3DColumn::control_points.
    """
    def __init__(self):
        super().__init__()
    
    @property
    def const_segment(self) -> bool:
        """True to indicate that the point is on a constant segment, or false to indicate that the point is not on a constant segment."""
        return True
        
    @property
    def continuity(self) -> float:
        """The continuity of the curve that follows the point. One of the following values will be returned, in upper-case: SMOOTH, CORNER or STRAIGHT."""
        return 1.0
        
    @property
    def x(self) -> float:
        """The value of the specified point on the X path."""
        return 1.0
        
    @property
    def y(self) -> float:
        """The value of the specified point on the Y path."""
        return 1.0
        
    @property
    def z(self) -> float:
        """The value of the specified point on the Z path."""
        return 1.0
        
    @property
    def tension(self) -> float:
        """The tension value for the specified point on the 3D Path. Returns 0 if the current value is outside -1 and 1."""
        return 1.0
        
    @property
    def bias(self) -> float:
        """The bias value for the specified point on the 3D Path. Returns 0 if the current value is outside -1 and 1."""
        return 1.0
        
    @property
    def keyframe(self) -> bool:
        """true if the control point is also a keyframe. Catmull 3d paths can have positional control point to define the path for which the timing is given by the velocity. To convert a control point into a keyframe, remove the control point and add a keyframe."""
        return True
    
class Path3DControlPointValue(BaseObject):
    """
    The Control Point value provided by a Path3DColumn.

    The control point values provided from OMC::Path3DColumn::control_points. Used to define specific points along the path.
    """
    def __init__(self):
        super().__init__()
    
    @property
    def x(self) -> float:
        """The value of the specified point on the X path."""
        return 1.0
        
    @property
    def y(self) -> float:
        """The value of the specified point on the Y path."""
        return 1.0
        
    @property
    def z(self) -> float:
        """The value of the specified point on the Z path."""
        return 1.0

class Path3DXYZColumnValue(BaseObject):
    """
    The value provided at a frame-value object for a Path3DColumn.

    This value is provided by OMC::Path3DColumnValue::value, and provides the value as a XYZ point at a given frame.
    """
    def __init__(self):
        super().__init__()
    
    @property
    def x(self) -> float:
        """The x position of the path at the given frame."""
        return 1.0
        
    @property
    def y(self) -> float:
        """The y position of the path at the given frame."""
        return 1.0
        
    @property
    def z(self) -> float:
        """The z position of the path at the given frame."""
        return 1.0

class Point3d(BaseObject):
    """Provides a 3D Point using double values."""
    def __init__(self, x:float=0.0, y:float=0.0, z:float=0.0):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z

class Vector3d(Point3d):
    """Provides a 3D Vector using double values."""
    def __init__(self, x:float, y:float, z:float):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z

class PegNode(Node):
    """
    Represents and provides the methods for a Peg node.

    The Peg node is an animateable, transformable node that provides its transformation to other connected nodes attached to its OutPort.
    """
    def __init__(self):
        super().__init__()
    
    def matrix(self, frame:int) -> Matrix:
        """
        Get the matrix for a peg at a specific frame.

        Provides the output transformation matrix of the peg node. Note, this is not the local transformation of the peg, but the accumulated transformation of the peg and all of its applied parents.
        The transformation is a standard OMC::Matrix

        Returns
            OMC::Matrix that represents the applied transformation of the peg.

        Detail a Peg Transformation
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        peg = scene.nodes["Top/Peg"]                              #Find the peg node.
        matrix = peg.matrix( 1 )
        matrix_values = matrix.extract_parameters_3d( harmony.Point3d() )
        print( "Translation : %s"%(matrix_values[0]) )
        print( "Scale       : %s"%(matrix_values[1]) )
        print( "Rotation    : %s"%(matrix_values[2]) )
        ```
        """
        return Matrix()
    
    def set_matrix(self, frame:int, matrix:Matrix, lastKey:bool=False):
        """
        Set the matrix of a peg at a specific frame.

        The peg will set its transformation values to match the transformation that is applied by the matrix (OMC::Matrix).

        Note
        The original transformation of this peg will be discarded and the matrix will be set instead. To apply a matrix value, use OMC::PegNode::apply_matrix.
        Parameters
        frame	- The frame at which the matrix is set.
        matrix	- The matrix to set on the peg.
        lastKey	- Whether this is set on the last available key relative to the frame [true], or at the given frame [false]

        Setting a Transformation
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        peg = scene.nodes["Top/Peg"]                                 #Find the peg node.
        matrix_to_apply = harmony.Matrix( )                          #Create a matrix to apply.
        matrix_to_apply.scale( 2.0, 1.0, 1.0 )                       #Scale the matrix horizontally by 2.0
        peg.set_matrix(1.0, matrix_to_apply, False)
        ```
        """
        return
    
    def apply_matrix(self, frameOrRange, matrix:Matrix):
        """
        Apply the matrix of a peg at a specific frame or range. This results in the matrix being appended to the existing transformation.

        The peg will apply the matrix to the existing transformation already supplied by the peg.

        Note
        The original transformation of this peg is not discarded and the matrix will applied onto the existing peg's transformation.
        
        Parameters
            matrix	- the matrix to set on the peg.
            range	- supplied as a list in the form [startFrame, endFrame]


        Apply a Matrix to All Frames
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        peg = scene.nodes["Top/Peg"]                                 #Find the peg node.
        matrix_to_apply = harmony.Matrix( )                          #Create a matrix to apply.
        matrix_to_apply.scale( 2.0, 1.0, 1.0 )                       #Scale the matrix horizontally by 2.0
        peg.apply_matrix( [1, scene.frame_count], matrix_to_apply )  #Apply the matrix to all valid frames in the scene.
        ```
        """
        return
    
    def translation(self, frame:int) -> Vector3d:
        """
        Get the translation for a peg at a specific frame.

        The translation of the peg is provided as a OMC::Vector3d object.
        """
        return Vector3d()
    
    def set_translation(self, frame:int, position:Vector3d, lastKey:bool):
        """
        Set the translation of a peg at a specific frame. Sets the translation of a peg to match the vector (OMC::Vector3d) translation at a given frame.

        Note
        The translation is set as a local translation on the peg. If a global translation is preferred, the incoming matrix and camera matrix should be considered.
        
        Parameters
            frame	- The frame at which the translation will be set.
            position	- The OMC::Vector3d to apply to the peg.
            lastKey	- Whether this is set on the last available key relative to the frame [true], or at the given frame [false]


        Sets the Translation at a Given Frame
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        peg = scene.nodes["Top/Peg"]                                 #Find the peg node.
        vector_to_set = harmony.Vector3d( 2.0, 0.0, 0.0 )            #Create a vector to set.
        peg.set_translation( 1, vector_to_set, False )               #Set the vector translation on the first frame.
        ```
        """
        return
    
    def apply_translation(self, frameOrRange, position:Vector3d):
        """
        Apply the translation of a peg at a specific frame or range. This results in the translation being appended to the existing transformation.

        Applies a vector's (OMC::Vector3d) translation to the existing translation of the peg. This will apply directly to the peg's position and does not consider its global transformation.

        Note
        The translation is set as a local translation on the peg. If a global translation is preferred, the incoming matrix and camera matrix should be considered.
        
        Parameters
            range	- supplied as a list in the form [startFrame, endFrame]
            position	- the OMC::Vector3d to apply to the peg.
        
        ```python
        from ToonBoom import harmony                                     #Import the Harmony Module
        sess = harmony.session()                                         #Get access to the Harmony session, this class.
        proj = sess.project                                              #Get the active session's currently loaded project.
        scene = proj.scene                                               #Get the top scene in the project.
                                                                        
        peg = scene.nodes["Top/Peg"]                                     #Find the peg node.
                                                                        
        vector_to_apply = harmony.Vector3d( 2.0, 0.0, 0.0 )              #Create a vector to apply.
        range = [1, scene.frame_count]                                   #The range to apply, all frames in scene.
        peg.apply_translation( range, vector_to_apply )                  #Apply the vector to all valid frames in the scene.
        ```
        """
        return
    
    def scale(self, frame:int) -> Vector3d:
        """
        Get the scale for a peg at a specific frame.

        The scale of the peg is provided as a OMC::Vector3d object.
        """
        return Vector3d()
    
    def set_scale(self, frame:int, scale:Vector3d, lastKey:bool=False):
        """
        Set the scale of a peg at a specific frame.

        Sets the scale of a peg to match the vector (OMC::Vector3d) scale at a given frame.

        Parameters
            frame	- The frame at which the translation will be set.
            scale	- The OMC::Vector3d to apply to the peg.
            lastKey	- Whether this is set on the last available key relative to the frame [true], or at the given frame [false]

        Sets the Scale at a Given Frame
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        peg = scene.nodes["Top/Peg"]                                 #Find the peg node.
        vector_to_set = harmony.Vector3d( 2.0, 1.0, 1.0 )            #Create a vector to set.
        peg.set_scale( 1, vector_to_set, False )                     #Set the vector translation on the first frame.
        ```
        """
        return
    
    def apply_scale(self, frameOrRange, scale:Vector3d):
        """
        Apply the scale of a peg at a specific frame or range. This results in the scale being appended to the existing transformation.

        Applies a vector's (OMC::Vector3d) scale to the existing scale of the peg. This will apply directly to the peg's scale and does not consider its global transformation.

        Note
        The scale is set as a local translation on the peg. If a global translation is preferred, the incoming matrix and camera matrix should be considered.
        
        Parameters
            range	- supplied as a list in the form [startFrame, endFrame]
            scale	- the OMC::Vector3d to apply to the peg.
        
        ```python
        from ToonBoom import harmony                                     #Import the Harmony Module
        sess = harmony.session()                                         #Get access to the Harmony session, this class.
        proj = sess.project                                              #Get the active session's currently loaded project.
        scene = proj.scene                                               #Get the top scene in the project.
        peg = scene.nodes["Top/Peg"]                                     #Find the peg node.
        vector_to_apply = harmony.Vector3d( 2.0, 1.0, 1.0 )              #Create a vector to apply.
        range = [1, scene.frame_count]                                   #The range to apply, all frames in scene.
        peg.applyScale( range, vector_to_apply )                         #Apply the vector as a scale to all valid frames in the scene.
        ```
        """
        return
    
    def rotation(self, frame:int) -> Vector3d:
        """
        Get the rotation for a peg at a specific frame.

        The rotation is provided by a vector (OMC::Vector3d) that provides the rotation of the peg on each available axis in 3D.
        """
        return Vector3d()
    
    def set_rotation(self, frame:int, rotation, lastKey:bool=False):
        """
        Set the rotation of a peg at a specific frame.

        Sets the rotation of a peg to match the vector (OMC::Vector3d) rotation at a given frame, provided as a vector of degrees for each angle on the axis.

        Parameters
            frame	- The frame at which the translation will be set.
            rotation	- The OMC::Vector3d to apply to the peg.
            lastKey	- Whether this is set on the last available key relative to the frame [true], or at the given frame [false]

        Sets the Rotation at a Given Frame
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        peg = scene.nodes["Top/Peg"]                                 #Find the peg node.
        vector_to_set = harmony.Vector3d( 0.0, 0.0, 45.0 )           #Create a vector to set.
        peg.set_rotation( 1, vector_to_set, False )                  #Set the vector translation on the first frame.
        ```
        """
        return
    
    def apply_rotation(self, frameOrRange, rotatio:Vector3d):
        """
        Apply the rotation of a peg at a specific frame or range. This results in the rotation being appended to the existing transformation.

        Applies a vector's (OMC::Vector3d) rotation to the existing rotation of the peg.

        Parameters
            range	- Supplied as a list in the form [startFrame, endFrame]
            rotation	- The OMC::Vector3d to apply to the peg.

        Apply Rotation
        ```python
        from ToonBoom import harmony                                     #Import the Harmony Module
        sess = harmony.session()                                         #Get access to the Harmony session, this class.
        proj = sess.project                                              #Get the active session's currently loaded project.
        scene = proj.scene                                               #Get the top scene in the project.
        peg = scene.nodes["Top/Peg"]                                     #Find the peg node.
        vector_to_apply = harmony.Vector3d( 0.0, 0.0, 4.0 )              #Create a vector to apply.
        range = [1, scene.frame_count]                                   #The range to apply, all frames in scene.
        peg.apply_rotation( range, vector_to_apply )                     #Apply the vector as a rotation to all valid frames in the scene.
        ```
        """
        return
    
    def skew(self, frame:int) -> float:
        """
        Get the skew for a peg at a specific frame.

        Provides the skew applied by the peg at a given frame. The skew is provided as a number value in degrees on the skewed axis.
        """
        return
    
    def set_skew(self, frame:int, skewValue:float, lastKey:bool=False):
        """
        Set the skew of a peg at a specific frame.

        Sets the local skew applied by the peg for a given frame.

        Parameters
            frame	- The frame at which the translation will be set.
            skewValue	- The skew to apply to the peg.
            lastKey	- Whether this is set on the last available key relative to the frame [true], or at the given frame [false]

        Sets the Skew at a Given Frame
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        peg = scene.nodes["Top/Peg"]                                 #Find the peg node.
        peg.set_skew( 1, 45, False )                                #Set the skew on the first frame.
        ```
        """
        return
    
    def apply_skew(self, frameOrRange, skewValue:float):
        """
        Apply the skew of a peg at a specific frame or range. This results in the skew being appended to the existing transformation.

        Applies a skew to the transformation over the frame range provided. The original skew is kept and the new value is applied onto that.

        Parameters
            range	- Supplied as a list in the form [startFrame, endFrame]
            skew	- The OMC::Vector3d to apply to the peg.

        Apply Skew
        ```python
        from ToonBoom import harmony                                     #Import the Harmony Module
        sess = harmony.session()                                         #Get access to the Harmony session, this class.
        proj = sess.project                                              #Get the active session's currently loaded project.
        scene = proj.scene                                               #Get the top scene in the project.
        peg = scene.nodes["Top/Peg"]                                     #Find the peg node.
        range = [1, scene.frame_count]                                   #The range to apply, all frames in scene.
        peg.apply_skew( range, 45 )                                      #Apply the skew to all valid frames in the scene.
        ```
        """
        return
    
    def pivot(self, frame:int, apply_element_pivots:bool=False):
        """
        Get the pivot at the given frame.

        Provides the pivot of a PegNode as a Vector3d object. The pivot is generally static on Peg, but can change from frame to frame when the peg (or drawing) is set to different pivot modes.
        
        Parameters
            frame	- The frame at which the matrix is retrieved.
            apply_element_pivots	- Whether to consider the attached element's influence on the peg's pviot [true] or not.

        Get a Peg's Pivot
        ```python
        from ToonBoom import harmony                                     #Import the Harmony Module
        sess = harmony.session()                                         #Get access to the Harmony session, this class.
        proj = sess.project                                              #Get the active session's currently loaded project.
        scene = proj.scene                                               #Get the top scene in the project.
        peg = scene.nodes["Top/Peg"]                                     #Find the peg node.
        frame = 1
        pivot = peg.pivot( frame, False )
        print( "Pivot at frame %s : %s %s %s"%(frame, pivot.x, pivot.y, pivot.z) )
        ```
        """
        return
    
    def set_pivot(self, frame:int, position:Vector3d, compensate_for_elements:int=True):
        """
        Set the pivot of a peg at a specific frame.

        Sets the pivot on a peg at a given frame. Generally, a peg does not provide an animateable pivot– but the pivot may need to compensate for the elements at a given frame.

        Parameters
            frame	- The frame at which the matrix is set.
            position	- The pivot position to which the peg will be set; provided as a OMC::Vector3d object.
            compensate_for_elements	- Bool defining whether the pivot should be set in a way that compensates for the attached elements and their pivot modes.

        Set a Peg's Pivot
        ```python
        from ToonBoom import harmony                                     #Import the Harmony Module
        sess = harmony.session()                                         #Get access to the Harmony session, this class.
        proj = sess.project                                              #Get the active session's currently loaded project.
        scene = proj.scene                                               #Get the top scene in the project.
        peg = scene.nodes["Top/Peg"]                                     #Find the peg node.
        frame = 1
        old_pivot = peg.pivot( frame, False )
        print( "Pivot at frame %s : %s %s %s"%(frame, pivot.x, pivot.y, pivot.z) )
        new_pivot_to_set = harmony.Vector3d( 1.0, 2.0, 0.0 )             #The new pivot object we'll use...
        try:
        peg.set_pivot( frame, new_pivot_to_set, False )                  #Set the pivot at frame 1
        new_pivot = peg.pivot( frame, False )                            #Get the new_pivot, for demo . . . unnecessary, as an error would have been throw if failed.
        
        #Print it for demo-purposes.
        print( "New Pivot at frame %s : %s %s %s"%(frame, new_pivot.x, new_pivot.y, new_pivot.z) )
        except:
        print( "Failed to set the Pivot." )
        ```
        """
        return

class Point2d(BaseObject):
    """Provides a 2D Point using double values."""
    def __init__(self, x:float=0.0, y:float=0.0):
        super().__init__()
        self.x = x
        self.y = y

class Position2DAttribute(Attribute):
    """
    The Position2D attribute wrapper.

    This object wraps a Position2D Attribute, which provides the 2D positional information.
    """
    def __init__(self):
        super().__init__()
    
    def localvalue(self) -> Point2d:
        """
        Get the attribute's localvalue as a OMC::Point2d value.

        Provides the localvalue as a OMC::Point2d value. The local value is the non-animateable value of an attribute when no column is present. If the attribute can be linked and has a column linked to it, the value at a frame is provided by the column and the local value is ignored.

        Note
        Its generally better to reference the value over the localvalue. When no column is present, the value will also provide the localvalue – this is not true in reverse, if a column is present, the localvalue will still reference the ignored localvalue. Non-animateable attributes that cannot be linked will only provide the localvalue.


        Retrieve a OMC::Point2d Localvalue
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Transformation-Limit"]               #Find the Transformation-Limit node, as it contains a 2D position attribute.
        point2d_attribute_keyword = "POS"                            #The path to a OMC::Point2d attribute
        attribute = node.attributes[point2d_attribute_keyword]       #Get the attribute by name
        if attribute:
        current_value = attribute.localvalue()                     #Get the attribute's localvalue.
        #Show the localvalue of the attribute.
        print( "LOCALVALUE: %s %s"%( current_value.x, current_value.y ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(point2d_attribute_keyword) )
        ```
        """
        return Point2d()
    
    def value(self, frame:int) -> Point2d:
        """
        Get the attribute's value as a OMC::Point2d value at a given frame.

        Provides the value as a OMC::Point2d value. If the attribute can be linked and has a column linked to it, the value at a frame is provided by the column and the local value is ignored.

        Retrieve a OMC::Point2d Value
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Transformation-Limit"]               #Find the Transformation-Limit node, as it contains a 2D position attribute.
        point2d_attribute_keyword = "POS"                            #The path to a OMC::Point2d attribute
        attribute = node.attributes[point2d_attribute_keyword]       #Get the attribute by name
        if attribute:
        at_frame = 1
        current_value = attribute.value(at_frame)                       #Get the attribute's value at frame 1
        #Show the value of the attribute.
        print( "VALUE AT FRAME %s : %s %s"%( at_frame, current_value.x, current_value.y ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(point2d_attribute_keyword) )
        ```
        """
        return Point2d()
    
    def set_localvalue(self, value:Point2d):
        """
        Sets the attribute's local value as a OMC::Point2d value.

        Sets the local value of the attribute to the provided OMC::Point2d value. The local value is the non-animateable value of an attribute when no column is present. If the attribute can be linked and has a column linked to it, the value at a frame is provided by the column and the local value is ignored.

        Note
        Its generally better to reference the value over the localvalue. When no column is present, the value will also provide the localvalue – this is not true in reverse, if a column is present, the localvalue will still reference the ignored localvalue. Non-animateable attributes that cannot be linked will only provide the localvalue.
        
        Parameters
            value	- the OMC::Point2d value to which the attribute should be set.


        Set a OMC::Color Localvalue
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        import random
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Transformation-Limit"]               #Find the Transformation-Limit node, as it contains a 2D position attribute.
        point2d_attribute_keyword = "POS"                            #The path to a OMC::Point2d attribute
        attribute = node.attributes[point2d_attribute_keyword]       #Get the attribute by name
        if attribute:
        current_value = attribute.localvalue()                     #Get the attribute's localvalue.
        #Show the current localvalue of the attribute.
        print( "CURRENT LOCALVALUE: %s"%( current_value ) )
        new_value = harmony.Point2d( random.uniform( -20.0, 20.0 ), random.uniform( -20.0, 20.0 ) )
        attribute.set_localvalue( new_value )                      #Set the attribute's local value to the new value
        new_value = attribute.localvalue()                         #Get the attribute's new localvalue, to check it for debug/example purposes
        print( "NEW LOCALVALUE: %s %s"%( new_value.x, new_value.y ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(point2d_attribute_keyword) )
        ```
        """
        return
    
    def set_value(self, frame:int, Point2d:Point2d, adjustLastKeyframe=False):
        """
        Set the attribute's value as a OMC::Point2d value at a given frame.

        Sets the value of the attribute to the provided OMC::Point2d value at the given frame. If the attribute can be linked and has a column linked to it, the value is set on the column – otherwise, it is set on the localvalue of the attribute.

        Note
        If no column is present, setting an animateable column's value on the attribute will result in the creation of a new column.
        
        Parameters
            frame	- the frame at which the attribute is set.
            value	- the OMC::Point2d value to which the attribute should be set.


        Set a OMC::Point2d Value at a Frame
        ```python
        import random
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Transformation-Limit"]               #Find the Transformation-Limit node, as it contains a 2D position attribute.
        point2d_attribute_keyword = "POS"                            #The path to a OMC::Point2d attribute
        attribute = node.attributes[point2d_attribute_keyword]       #Get the attribute by name
        if attribute:
        at_frame = 1
        current_value = attribute.value( at_frame )                #Get the attribute's value.
        #Show the current localvalue of the attribute.
        print( "CURRENT VALUE AT %s : %s"%( at_frame, current_value ) )
        new_value = harmony.Point2d( random.uniform( -20.0, 20.0 ), random.uniform( -20.0, 20.0 ) )
        attribute.set_value( at_frame, new_value )                                                      #Set the attribute's local value to the new value
        new_value = attribute.value( at_frame )                                                         #Get the attribute's new localvalue, to check it for debug/example purposes
        print( "NEW VALUE AT %s : %s"%( at_frame, new_value ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(point2d_attribute_keyword) )
        ```
        """
        return
    
    def offset_value(self, frameOrRange, Point2d:Point2d):
        """
        Offsets the attribute's value at a given frame or frame range.

        Provided a OMC::Point2d object, will offset the existing value (either the animated value, or local value if none exists) by the color argument's value.

        Parameters
            frameOrRange	- A frame range provided by a list in form [startFrame, endFrame]
            value	- The OMC::Colour object to by which the attribute is offset.

        Offset a Point2d Attribute
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Transformation-Limit"]               #Find the Transformation-Limit node, as it contains a 2D position attribute.
        point2d_attribute_keyword = "POS"                            #The path to a OMC::Point2d attribute
        attribute = node.attributes[point2d_attribute_keyword]       #Get the attribute by name
        if attribute:
        at_frame = 1
        current_value = attribute.value( at_frame )                #Get the attribute's value.
        #Show the current localvalue of the attribute.
        print( "CURRENT VALUE AT %s : %s"%( at_frame, current_value ) )
        new_value = harmony.Point2d( random.uniform( -20.0, 20.0 ), random.uniform( -20.0, 20.0 ) )
        range = [ at_frame, scene.frame_count ]                    #The range will be from at_frame, to the last frame of the scene.
        attribute.offset_value( range, new_value )                 #Offset the attribute's value by the provided value
        new_value = attribute.value( at_frame )                    #Get the attribute's new localvalue, to check it for debug/example purposes
        print( "NEW VALUE AT %s : %s"%( at_frame, new_value ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(point2d_attribute_keyword) )
        ```
        """
        return
    
    def reset_localvalue(self):
        """
        Reset the attribute's localvalue to the default value.

        The value of an attribute has a default value when the node is initially created. This method will reset the localvalue to its initial default value.
        """
        return
    
    def reset_value(self, frame:int):
        """
        Reset the attribute to the default value.

        The value of an attribute has a default value when the node is initially created. This method will reset the value to its initial default value at the provided frame.

        Parameters
            frame	- the frame at which the attribute is reset.
        """
        return
    
    @property
    def default(self) -> Point2d:
        """
        Get the default value of the attribute.

        Provides the default value of the attribute – this is the value that the attribute will use when it is reset.
        """
        return Point2d()
    
class Position3DAttribute(Attribute):
    """
    The Position3D attribute wrapper.

    This object wraps a Position3D Attribute, which provides the 3D positional information.
    """
    def __init__(self):
        super().__init__()
    
    def localvalue(self) -> Point3d:
        """
        Get the attribute's localvalue as a OMC::Point3d value.

        Provides the localvalue as a OMC::Point3d value. The local value is the non-animateable value of an attribute when no column is present. If the attribute can be linked and has a column linked to it, the value at a frame is provided by the column and the local value is ignored.

        Note
        Its generally better to reference the value over the localvalue. When no column is present, the value will also provide the localvalue – this is not true in reverse, if a column is present, the localvalue will still reference the ignored localvalue. Non-animateable attributes that cannot be linked will only provide the localvalue.


        Retrieve a OMC::Point3d Localvalue
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Peg"]                                #Find the peg, as it contains a 3D position attribute.
        point3d_attribute_keyword = "POSITION"                       #The path to a OMC::Point3d attribute
        attribute = node.attributes[point3d_attribute_keyword]       #Get the attribute by name
        if attribute:
        current_value = attribute.localvalue()                     #Get the attribute's localvalue.
        #Show the localvalue of the attribute.
        print( "LOCALVALUE: %s %s %s"%( current_value.x, current_value.y, current_value.z ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(point3d_attribute_keyword) )
        ```
        """
        return Point3d()
    
    def value(self, frame:int) -> Point3d:
        """
        Get the attribute's value as a OMC::Point3d value at a given frame.

        Provides the value as a OMC::Point3d value. If the attribute can be linked and has a column linked to it, the value at a frame is provided by the column and the local value is ignored.


        Retrieve a OMC::Point3d Value
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Peg"]                                #Find the peg, as it contains a 3D position attribute.
        point3d_attribute_keyword = "POSITION"                       #The path to a OMC::Point3d attribute
        attribute = node.attributes[point3d_attribute_keyword]       #Get the attribute by name
        if attribute:
        at_frame = 1
        current_value = attribute.value(at_frame)                       #Get the attribute's value at frame 1
        #Show the value of the attribute.
        print( "VALUE AT FRAME %s : %s %s %s"%( at_frame, current_value.x, current_value.y, current_value.z ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(point3d_attribute_keyword) )
        ```
        """
        return Point3d()
    
    def set_localvalue(self, value:Point3d):
        """
        Sets the attribute's local value as a OMC::Point3d value.

        Sets the local value of the attribute to the provided OMC::Point3d value. The local value is the non-animateable value of an attribute when no column is present. If the attribute can be linked and has a column linked to it, the value at a frame is provided by the column and the local value is ignored.

        Note
        Its generally better to reference the value over the localvalue. When no column is present, the value will also provide the localvalue – this is not true in reverse, if a column is present, the localvalue will still reference the ignored localvalue. Non-animateable attributes that cannot be linked will only provide the localvalue.
        
        Parameters
            value	- the OMC::Point3d value to which the attribute should be set.


        Set a OMC::Color Localvalue
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        import random
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Peg"]                                #Find the peg, as it contains a 3D position attribute.
        point3d_attribute_keyword = "POSITION"                       #The path to a OMC::Point3d attribute
        attribute = node.attributes[point3d_attribute_keyword]       #Get the attribute by name
        if attribute:
        current_value = attribute.localvalue()                     #Get the attribute's localvalue.
        #Show the current localvalue of the attribute.
        print( "CURRENT LOCALVALUE: %s"%( current_value ) )
        new_value = harmony.Point3d( random.uniform( -20.0, 20.0 ), random.uniform( -20.0, 20.0 ), random.uniform( -20.0, 20.0 ) )
        attribute.set_localvalue( new_value )                      #Set the attribute's local value to the new value
        new_value = attribute.localvalue()                         #Get the attribute's new localvalue, to check it for debug/example purposes
        print( "NEW LOCALVALUE: %s %s %s"%( new_value.x, new_value.y, new_value.z ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(point3d_attribute_keyword) )
        ```
        """
        return
    
    def set_value(self, frame:int, Point3d:Point3d, adjustLastKeyframe=False):
        """
        Set the attribute's value as a OMC::Point3d value at a given frame.

        Sets the value of the attribute to the provided OMC::Point3d value at the given frame. If the attribute can be linked and has a column linked to it, the value is set on the column – otherwise, it is set on the localvalue of the attribute.

        Note
        If no column is present, setting an animateable column's value on the attribute will result in the creation of a new column.
        
        Parameters
            frame	- the frame at which the attribute is set.
            value	- the OMC::Point3d value to which the attribute should be set.


        Set a OMC::Point3d Value at a Frame
        ```python
        import random
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Peg"]                                #Find the peg, as it contains a 3D position attribute.
        point3d_attribute_keyword = "POSITION"                       #The path to a OMC::Point3d attribute
        attribute = node.attributes[point3d_attribute_keyword]       #Get the attribute by name
        if attribute:
        at_frame = 1
        current_value = attribute.value( at_frame )                #Get the attribute's value.
        #Show the current localvalue of the attribute.
        print( "CURRENT VALUE AT %s : %s"%( at_frame, current_value ) )
        new_value = harmony.Point3d( random.uniform( -20.0, 20.0 ), random.uniform( -20.0, 20.0 ), random.uniform( -20.0, 20.0 ) )
        attribute.set_value( at_frame, new_value )                                                      #Set the attribute's local value to the new value
        new_value = attribute.value( at_frame )                                                         #Get the attribute's new localvalue, to check it for debug/example purposes
        print( "NEW VALUE AT %s : %s"%( at_frame, new_value ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(point3d_attribute_keyword) )
        ```
        """
        return
    
    def offset_value(self, frameOrRange, Point3d:Point3d):
        """
        Offsets the attribute's value at a given frame or frame range.

        Provided a OMC::Point3d object, will offset the existing value (either the animated value, or local value if none exists) by the color argument's value.

        Parameters
            frameOrRange	- A frame range provided by a list in form [startFrame, endFrame]
            value	- The OMC::Colour object to by which the attribute is offset.

        Offset a Point3d Attribute
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        node = scene.nodes["Top/Peg"]                                #Find the peg, as it contains a 3D position attribute.
        point3d_attribute_keyword = "POSITION"                       #The path to a OMC::Point3d attribute
        attribute = node.attributes[point3d_attribute_keyword]       #Get the attribute by name
        if attribute:
        at_frame = 1
        current_value = attribute.value( at_frame )                #Get the attribute's value.
        #Show the current localvalue of the attribute.
        print( "CURRENT VALUE AT %s : %s"%( at_frame, current_value ) )
        new_value = harmony.Point3d( random.uniform( -20.0, 20.0 ), random.uniform( -20.0, 20.0 ), random.uniform( -20.0, 20.0 ) )
        range = [ at_frame, scene.frame_count ]                    #The range will be from at_frame, to the last frame of the scene.
        attribute.offset_value( range, new_value )                 #Offset the attribute's value by the provided value
        new_value = attribute.value( at_frame )                    #Get the attribute's new localvalue, to check it for debug/example purposes
        print( "NEW VALUE AT %s : %s"%( at_frame, new_value ) )
        else:
        print( "Unable to find attribute by keyword: %s"%(point3d_attribute_keyword) )
        ```
        """
        return
    
    def reset_localvalue(self):
        """
        Reset the attribute's localvalue to the default value.

        The value of an attribute has a default value when the node is initially created. This method will reset the localvalue to its initial default value.
        """
        return
    
    def reset_value(self, frame:int):
        """
        Reset the attribute to the default value.

        The value of an attribute has a default value when the node is initially created. This method will reset the value to its initial default value at the provided frame.

        Parameters
            frame	- the frame at which the attribute is reset.
        """
        return
    
    @property
    def default(self) -> Point3d:
        """
        Get the default value of the attribute.

        Provides the default value of the attribute – this is the value that the attribute will use when it is reset.
        """
        return Point3d()

class PreferencePair(BaseObject):
    """
    The key,value pair of an item in the application's preferences.

    The map[QString] operator for the OMC::Preferences object provides a PreferencePair that is used to modify the preference value.
    """
    def __init__(self):
        super().__init__()
    
    def reset(self) -> bool:
        return True
    
    @property
    def key(self) -> str:
        """Gets the preference's key value."""
        return ""
        
    @property
    def type(self) -> str:
        """Gets the preference's type."""
        return ""
        
    @property
    def value(self):
        """Gets the preference's value."""
        return
    
class ProjectNamedResolution(BaseObject):
    """A named resolution object, containing the properties of a saved resolution."""
    def __init__(self):
        super().__init__()

    @property
    def x(self) -> int:
        """Get the X value of the named resolution."""
        return 1
    
    @property
    def y(self) -> int:
        """Get the Y value of the named resolution."""
        return 1
    
    @property
    def fov(self) -> float:
        """Get the fov value of the named resolution."""
        return 1.0
    
    @property
    def name(self) -> str:
        """Get the name value of the named resolution."""
        return ""
    
    @property
    def projection(self) -> str:
        """Get the project-type of the named resolution."""
        return ""
    
class ProjectResolution(BaseObject):
    """The current resolution of the scene."""
    def __init__(self):
        super().__init__()

    @property
    def x(self) -> int:
        """Get/Set the X value of the current preview resolution."""
        return 1
    
    @property
    def y(self) -> int:
        """Get/Set the Y value of the current preview resolution."""
        return 1
    
    @property
    def default_name(self) -> str:
        """
        The default resolution name, if one is being used.

        The default_name is used to get the preset name of the project's resolution, or set it to a named resolution.

        Setting the Project to a Named Resolution
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the current project.
        resolution = proj.resolution                                 #The resolution object.
        resolution.default_name = "HDTV"                             #Set the resolution to the HDTV preset.
        ```
        """
        return ""
    
    @property
    def default_FOV(self) -> float:
        """Get the default FOV value."""
        return 1.0
    
    @property
    def names(self) -> ProjectNamedResolution:
        """
        Get/Set the Y value of the default resolution.

        Named resolutions are preset resolutions available within the application. This is useful for applying standard resolutions to the scene.
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the current project.
        resolution = proj.resolution                                 #The resolution object.
        named_resolutions = resolution.names
        for named_resolution in named_resolutions:
        this_resolution = named_resolutions[named_resolution]
        print( "Resolution Name: %s"%(named_resolution) )
        print( "   Resolution: %s %s (%s) %s "%(this_resolution.x, this_resolution.y, this_resolution.fov, this_resolution.projection) )
        ```
        """
        return ProjectNamedResolution
    
class PythonGILScope():
    def __init__(self):
        super().__init__()
    
    def __getitem__(self):
        return PythonGILScope()
    
    def release(self):
        return

class PythonThreadHelper():
    def __init__(self):
        super().__init__()
    
    def mainThreadIncrease(self):
        return
    
    def mainThreadDecrease(self):
        return
    
    def helper(self):
        return PythonThreadHelper()
    
    def getScopeLockScope(self):
        return
    
    def getThreadUnlockScopeScope(self):
        return
    
class PythonThreadScope():
    def __init__(self):
        super().__init__()
    
    def __getitem__(self):
        return PythonThreadScope()
    
    def release(self):
        return

class QIntList(tuple):
    def __init__(self):
        super().__init__()

class QuaternionColumn(Path3DColumn):
    """
    Represents and provides the methods for a quaternion path column in a scene.

    The quaternion column is a column type that provides a quaternion rotation value. For more information see OMC::Path3DColumn.
    """
    def __init__(self):
        super().__init__()

class ReadNode(Node):
    """
    Represents and provides the methods for a Read (Drawing) node.

    The Read node provides an image from an attached Element source as either a bitmap element or a vector element (provided as a OMC::DrawingElement).

    At the moment, the read node is a placeholder node that will be extended in future DOM versions. Standard attribute access is available already.
    """
    def __init__(self):
        super().__init__()
    
class SceneAspect(BaseObject):
    """
    The aspect ratio of the cells in the scene grid.

    See OMC::Scene::aspect for more information.
    """
    def __init__(self):
        super().__init__()
    
    @property
    def x(self) -> float:
        """Get/set the X value of the aspect ratio of the cells in the scene grid."""
        return 1.0
        
    @property
    def y(self) -> float:
        """Get/set the Y value of the aspect ratio of the cells in the scene grid."""
        return 1.0

class SceneCenter(BaseObject):
    """
    The center coordinates of the scene.

    See OMC::Scene::center for more information.
    """
    def __init__(self):
        super().__init__()
    
    @property
    def x(self) -> float:
        """Get/Set the X value of the centre coordinate of the scene grid."""
        return 1.0
        
    @property
    def y(self) -> float:
        """Get/Set the number of units in the Y axis of the scene grid."""
        return 1.0

class SceneUnitConverter(BaseObject):
    """
    A converter utility for changing between OGL units and scene units.

    Provided by the OMC::Scene::unit_converter.

    Scenes within Harmony use field units, but most graphical operations use OpenGL units. Depending on the function and the context, conversion between these units are necessary and are done with the unit_converter. This converter (OMC::SceneUnitConverter) will use the scene's metric information to convert between the units.

    Conversion from OGL to Field Units
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    unit_converter = scene.unit_converter                        #The unit converter for this scene.
    open_gl_point = harmony.Point3d( 1.0, 1.0, 1.0 )             #A Point3D object in 'OpenGL' units.
    field_point   = unit_converter.to_field( open_gl_point )     #Convert it.
    #Print the converted field units.
    print( "Field Units: %s %s %s"%(field_point.x, field_point.y, field_point.z) )
    ```
    """
    def __init__(self):
        super().__init__()
    
    def to_ogl(self, value:float, axis:str, val:Point3d) -> float:
        """
        [1/2] - value + axis

        Converts a 2D position on an axis from fields in the worldspace to OGL.
        ------------------------------------------------------------------------
        [2/2] - val

        Converts a 2D point from fields in the worldspace to OGL.
        """
        return 1.0
    
    def to_field(self, value:float, axis:str, val:Point3d) -> float:
        """
        [1/2] - value + axis

        Converts a 2D position on an axis from OGL to fields in the worldspace.
        ------------------------------------------------------------------------
        [2/2] - val

        Converts a 2D point from OGL to fields in the worldpspace.
        """
        return 1.0

class SceneUnits(BaseObject):
    """
    The units in the scene .

    See OMC::Scene::units for more information.
    """
    def __init__(self):
        super().__init__()
    
    @property
    def x(self) -> float:
        """Get/Set the number of units in the X axis of the scene grid."""
        return 1.0
        
    @property
    def y(self) -> float:
        """Get/Set the number of units in the Y axis of the scene grid."""
        return 1.0

    @property
    def z(self) -> float:
        """Get/Set the number of units in the Z axis of the scene grid."""
        return 1.0

class Scene(BaseObject):
    """
    A scene within the project in the application.

    The project provides access to functions and properties related to the active project within the instance of Harmony.
    """
    def __init__(self):
        super().__init__()
    
    def frame_insert(self, atFrame:int, nbFrames:int, options:FrameOptions) -> bool:
        """
        Inserts frames at the selected frame number.

        atFrame = 0 -> insert before first frame.
        atFrame = n -> insert after frame n.
        atFrame = scene_object.frame_count.
        
        Parameters
            atFrame	- The frame number at which the frames will be inserted. Frames are inserted after the frame indicated. Use 0 to insert frames before the first frame.
            nbFrames	- The number of frames to insert
            options	- This optional parameter should be an object with the desired behaviours for when the frames are inserted. See OMC::FrameOptions for further information on options.

        Add 10 Frames at the start of the scene:
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        scene.frame_insert( 0, 10, harmony.FrameOptions(True, True) )  #Insert the frames, with FrameOptions( ripple_markers = True, extend_exposure = True)
        #Content will now be pushed out 10 frames from before the starting frame of the scene.
        ```

        Returns
            True if the number of frames given is valid.
        """
        return True
    
    def frame_remove(self, atFrame:int, nbFrames:int, options:FrameOptions) -> bool:
        """
        Deletes frames starting from the selected frame number.

        atFrame = 0 -> delete at the beginning atFrame = n -> delete frames following the nth frame atFrame = Application.frame.nbFrames() -> won't delete anything

        Parameters
            atFrame	The frame number at which the frames will be removed. Frames are removed after the frame indicated. Use 0 to remove frames before the first frame.
            nbFrames	The number of frames to remove
            options	This optional parameter should be an object with the desired behaviours for when the frames are removed. See OMC::FrameOptions for further information on options.

        Remove 10 Frames at the start of the scene:
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        scene.frame_remove( 1, 10, harmony.FrameOptions(True, True) )  #Remove the frames, with FrameOptions( ripple_markers = True, extend_exposure = True)
        #Content will now be pulled back10 frames from before the starting frame of the scene.
        ```
        """
        return True
    
    @property
    def aspect(self) -> SceneAspect:
        """
        Get the aspect ratio of the scene.

        The aspect ratio is provided as an object (OMC::SceneAspect) that provides properties related to the aspect ratio of the scene.
        """
        return SceneAspect()
        
    @property
    def units(self) -> SceneUnits:
        """
        Get the number of units of the scene.

        The units are provided as an object (OMC::SceneUnits) that provides properties related to the units of the scene.
        """
        return SceneUnits()
        
    @property
    def center(self) -> SceneCenter:
        """
        Get the center coordinates of the scene.

        The center coordinates of the scene, provided as a read/write object (OMC::SceneCenter).
        """
        return SceneCenter()
        
    @property
    def name(self) -> str:
        """Get/set the scene's name."""
        return ""
        
    @property
    def framerate(self) -> float:
        """
        Get/set the framerate of the scene.

        Change the Scene's framerate
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        scene.framerate = 24000.0/1001.0                             #Set the framerate to 24P NTSC
        ```
        """
        return 1.0
        
    @property
    def vector_texture_pixel_density(self) -> float:
        """
        Get/set the default texture pixel density for new Vector Drawings.

        The vector texture pixel density is the ratio used for pixel density in textures being applied to vector shapes.
        """
        return 1.0
        
    @property
    def bitmap_texture_pixel_density(self) -> float:
        """
        Get/set the default texture pixel density for new bitmap Drawings.

        The bitmap texture pixel density is the ratio used for pixel density in bitmap layers.
        """
        return 1.0
        
    @property
    def frame_count(self) -> int:
        """
        Get/set the frame count of the scene.

        The number of frames in a scene. This value can be changed – frames changes will be applied at the end of the scene. Frames can be added or removed more specifically with OMC::Scene::frame_insert and OMC::Scene::frame_remove.


        Change the Scene's frame length
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        scene.frame_count = 10                                       #Change the frame count to 10.
        ```
        """
        return 1
        
    @property
    def frame_start(self) -> int:
        """
        Get/set the start-frame of the scene.

        The frame start is the temporary frame start (in) position of the scene and will be where the playhead starts and restarts at loop.

        Change the frame_start to 10:
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        scene.frame_start = 10
        ```
        """
        return 1
        
    @property
    def frame_stop(self) -> int:
        """
        Get/set the stop-frame of the scene.

        The frame stop is the temporary frame stop (out) position of the scene and will be where the playhead stops and where it will loop when enabled.

        Change the frame_stop to 10:
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        scene.frame_stop = 15
        ```
        """
        return 1
        
    @property
    def colorspace(self) -> str:
        """
        Get/set the colorspace of the scene.

        The colorspace name is provided and can be set as a value. In order to get available colorspaces, see OMC::Scene::colorspaces.

        Change the colorspace:
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        print( "Color Space: %s"%(scene.colorspace) )                #Print the current colorspace.
        scene.colorspace = "Rec.709"
        print( "Color Space: %s"%(scene.colorspace) )                #Expected result: "Color Space: Rec.709"
        ```
        """
        return ""
        
    @property
    def colorspaces(self) -> List[str]:
        """
        Get list of available colorspace names.

        The available colorspaces in the application. These colorspaces are extended and defined in a resource file.

        Print available colorspaces:
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        for colorspace in scene.colorspaces:
        print( "Colour Space Name: %s"%(colorspace) )              #Print the colorspace names.
        ```
        """
        return [""]
        
    @property
    def camera(self) -> CameraNode:
        """
        Get/set the camera node object for the scene.

        Provides the OMC::CameraNode object that represents the currently active camera in the scene.

        Identify the Camera Node:
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        camera = scene.camera
        if not camera:
        print( "No camera is currently set." )
        else:
        print( "Current Camera: %s"%(camera.path) )
        ```

        Set the Camera Node to the first identified camera:
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        for node in scene.nodes:
        if( node.type.upper() == "CAMERA" ):
            scene.camera = node
            print( "Set the Camera: %s"%(node.path) )
            break
        ```
        """
        return CameraNode()
        
    @property
    def camera_path(self) -> str:
        """
        Get/set the camera's name being used in the scene.

        Similar to OMC::Scene::camera – but provides the string representing the path to the camera node of the scene.
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        print( "Current Camera: %s"%(scene.camera_path) )            #Print the camera path.
        ```
        """
        return ""
        
    @property
    def unit_converter(self) -> SceneUnitConverter:
        """
        The tool used for converting between OGL and scene spaces.

        Scenes within Harmony use field units, but most graphical operations use OpenGL units. Depending on the function and the context, conversion between these units are necessary and are done with the unit_converter. This converter (OMC::SceneUnitConverter) will use the scene's metric information to convert between the units.

        Conversion from OGL to Field Units
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        unit_converter = scene.unit_converter                        #The unit converter for this scene.
        open_gl_point = harmony.Point3d( 1.0, 1.0, 1.0 )             #A Point3D object in 'OpenGL' units.
        field_point   = unit_converter.to_field( open_gl_point )     #Convert it.
        #Print the converted field units.
        print( "Field Units: %s %s %s"%(field_point.x, field_point.y, field_point.z) )
        ```
        """
        return SceneUnitConverter()
        
    @property
    def metadata(self) -> MetaDataHandler:
        """
        The metadata handler object to provide metadata information.

        Metadata can be used to store generic information in the scene, and in nodes. This data is created and accessed through the object (OMC::MetaDataHandler) provided by this property.
        Note
        Some metadata is used internally in the scene, and is not accessible in the DOM scripting.

        Print all Metadata in the scene.
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        for metadata in scene.metadata:
        print( "Key : %s"%(metadata.key) )
        print( "  Value : %s"%(metadata.value) )
        print( "  Type : %s"%(metadata.type) )
        ```

        Create Some Metadata
        ```python
        import json
        import time
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        metadata = scene.metadata                                    #The metadata handler.
        production_data = { 
                            "artist"   : "John Doe",
                            "scene_id" : "TB_001_0010",
                            "date"     : int(time.time())
                        }
        metadata["production_data"] = json.dumps( production_data )
        print( "Set Production Data" )
        json_data = metadata["production_data"].value
        retrieved_data = json.loads( json_data )
        for x in retrieved_data:
        print( "%s : %s"%(x, retrieved_data[x]) )
        #The metadata will be saved and available within the scene in subsequent instances of Harmony. This is useful for saving
        #generic data related to scenes or nodes.
        ```
        """
        return MetaDataHandler()
        
    @property
    def sounds(self):
        """
        The list of sound objects in the scene.

        Sounds and sound lists will be implemented in future DOM versions.
        """
        return Sound()
        
    @property
    def top(self) -> NodeList:
        """
        The top group in the scene.

        Every scene has an initial 'group' that contains the nodes of the scene. This group is transparent, in that it is not represented by any node in the node view – but it represents the outer-most layer in which nodes can be placed. Every scene starts with this group, named 'Top', and all subsequent nodes are placed within this container.

        Identify All Nodes in the 'Top' group of the scene.
        ```python
        import json
        import time
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        nodes = scene.top.nodes                                      #The node list of the nodes contained within the 'Top' group.
        for node in nodes:
        print( "Node: %s (%s)"%(node.path, node.type) )
        #Note -- this list will identify all nodes directly within the group, and does not consider the contents recursively.
        #The node list will not show nodes contained within other groups interior to itself; to do this, a recursive approach should be considered.  
        print( "\nNow -- Recursively . . ." )
        #Here is a recursive approach, a function that will do the work for us. . .
        def recursively_detail_group(group, depth):
        for node in group.nodes:                                         #Look through all if this group's contents.
            print( "%sNode: %s (%s)"%("   "*depth, node.path, node.type) ) #Print Information
            if node.type.upper() == "GROUP":                               #If its a group type, we recursive even further.
            recursively_detail_group( node, depth+1 )                    #Calling this same function will dive deeper into the next group.
        recursively_detail_group(scene.top, 0)                             #Start diving into the groups!
        ```
        """
        return NodeList()
        
    @property
    def nodes(self) -> NodeList:
        """
        The list of all nodes in the scene.

        The scene's nodelist provides the list of all the nodes in the scene, regardless of the group hierarchy. This means that all nodes in the scene, inlcuding those in subgroups, should be in this list. It can also be used to create and remove nodes from the scene as needed.

        Print path of all Nodes in the Scene:
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        nodes = scene.nodes                                          #The overall node list of the scene.
        for node in nodes:
        print( "Node: %s (%s)"%(node.path, node.type) )
        ```
        """
        return NodeList()
        
    @property
    def compositions(self):
        """The list of all compositions in the scene (based on available displays)."""
        return CompositionList()
        
    @property
    def columns(self) -> ColumnList:
        """
        The list of all columns in the scene.

        Columns are the time-based objects that provide values to animateable attributes on nodes. The scene's column list (OMC::ColumnList) is a list containing all columns in the scene and can be used to create, modify and remove columns as needed.

        List All Columns:
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        columns = scene.columns                                      #The overall node list of the scene.
        for col in columns:
        print( "Column: %s (%s)"%(col.name, col.type) )
        ```
        """
        return ColumnList()
        
    @property
    def display(self) -> DisplayNode:
        """
        Provides and sets the display node of the current display.

        Provides the OMC::DisplayNode that represents the display node set as the current global display in the scene. This value can be set as needed to different display nodes.

        Find and Set a Display Node:
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        nodes = scene.nodes                                          #The overall node list of the scene.
        for node in nodes:
        if node.type.upper() == "DISPLAY":
            scene.display = node
            print( "Set the Display Node to : %s"%(node.path) )
            break
        ```
        """
        return DisplayNode()
    
    @property
    def display_name(self) -> str:
        """
        Provides and sets the display node of the current display.

        Similar to OMC::Scene::display – provides the name of the OMC::DisplayNode as a string to the current display.

        Print the Current Display Name
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        print( "Current Display: %s"%(scene.display_name) )
        scene.display_name = None                                    #Set the Display to the generic "Display All" display. 
        ```
        """
        return ""
        
    @property
    def displays(self) -> List[Node]:
        """
        Provides a list of the display nodes available in the scene.

        Instead of searching for diplay nodes in the scene, OMC::Scene::displays provides a list of Display nodes available within the scene directly. This list cannot be modified directly. Print the Display List
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        displays = scene.displays                                        
        for display in displays:
        print( "Display: %s"%(display.name) )
        ```
        """
        return [Node()]
        
    @property
    def display_names(self) -> List[str]:
        """
        Provides a list of the display names available in the scene.

        Similar to OMC::Scene::displays, but instead of providing the node object (OMC::Node), provides the display names as strings.
        Print the Display Name List
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        display_names = scene.display_names                          #Get the display_name list.
        for display_name in display_names:
        print( "Display: %s"%(display_name) )
        ```
        """
        return [""]
        
    @property
    def palettes(self):
        """Provides a list of all available palettes in the project."""
        return PaletteList()

class HarmonyScene(Scene):
    """
    A scene within a loaded project.

    The scene provides access to functions and properties related to a specific scene within a project. The scene is composed of scene specific settings, nodes and column values.
    """
    def __init__(self):
        super().__init__()
    
    @property
    def selection(self):
        """
        Provides the selection handler for the current project.

        The selection handler (OMH::Selection) allows for read and write access to the current selection within the scene. This allows for nodes and columns to be referenced by selection, or selected as needed.
        
        Deselecting Undesired Nodes
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        history = proj.history
        history.begin( "Deselection unwanted nodes." )               #Selection can add undos (if undoable selection set in preferences)
        selection_handler = scene.selection                          #The selection handler.
        deselect_bad_nodes = []                                      #We'll iterate the list, find the nodes we want to deselect.
        for node in selection_handler.nodes:
        if not node.type.upper() == "PEG":                         #Lets deselect all nodes that ARE NOT pegs.
            deselect_bad_nodes.append( node )                        #We collect them here, to avoid deselecting them while iterating in the for loop; which could be complicated.
        if deselect_bad_nodes:
        selection_handler.remove( deselect_bad_nodes )               #Remove non-peg nodes from the selection, leaving ONLY pegs.
        
        history.end()
        ```
        """
        return Selection()
    
    @property
    def clipboard(self) -> Clipboard:
        """
        Provides the clipboard access for the current project.

        The clipboard object (OMH::Clipboard) is used for saving and recalling content as objects in memory. It is also used for generating templates.

        Copying Content
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        clipboard = scene.clipboard                                  #The clipboard object.
        selection_handler = scene.selection                          #The selection handler.
        selection_handler.nodes.select_all()                         #Select all nodes in the scene.
        copy_object = clipboard.copy( selection_handler.nodes.list() )    #Create a copy_object in memory from the selection.
        selection_handler.select_none()
        new_nodes = clipboard.paste_new_nodes( copy_object, scene.top )   #Paste duplicate nodes into the top-group of the scene.
        for node in new_nodes:
        print( "Pasted: %s"%(node.path) )                               #Announce the new node's path
        if node.parent_group().path == scene.top.path:
            node.position.y = node.position.y + 300                         #Move it up, to avoid overlap with existing content
        ```
        """
        return Clipboard()
    
    @property
    def processing_bit_depth(self) -> int:
        """
        Provides the processing bit-depth of the scene at render.

        The processing bit-depth defines how the Harmony handles the softrendering in the scene. Harmony supports both processing in 16-bit clamped values, and 32-bit floating point values. When using floating-point values, the values are unclamped and allow for values beyond 0 and 1. At 16-bit, the processing is limited to values within the 16-bit range (0 - 32767).

        Changing Processing Bit-Depth
        ```python
        from ToonBoom import harmony                                 #Import the Harmony Module
        sess = harmony.session()                                     #Get access to the Harmony session, this class.
        proj = sess.project                                          #Get the active session's currently loaded project.
        scene = proj.scene                                           #Get the top scene in the project.
        print( "Current bit-depth: %s"%(scene.processing_bit_depth) )
        scene.processing_bit_depth = 32
        ```
        """
        return 1

class SceneList(ListObj, IterableObj):
    """
    A list of scenes contained within a project.

    Provided from OMC::Project::scenes and provides an object with iterable, list[idx] access to the available OMC::Scene objects. In Harmony, multiple scenes will be present in the project if symbols are used.

    Note
    The main scene should always be the first entry in the scene list. This main scene is also available from OMC::Project::scene.

    Identify All Scenes in a Project
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene_list = proj.scenes                                     #The scene list for the project.
    print( "Scene Count : %s"%(len(scene_list)) )
    for idx,scene in enumerate( scene_list ):
    print( "Scene %s : %s"%(idx,scene.name) )
    ```
    """
    def __init__(self):
        super().__init__()
    
    def __getitem__(self, idx:int) -> Scene:
        """Provides the Scene at the given index."""
        return Scene()

class HarmonySceneList(SceneList):
    """
    The Scene List specialized for Harmony.

    For more information, see the generic OMC::SceneList.
    """
    def __init__(self):
        super().__init__()

class SelectionColumnList(ListQVar, IterableQVar):
    def __init__(self):
        super().__init__()
    
    def __getitem__(self, idx:int, searchString:str) -> Column:
        """
        [1/2] - idx
        Returns a string that represents the flavor of the application. e.g. Harmony.

        ------------------------------------------------------------------------
        [2/2] - searchString         
        Search for an node in the node with a specialized search string. Search string formatting to be discussed.

        Returns
            The node found at the given string.
        """
        return Column()
    
    def contains(self, Column:Column) -> bool:
        """Identifies if the list contains the node (or subnode)."""
        return True
    
    def list(self) -> List[Column]:
        """Converts the dynamic list into a concrete list of node objects."""
        return [Column()]
    
    def add(self, column:Column):
        """
        Add a node to the selection.

        Returns
            True if successfully added to the selection.
        """
        return
    
    def remove(self, column:Column):
        """
        Remove a node from the selection.

        Returns
            True if successfully removed from the selection.
        """
        return
    
    def select_all(self):
        """Selects all columns in the scene."""
        return
    
    def select_none(self):
        """Removes all columns from the selection."""
        return

class SelectionNodeList(ListQVar, IterableQVar):
    def __init__(self):
        super().__init__()
    
    def __getitem__(self, idx:int, searchString:str) -> Node:
        """
        [1/2] - idx 

        Returns a string that represents the flavor of the application. e.g. Harmony.
        ------------------------------------------------------------------------
        [2/2] - searchString

        Search for an node in the node with a specialized search string. Search string formatting to be discussed.

        Returns
            The node found at the given string.
        """
        return Node()
    
    def contains(self, node:Node) -> bool:
        """Identifies if the list contains the node (or subnode)."""
        return True
    
    def list(self) -> List[Node]:
        """Converts the dynamic list into a concrete list of node objects."""
        return [Node()]
    
    def add(self, node):
        """
        Add a node to the selection.

        Returns
            True if successfully added to the selection.
        """
        return
    
    def remove(self, node):
        """
        Remove a node from the selection.

        Returns
            True if successfully removed from the selection.
        """
        return
    
    def select_all(self):
        """Selects all nodes in the scene."""
        return
    
    def select_none(self):
        """Removes all nodes from the selection."""
        return


class Selection(ListQVar, IterableQVar):
    """
    Provides selections within Harmony.

    The Selection object is provided from the OMH::HarmonyScene from the OMH::HarmonyScene::selection attribute.

    Deselecting Undesired Nodes
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    history = proj.history
    history.begin( "Deselection unwanted nodes." )               #Selection can add undos (if undoable selection set in preferences)
    selection_handler = scene.selection                          #The selection handler.
    deselect_bad_nodes = []                                      #We'll iterate the list, find the nodes we want to deselect.
    for node in selection_handler.nodes:
    if not node.type.upper() == "PEG":                         #Lets deselect all nodes that ARE NOT pegs.
        deselect_bad_nodes.append( node )                        #We collect them here, to avoid deselecting them while iterating in the for loop; which could be complicated.
    if deselect_bad_nodes:
    selection_handler.remove( deselect_bad_nodes )               #Remove non-peg nodes from the selection, leaving ONLY pegs.
    history.end()
    ```
    """
    def __init__(self):
        super().__init__()
    
    def contains(self, BaseObject) -> bool:
        """Identifies if the list contains the node (or subnode)."""
        return True
    
    def list(self) -> List[BaseObject]:
        """Converts the dynamic list into a concrete list of node objects."""
        return
    
    def add(self, item):
        """Add an item to the selection."""
        return
    
    def remove(self, node):
        """Remove an item from the selection."""
        return
    
    def select_all(self):
        """Selects all nodes and all columns in the scene."""
        return
    
    def select_none(self):
        """Removes all items from the selection."""
        return
    
    def setFrameRange(self, startFrame:int, length:int):
        """Sets the selection range."""
        return
    
    def create_template(self) -> str:
        """
        Creates template from the current selection in the scene, using only the current drawing versions.

        No template is created when there is nothing selected, when the path is not valid or when there is an IO error.

        Parameters
            name	: The name of the new template.
            path	: The location of the new template.
            copyOptions	: [optional] The OMC::copyOptions that provide extra options when creating the template.
        
        Returns
            Returns the full path of the new template. Will return an empty string if no template file was created.
        """
        return ""

    def __getitem__(self, idx) -> BaseObject:
        """
        Provides the object at the given index within the selection.

        The provided value can be of any supported selection-type. For more information see the available selection-specializations:

        OMH::Selection::nodes : A list handler for providing selected nodes.
        OMH::Selection::columns : A list handler for providing selected columns.
        """
        return BaseObject()

    @property
    def nodes(self) -> SelectionNodeList:
        """The list of selected nodes."""
        return SelectionNodeList()
        
    @property
    def columns(self) -> SelectionColumnList:
        """The list of selected columns."""
        return SelectionColumnList()
        
    @property
    def ranged(self) -> bool:
        """True if the selection has a range."""
        return True
        
    @property
    def frame_range(self):
        """The number of frames selected."""
        return
        
    @property
    def frame_start(self) -> int:
        """The start frame of the selected range."""
        return 1

class TextAttribute(Attribute):
    """
    The text-attribute wrapper.

    The text attribute is a non-animateable attribute that provides a text value from an Attribute on a Node. In some nodes, the text attribute is used directly as text; in other nodes, it can be used for specialized, formatted data saved internally as a string.

    Set the Text Attribute on a Group

    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    node = scene.nodes["Top/Group"]                              #Find the Group node.
    #The group node contains a hidden text attribute that defines what node is used to represent it in the timeline.
    #This node is set by name in the "TIMELINE_MODULE" attribute.
    text_attribute = node.attributes["TIMELINE_MODULE"]          #Get the TIMELINE_MODULE text attribute.
    try:                                                         #Instead of checking along the way for validity, we'll catch the error.
    #Now, lets find the node that outputs on the rightmost port of the group.
    #Using the right most port, follow it through its related port, and get the source.
    external_port = node.ports_out[0]
    internal_port = external_port.port_related
    source_node = internal_port.source_node
    
    #Set the group to be represented by this node.
    text_attribute.set_value(0, source_node.name )             
    print( "Set Group's TIMELINE_MODULE to: %s"%(source_node.name) )
    except:
    print( "Failed to find or set TIMELINE_MODULE" )
    ```
    """
    def __init__(self):
        super().__init__()
    
    def localvalue(self) -> str:
        """Get the attribute's value."""
        return ""
    
    def value(self, frame:int) -> str:
        """Get the attribute's value at a given frame."""
        return ""
    
    def setLocalvalue(self, value:str):
        """Get the attribute's value."""
        return
    
    def setValue(self, frame:int, value:str):
        """Get the attribute's value at a given frame."""
        return

class TimingAttribute(Attribute):
    """
    The attribute wrapper.

    This object wraps an element attribute – often provided by a DrawingAttribute when in element mode.

    When a DrawingAttribute is in in Timing Mode (OMC::DrawingAttribute::element_mode == False), the drawing attribute receives its values from the underlying TimingAttribute.
    The TimingAttribute provides a location, size, suffix and timing for content sourced externally from the project. This content is not sourced from the project's elements folder, and the timing is used to simply target a different source elsewhere or disk.
    """
    def __init__(self):
        super().__init__()
    
    def localvalue(self) -> str:
        """Get the attribute's value."""
        return ""
    
    def value(self, frame:int) -> str:
        """Get the attribute's value at a given frame."""
        return ""
    
    def setLocalvalue(self, value:str):
        """Get the attribute's value."""
        return
    
    def setValue(self, frame:int, value:str):
        """Get the attribute's value at a given frame."""
        return

class Transformation(BaseObject):
    """Provides a transformation object that can contain transformation, depth and deformation data."""
    def __init__(self):
        super().__init__()
    
    def reset(self):
        """Reset the transformation to its default values."""
        return
    
    def multiply(self, matrix:Matrix):
        """Compounds this matrix with m, same as = (*this) * m. The matrix object is modified in place."""
        return
    
    def translate(self, vector:Vector3d, deltaX:float=0.0, deltaY:float=0.0, deltaZ:float=0.):
        """Translates the local coordinate system represented by this tranformation matrix by the given vector. The matrix object is modified in place."""
        return
    
    def scale(self, scaleX:float=1.0, scaleY:float=1.0, scaleZ:float=1.0):
        """Scales the local coordinate system represented by this tranformation matrix by the given factors. The matrix object is modified in place."""
        return
    
    def rotate_radians(self, rads:float, vector:Vector3d):
        """Rotates the local coordinate system represented by this tranformation matrix by the given angle (expressed in radian) around the given vector. The matrix object is modified in place."""
        return
    
    def rotate_degrees(self, degs:float, vector:Vector3d):
        """	Rotates the local coordinate system represented by this tranformation matrix by the given angle (expressed in degree) around the given vector. The matrix object is modified in place."""
        return
    
    def skew(self, skew:float):
        """Skews the local coordinate system represented by this tranformation matrix by the given angle (expressed in degree). The matrix object is modified in place."""
        return
    
    def add(self, matrix:Matrix):
        """Add to the matrix of the transformation."""
        return
    
    def set(self, matrix:Matrix):
        """Set the matrix of the transformation."""
        return
    
    def deformation_reset(self):
        """Reset the transformation so that no deformation is present, but transformations are retained."""
        return
    
    def matrix_with_deformation(self) -> Matrix:
        """Returns the transformation matrix with the deformation's final transformation applied."""
        return Matrix()
    
    def matrix_inversed(self) -> Matrix:
        """Returns the inverted transformation matrix, if possible."""
        return Matrix()
    
    @property
    def depth(self) -> int:
        """The transformation depth, used when compositing in layered space, as opposed to the transformation space."""
        return 1
        
    @property
    def valid(self) -> bool:
        """Identifies if the transformation has been set and is valid."""
        return True
        
    @property
    def matrix(self) -> Matrix:
        """Get and set the transformation matrix."""
        return Matrix
        
    @property
    def deformation_valid(self) -> bool:
        """Identifies if the transformation has valid deformations applied."""
        return True
        
    @property
    def origin(self) -> Point3d:
        """Get the transformation matrix' origin."""
        return Point3d
    
class Vector2d(Point2d):
    """Provides a 2D Vector using double values."""
    def __init__(self):
        super().__init__()

class VeloBasedColumn(KeyframeableColumn):
    """
    A Column type that provides an interpolated value based on a velocity property.

    The VeloBased column uses a velocty-based interpolation to provide a double value.
    """
    def __init__(self):
        super().__init__()

class VeloBasedColumnValue(ColumnValue):
    """
    the frame,value object provided from the VeloBasedColumn

    The VeloBasedColumn provides the frame,value object representing a given frame from its VeloBasedColumn::operator[int idx] or when being iterated. This object can be used to get and set values on the column.
    """
    def __init__(self):
        super().__init__()
    
    @property
    def key(self) -> bool:
        """Defines whether or not the frame represents a key. Setting this to true will create a key."""
        return True
        
    @property
    def keyframe_previous(self) -> BezierColumnValue:
        """The previous frame at which there is a keyframe present, this frame value object if its currently a keyframe."""
        return BezierColumnValue()
        
    @property
    def keyframe_next(self) -> BezierColumnValue:
        """The next frame at which there is a keyframe present. If none are present, returns none."""
        return BezierColumnValue()

class VeloBasedControlPoint(ControlPoint):
    """
    An object that represents the control point of velo based column.

    Provided by OMC::VeloBasedColumn::control_points. Provides the keyframes and keyframe options associated with a keyframeable velo-based column.
    Look Through Velo-based Keyframes

    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    sess = harmony.session()                                     #Get access to the Harmony session, this class.
    proj = sess.project                                          #Get the active session's currently loaded project.
    scene = proj.scene                                           #Get the top scene in the project.
    columns = scene.columns                                      #The overall column list of the scene.
    velo_col = columns["VELO_COLUMN_NAME"]
    keyframes = velo_col.control_points                          #This list provides VeloBasedControlPoint objects.
    for keyframe in keyframes:
    print( "Key At: %s %s"%(keyframe.frame, keyframe.value)  )
    ```
    """
    def __init__(self):
        super().__init__()

def session() -> Harmony:
    """
    Provides the session for Harmony and its active object.

    This is the main access to the application, the project and its contents.

    The session is loaded when the application is launched and a project is opened. When internal to Harmony, the session will be the actively loaded project in Harmony. When offline, the session will be the project that has been loaded from the subsequent open_project and open_project_database commands.

    Returns
        OMH::Harmony* The harmony session object that provides further access to the application and its contents.
    
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    session = harmony.session()
    ```
    """
    return Harmony()

def close_project():
    """
    Closes the currently loaded project..

    Closing the project from an internal Python console will result in the project being closed similar to using the menu option File -> Close .
    Closing the project from an external Python console will result in the active project being closed, and the session no longer having a project available. A subsequent project will need to be loaded for further actions in the interpreter.

    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    harmony.open_project( "path/to/project/file.xstage )         #Open the Harmony scene file offline.
    harmony.close_project()                                      #Closes the project as above.
    ```
    """
    return

def open_project(projectPath:str):
    """
    Opens an offline Harmony project.

    Open the scene located at the given path. If a scene is previously opened, it will be closed first. Unsaved changes will be lost. Opening an offline project requires a Harmony Database license, but will open an offline Harmony stage file.

    Parameters
        projectPath	- The path to the project file, including the filename and .xstage.
    
    ```python
    from ToonBoom import harmony                                 #Import the Harmony Module
    harmony.open_project( "path/to/project/file.xstage )         #Open the Harmony scene file offline.
    ```
    """
    return

def open_project_database(userName:str, envName:str, jobName:str, sceneName:str, versionName:str=""):
    """
    Opens a project over the Harmony database given the current database configuration.

    Opening a project over the Harmony Database requires a database configuration and appropriate database licenses. The project will be opened with the provided arguments.

    Parameters
        userName	- The username to use while loading the project over the database. This username should be a valid user name in the database.
        envName	- The environment in which the project resides.
        jobName	- The job in which the project resides.
        sceneName	- The name of the scene that should be loaded.
        versionName	- Optional. The named version to load. If none is provided, the current version of the scene is loaded.
    
    ```python
    from ToonBoom import harmony                                                   #Import the Harmony Module
    harmony.open_project_database( "usabatch", "environment", "job", "scene" )     #Open the Harmony scene file online, with the Harmony server's database..
    ```
    """
    return

def launch():
    """
    Launches the instance of Harmony if none is available. Launching an instance of harmony allows access to specific Harmony global objects, further access to a scene will require a project to be opened.

    Note
    When using open_project, or open_project_database – an instance of Harmony will be launched if no other instance is available
    """
    return
