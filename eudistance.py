from scipy import spatial
import numpy
from sklearn.metrics.pairwise import euclidean_distances

import math

print('*** Program started ***')


######################################################################### Calculating distance by using  python math function
############################################################# 2 D array
x1 = [1,3,4,5,2]
x2 = [1,4,2,3,2]

######################################################################### Calculating distance by using scipy
eudistance = spatial.distance.euclidean(x1, x2)
print("eudistance Using scipy", eudistance)


######################################################################### Calculating distance by using numpy
x1np=numpy.array(x1)
x2np=numpy.array(x2)
eudistance = numpy.sqrt(numpy.sum((x1np-x2np)**2))
print("eudistance Using numpy", eudistance)

eudistance = numpy.linalg.norm(x1np-x2np)
print("eudistance Using numpy", eudistance)


######################################################################### Calculating distance by using sklearn
eudistance =  euclidean_distances([x1np], [x2np]) # for some strange reasons, values needs be in 2-D array
print("eudistance Using sklearn", eudistance)

print('*** Program ended ***')