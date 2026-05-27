import pybullet as p
import pybullet_data
import time

## setup
p.connect(p.GUI)
p.resetSimulation()
p.setGravity(gravX=0, gravY=0, gravZ=-9.8)
p.setAdditionalSearchPath(path=pybullet_data.getDataPath())

plane = p.loadURDF("plane.urdf")

cube_position = [0.3, 0, 0.2]

#loading cube
cube_id = p.loadURDF(
    "cube_small.urdf",
    cube_position
)

#loading arm 
urdf_path = "assets/urdf/so101.urdf"
robot_id = p.loadURDF(
    urdf_path,
    basePosition=[0, 0, 0],
    useFixedBase=True
)

movable_joints = []

num_joints = p.getNumJoints(robot_id)

for i in range(num_joints):

    joint_info = p.getJointInfo(robot_id, i)
    joint_type = joint_info[2]
    if joint_type != p.JOINT_FIXED:
        movable_joints.append(i)

while True:

    p.stepSimulation()

    time.sleep(1 / 240)