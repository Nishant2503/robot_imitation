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


p.resetDebugVisualizerCamera(
    cameraDistance=0.8,
    cameraYaw=0,
    cameraPitch=-35,
    cameraTargetPosition=[0, 0, 0.1]
)


target_position = [0.2, -0.2, 0.2]

cube_id = p.loadURDF(
    "cube_small.urdf",
    target_position
)


end_effector_link_index = 7

joint_angles = p.calculateInverseKinematics(
    bodyUniqueId=robot_id,
    endEffectorLinkIndex=end_effector_link_index,
    targetPosition=target_position
)

print("IK Joint Angles:")
print(joint_angles)


movable_joints = [1, 2, 3, 4, 5]



current_positions = []

for joint in movable_joints:

    joint_state = p.getJointState(robot_id, joint)

    current_positions.append(joint_state[0])


steps = 240

for step in range(steps):

    alpha = step / steps

    for k, joint in enumerate(movable_joints):

        target = current_positions[k] + alpha * (
            joint_angles[k] - current_positions[k]
        )

        p.setJointMotorControl2(
            bodyUniqueId=robot_id,
            jointIndex=joint,
            controlMode=p.POSITION_CONTROL,
            targetPosition=target,
            force=20
        )

    p.stepSimulation()

    time.sleep(1 / 240)

while True:

    p.stepSimulation()

    time.sleep(1 / 240)