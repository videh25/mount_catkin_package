import sys

def mount(argv):
    # Generates a Xacro file that imports and combines the arm and gripper
    # Stores the xacro file in the scripts/urdf folder of the package
    # Arm.xacro , Gripper.xacro passed :: Absolute paths
    #Also pass xacro name of the arm

    if len(argv) != 4:
        print("Please pass proper arguments")
        sys.exit(1)

    # arm.xacro = argv[1]
    # gripper.xacro = argv[2]
    with open("urdf/arm_with_gripper.xacro", 'w') as file:
        file.write('''<?xml version="1.0"?>
<robot xmlns:xacro="http://wiki.ros.org/xacro" name="arm_with_gripper">
<xacro:include filename="'''+ argv[1]+'''" />
<xacro:include filename="'''+ argv[2]+'''"/>
<xacro:'''+argv[3]+''' prefix="" joint_limited="true" />
<xacro:gripper />
<link name="world" />

<joint name="world_joint" type="fixed">
	<parent link="world" />
	<child link = "base_link" />
	<origin xyz="0.0 0.0 0.0" rpy="0.0 0.0 0.0" />
</joint>

</robot>''')

if __name__ == "__main__":
    mount(sys.argv)