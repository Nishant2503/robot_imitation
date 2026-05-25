import pybullet as p
import pybullet_data
import time
import os

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)

# Load ground
p.loadURDF("plane.urdf")

# Path to your robot URDF
urdf_path = "assets/urdf/so101.urdf"

# Check if file exists
if not os.path.exists(urdf_path):
    raise FileNotFoundError(f"URDF not found at: {urdf_path}")

# Load robot
robot_id = p.loadURDF(
    urdf_path,
    basePosition=[0, 0, 0],
    useFixedBase=True
)

# Set camera view
p.resetDebugVisualizerCamera(
    cameraDistance=0.8,
    cameraYaw=45,
    cameraPitch=-35,
    cameraTargetPosition=[0, 0, 0.1]
)

# Print joint info
num_joints = p.getNumJoints(robot_id)
print("Number of joints:", num_joints)

for i in range(num_joints):
    info = p.getJointInfo(robot_id, i)
    print("Joint index:", i)
    print("Joint name:", info[1].decode("utf-8"))
    print("Joint type:", info[2])
    print("Lower limit:", info[8])
    print("Upper limit:", info[9])
    print("Link name:", info[12].decode("utf-8"))
    print("----------------------")

while True:
    p.stepSimulation()
    time.sleep(1 / 240)