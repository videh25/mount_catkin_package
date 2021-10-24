import sys

def urdf2macro(argv):
    # Pass absoute path of urdf as argument
    # Pass gripper_base_to_tcp_distance as argument
    # Pass name of base link as argument
    if len(argv) != 4:
        print("Please pass proper arguments")
        sys.exit(1)
    
    if argv[1][-5:] not in ['.urdf', '.URDF']:
        print("Pass a proper urdf file with approriate format")
        sys.exit(1)

    gripper_base_to_tcp_distance = argv[2]
    gripper_base_name = argv[3]

    search_state = [False, False, False]
    copy_start_index = [0,0]
    copy_end_index = [0,0]
    
    with open(argv[1]) as urdf_file:
        read_lines_urdf = urdf_file.readlines()
        for line_ind,line in enumerate(read_lines_urdf):
            if not search_state[0]:
                if ("<robot" in line):
                    search_state[0] = True
                    if ">" in line:
                        search_state[1] = True
                        if line.find(">") == len(line) - 1:
                            copy_start_index[0] = line_ind + 1
                            copy_start_index[1] = 0
                        else:
                            copy_start_index[0] = line_ind
                            copy_start_index[1] = line.find(">") + 1

            elif search_state[0] and (not search_state[1]):
                if ">" in line:
                    search_state[1] = True
                    if line.find(">") == len(line) - 1:
                        copy_start_index[0] = line_ind + 1
                        copy_start_index[1] = 0
                    else:
                        copy_start_index[0] = line_ind
                        copy_start_index[1] = line.find(">") + 1
            
            elif search_state[0] and search_state[1] and (not search_state[2]):
                if "</robot>" in line:
                    search_state[2] = True
                    if line.find("</robot>") == 0:
                        copy_end_index[0] = line_ind - 1
                        copy_end_index[1] = len(read_lines_urdf[line_ind-1])-1
                    else:
                        copy_end_index[0] = line_ind
                        copy_end_index[1] = line.find("</robot>")
            
            elif False not in search_state:
                break
        
        print(argv[1][:-5] + ".xacro")

        with open(argv[1][:-5] + ".xacro", 'a+') as xacro_file:
            # DOCUMENT: end link of arm must be named tool0
            # DOCUMENT: base link of gripper must be named gripper_base
            xacro_file.write('''<?xml version="1.0" encoding="utf-8"?>
<robot xmlns:xacro="https://ros.org/wiki/xacro">
<xacro:macro name="gripper">
<joint name="flange_to_gripper_joint" type="fixed">
    <parent link="tool0"/>
    <child link="'''+ gripper_base_name+'''"/>
    <origin rpy="0 0 0" xyz="0 0 0"/>
</joint>''')
                  
            for i in range(copy_start_index[0], copy_end_index[0] + 1):
                if i == copy_start_index[0]:
                    xacro_file.write(read_lines_urdf[i][copy_start_index[1]:])
                elif i == copy_end_index[0]:
                    xacro_file.write(read_lines_urdf[i][:copy_end_index[1]+1])
                else:
                    xacro_file.write(read_lines_urdf[i])
            
            xacro_file.write('''
<joint name="tcp_joint" type="fixed">
    <origin xyz="0 0 ''' + str(gripper_base_to_tcp_distance) + '''" rpy="0 0 0"/>
    <parent link="'''+ gripper_base_name+'''"/>
    <child link="tcp"/>
</joint>
<link name="tcp"/>

</xacro:macro>
</robot>''')

if __name__ == "__main__":
    urdf2macro(sys.argv)