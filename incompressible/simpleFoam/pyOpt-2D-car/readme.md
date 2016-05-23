This case is for a incompressible simplefoam 2D optimisation problem of a simple car with 1m/s inlet flow.

Software used for the case are

python + numpy

pyOpt 1.2.4 (www.pyopt.org)

salome 7.7.1 (salome-platform.org) 

gmsh 2.12 (gmsh.info)

cfMesh 1.1.1 (cfmesh.com)

OpenFOAM-dev (20-05-2016)  (openfoam.org)

the optimise.py runs all the commands and cases. 
Correct paths must be set here for cfMesh, OpenFOAM and salome. 
gmsh should be avaliable in the path so you can run it from a terminal.

xdat can be used to make parallel plots after tweaking the output file from pyOpt.

The optimisation problem have one objective (drag) and 6 variables (radii).

the pv.py file can be used with paraviews pvpython to generate the images of the car.


