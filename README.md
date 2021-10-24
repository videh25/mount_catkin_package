# mount_catkin_package
A ROS package to mount a gripper (with given URDF) on a robotic arm's flage (given URDF). 
Note: The package was built on ROS-Noetic

### Getting Started
1. Create a catkin workspace for these packages to download in.
2. Download the three packages in the src folder of the worskpace.
3. Run `catkin_make` in the workspace folder.

### Description of Packages
#### 1.ur_description
Description of the Universal Robot's Manipulator Arms.
Folder taken from https://github.com/ros-industrial/universal_robot/tree/melodic-devel-staging/ur_description
#### 2. robotiq_arg85_description
Description of the gripper
Folder cloned from https://github.com/a-price/robotiq_arg85_description
#### 3. mount
Package developed to easily mount the grippers on the robotic arms

### 2 main functions:
#### 1. urdf2macro.py
For modularity and mounting, it is handy to have a .xacro file of the gripper and arm saved. However, .urdf file of gripper was available.
This function converts a takes .urdf file as input and generates a .xacro file that can be used to mount the gripper on arm.

Usage:
_Using rosrun_
```shell
rosrun urdf2macro.py <Absolute Path of the gripper.urdf> <Flange to TCP distance> <Name of base_link of gripper>
```
**Flange(Enf Effector of Arm) to TCP distance:** Tool Centre Point (TCP), to be used for Inverse Kinematics will be set based on this.

**Name of base_link of gripper:** To be searched in the <gripper>.urdf file. It is the name of link supposed to be attached directly to flange.

The new <gripper>.xacro file will be generated in the same folder and same name as the <gripper>.urdf. Feel free to copy paste this .xacro file for convinience.
  
#### 2. mount.py
Loads the given <gripper>.xacro and <arm>.xacro by generating a .xacro file by combining both individual .xacros. The resultant .xacro is saved as the mount\scripts\urdf\arm_with_gripper.xacro
  
Usage:
  _Using rosun_
  ```shell
  rosrun mount mount.py <Absolute path to <arm>.xacro> <Absolute path to <gripper>.xacro> <Name of macro of the arm>
  ```

**Name of macro of the arm:** To be searched in the <arm>.xacro file. It is the name of macro used to define the links and joints of the arm.
  
### Launching the loaded arm-gripper pair in rviz
Once the arm and gripper are successfully loaded, launch the model using display.launch as follows:
  ```shell
  roslaunch mount display.launch
  ```
  This should launch the loaded model of arm and gripper in rviz.

## Examples
For the given robotic arm sets and gripper,
  
1. Convert the gripper urdf to xacro
  
  ```shell
  
  ```
2. Load the gripper and arm
  _For UR5_
  ```shell
  
  ```
  
  
  _For UR3_
  ```shell
  
  ```
 3. Launching any loaded model in rviz
  UR5
  
  UR3
