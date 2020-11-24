This case is for a incompressible simplefoam 2D optimisation problem of a simple car with 1m/s inlet flow.

Software used for the case are

python + numpy

platypus (https://github.com/Project-Platypus/Platypus)

salome 9.5.0 (salome-platform.org) 

OpenFOAM (v2006)  (openfoam.com)

the optimise.py runs all the commands and cases. 
Correct paths must be set here for OpenFOAM and salome. 

The optimisation problem have one objective (drag) and 6 variables (radii).

the pv.py file can be used with paraviews pvpython to generate the images of the car.


