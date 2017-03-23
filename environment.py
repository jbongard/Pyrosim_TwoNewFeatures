import constants as c

class ENVIRONMENT:

        def __init__(self, e): 

		self.ID = e

		#self.l = c.l
		#self.w = c.l
		#self.h = c.l

		#self.z = c.l/2

		#self.Send_Light_Source(sim)

		#self.Send_Ball()
 
	def Send_To(self,sim):

		sim.Send_Box(objectID=9, x=0, y=0, z=c.blockLength/2, length=c.blockLength*5, width=c.blockLength*5, height=c.blockLength, r=0, g=0.5, b=0)

		sim.Send_Light_Source(objectIndex = 9)

		sim.Send_Cylinder(objectID=10, x=0, y=0, z=c.blockLength*4, length=0, radius=2*c.r, r=1, g=1, b=1)
