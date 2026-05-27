import pybullet as p
import pybullet_data
import time
import os

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)

p.loadURDF("plane.urdf")

urdf_path = "assets/urdf/so101.urdf"

robot_id = p.loadURDF(
    urdf_path,
    basePosition=[0, 0, 0],
    useFixedBase=True
)

# Set camera view
p.resetDebugVisualizerCamera(
    cameraDistance=0.8,
    cameraYaw=0,
    cameraPitch=-35,
    cameraTargetPosition=[0, 0, 0.1]
)
num_joints = p.getNumJoints(robot_id)


for i in range(num_joints):

    print("Joint index:", i)
    info = p.getJointInfo(robot_id,i)
    joint_name = info[1].decode("utf-8")
    joint_type = info[2]

    if joint_type == p.JOINT_FIXED:
        print("Joint", joint_name, "is fixed.")
        continue

    for _ in range(240):
        p.setJointMotorControl2(
            bodyUniqueId = robot_id,
            jointIndex = i,
            controlMode = p.POSITION_CONTROL,
            targetPosition = 0.5,
            force = 5
        )
        p.stepSimulation()
        time.sleep(1/240)

    time.sleep(1)
    for _ in range(240):
        p.setJointMotorControl2(
            bodyUniqueId = robot_id,
            jointIndex = i,
            controlMode = p.POSITION_CONTROL,
            targetPosition = 0,
            force = 5
        )
        p.stepSimulation()
        time.sleep(1/240)


while True:
    p.stepSimulation()
    time.sleep(1 / 240)



