import pybullet as p
import pybullet_data
import time

# Connect to PyBullet GUI
p.connect(p.GUI)

# Add default PyBullet data path
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Set gravity
p.setGravity(0, 0, -9.81)

# Load ground plane
p.loadURDF("plane.urdf")

# Create table
table_collision = p.createCollisionShape(
    p.GEOM_BOX,
    halfExtents=[0.4, 0.3, 0.02]
)

table_visual = p.createVisualShape(
    p.GEOM_BOX,
    halfExtents=[0.4, 0.3, 0.02],
    rgbaColor=[0.7, 0.7, 0.7, 1]
)

p.createMultiBody(
    baseMass=0,
    baseCollisionShapeIndex=table_collision,
    baseVisualShapeIndex=table_visual,
    basePosition=[0.3, 0, 0.02]
)

# Create red block
block_collision = p.createCollisionShape(
    p.GEOM_BOX,
    halfExtents=[0.025, 0.025, 0.025]
)

block_visual = p.createVisualShape(
    p.GEOM_BOX,
    halfExtents=[0.025, 0.025, 0.025],
    rgbaColor=[1, 0, 0, 1]
)

p.createMultiBody(
    baseMass=0.05,
    baseCollisionShapeIndex=block_collision,
    baseVisualShapeIndex=block_visual,
    basePosition=[0.25, 0.05, 0.07]
)

# Set camera view
p.resetDebugVisualizerCamera(
    cameraDistance=0.8,
    cameraYaw=45,
    cameraPitch=-35,
    cameraTargetPosition=[0.25, 0, 0]
)

# Run simulation
while True:
    p.stepSimulation()
    time.sleep(1 / 240)