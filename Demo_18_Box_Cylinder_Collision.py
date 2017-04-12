from pyrosim import PYROSIM

ARM_LENGTH = 0.5

ARM_RADIUS = ARM_LENGTH / 10.0

sim = PYROSIM(playPaused = False, evalTime = 200)

sim.Send_Box(objectID=0, x=0, y=0, z=0.05, length=0.5, width=0.5, height=0.1)

sim.Send_Cylinder(objectID=1 , x=0, y=0, z=0.05 + 0.5, length=0, radius=0.1)

sim.Start()

