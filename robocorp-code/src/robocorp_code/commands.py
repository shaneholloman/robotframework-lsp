# Warning: Don't edit file (autogenerated from python -m dev codegen).

ROBOCORP_GET_LANGUAGE_SERVER_PYTHON = "robocorp.getLanguageServerPython"  # Get a python executable suitable to start the language server
ROBOCORP_GET_PLUGINS_DIR = "robocorp.getPluginsDir"  # Get the directory for plugins
ROBOCORP_CREATE_ROBOT = "robocorp.createRobot"  # Create Robot
ROBOCORP_LIST_ROBOT_TEMPLATES_INTERNAL = "robocorp.listRobotTemplates.internal"  # Provides a list with the available robot templates
ROBOCORP_CREATE_ROBOT_INTERNAL = "robocorp.createRobot.internal"  # Actually calls rcc to create the robot
ROBOCORP_UPLOAD_ROBOT_TO_CLOUD = "robocorp.uploadRobotToCloud"  # Upload Robot to the cloud
ROBOCORP_LOCAL_LIST_ROBOTS_INTERNAL = "robocorp.localListRobots.internal"  # Lists the activities currently available in the workspace
ROBOCORP_IS_LOGIN_NEEDED_INTERNAL = "robocorp.isLoginNeeded.internal"  # Checks if the user is already logged in
ROBOCORP_CLOUD_LOGIN = "robocorp.cloudLogin"  # Log in Robocloud
ROBOCORP_CLOUD_LOGIN_INTERNAL = "robocorp.cloudLogin.internal"  # Log in Robocloud (receives credentials)
ROBOCORP_CLOUD_LIST_WORKSPACES_INTERNAL = "robocorp.cloudListWorkspaces.internal"  # Lists the workspaces available for the user (in the cloud)
ROBOCORP_UPLOAD_TO_NEW_ROBOT_INTERNAL = "robocorp.uploadToNewRobot.internal"  # Uploads an Robot as a new Robot in the cloud
ROBOCORP_UPLOAD_TO_EXISTING_ROBOT_INTERNAL = "robocorp.uploadToExistingRobot.internal"  # Uploads an Robot as an existing Robot in the cloud
ROBOCORP_RUN_IN_RCC_INTERNAL = "robocorp.runInRcc.internal"  # Runs a custom command in RCC
ROBOCORP_RUN_ROBOT_RCC = "robocorp.runRobotRcc"  # Run Robot
ROBOCORP_DEBUG_ROBOT_RCC = "robocorp.debugRobotRcc"  # Debug Robot
ROBOCORP_SAVE_IN_DISK_LRU = "robocorp.saveInDiskLRU"  # Saves some data in an LRU in the disk
ROBOCORP_LOAD_FROM_DISK_LRU = "robocorp.loadFromDiskLRU"  # Loads some LRU data from the disk
ROBOCORP_COMPUTE_ROBOT_LAUNCH_FROM_ROBOCORP_CODE_LAUNCH = "robocorp.computeRobotLaunchFromRobocorpCodeLaunch"  # Computes a robot launch debug configuration based on the robocorp code launch debug configuration

ALL_SERVER_COMMANDS = [
    ROBOCORP_GET_PLUGINS_DIR,
    ROBOCORP_LIST_ROBOT_TEMPLATES_INTERNAL,
    ROBOCORP_CREATE_ROBOT_INTERNAL,
    ROBOCORP_LOCAL_LIST_ROBOTS_INTERNAL,
    ROBOCORP_IS_LOGIN_NEEDED_INTERNAL,
    ROBOCORP_CLOUD_LOGIN_INTERNAL,
    ROBOCORP_CLOUD_LIST_WORKSPACES_INTERNAL,
    ROBOCORP_UPLOAD_TO_NEW_ROBOT_INTERNAL,
    ROBOCORP_UPLOAD_TO_EXISTING_ROBOT_INTERNAL,
    ROBOCORP_RUN_IN_RCC_INTERNAL,
    ROBOCORP_SAVE_IN_DISK_LRU,
    ROBOCORP_LOAD_FROM_DISK_LRU,
    ROBOCORP_COMPUTE_ROBOT_LAUNCH_FROM_ROBOCORP_CODE_LAUNCH,
]
