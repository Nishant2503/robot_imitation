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

cube_id = p.loadURDF(
    "cube_small.urdf",
    [0.2, -0.2, 0.2]
)

endEffector_link_index = 7

end_pos = p.calculateInverseKinematics(
    bodyUniqueId=robot_id,
    endEffectorLinkIndex=endEffector_link_index,
    targetPosition=[0.2, -0.2, 0.2]
)

movable_joints = [1,2,3,4,5,7]
k=0

for i in movable_joints:
    p.setJointMotorControl2(
        bodyUniqueId=robot_id,
        jointIndex=i,
        controlMode=p.POSITION_CONTROL,
        targetPosition=end_pos[k],
        force=5
    )
    k=k+1




while True:
    p.stepSimulation()
    time.sleep(1 / 240)