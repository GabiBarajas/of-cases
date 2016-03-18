This case is for a incompressible simplefoam case using kOmegaSST and 40m/s inlet velocity.

Software used for the case are

salome 7.7.1 (salome-platform.org) 

gmsh 2.12 (gmsh.info)

cfMesh 1.1.1 (cfmesh.com)

OpenFOAM-dev (15-03-2016)  (openfoam.org)

the Ahmed.py creates the 3D files, properties can be adjusted here eg. the slant angle.

the gmshToStl.sh converts the 3D files into a joined stl file for cfmesh.

the runMeshCase.sh file shows the commands to create the mesh and prepare for running.

