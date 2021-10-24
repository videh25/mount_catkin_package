# mount_catkin_package
A ROS package to mount a gripper (with given URDF) on a robotic arm's flage (given URDF). 
Note: The package was built on ROS-Noetic

## Getting Started
1. Create a catkin workspace for these packages to download in.
2. Download the three packages in the src folder of the worskpace.
3. Run `catkin_make` in the workspace folder.

## Description of Packages
### 1.ur_description
Description of the Universal Robot's Manipulator Arms.
Folder taken from https://github.com/ros-industrial/universal_robot/tree/melodic-devel-staging/ur_description
### 2. robotiq_arg85_description
Description of the gripper
Folder cloned from https://github.com/a-price/robotiq_arg85_description
### 3. mount
Package developed to easily mount the grippers on the robotic arms

### 2 main functions:
1. mount.py
2. urdf2macro.py

