from population import POPULATION
#import copy
from environments import ENVIRONMENTS
import constants as c

envs = ENVIRONMENTS()

parents = POPULATION(c.popSize)
parents.Initialize()
parents.Evaluate(envs, pp=False, pb=False)
#print 0,
#parents.Print()

#for g in range(1,c.numGens):
#	children = POPULATION(c.popSize)
#	children.Fill_From(parents)
#	children.Evaluate(envs, pp=False,pb=True)
#	print g,
#	children.Print()
#	#print children.p[0].Print()
#	parents = children

#for e in range(0,c.numEnvironments):

#	parents.p[0].Start_Evaluation(envs.envs[e],pp=False,pb=False)
#	parents.p[0].Compute_Fitness()	


