This case is for a incompressible simplefoam MRF case using kOmegaSST and 0.001 m3/s inlet flow.

Software used for the case are

python + numpy

salome 7.7.1 (salome-platform.org) 

gmsh 2.12 (gmsh.info)

cfMesh 1.1.1 (cfmesh.com)

OpenFOAM-dev (15-03-2016)  (openfoam.org)

the Allrun.msh creates the 3D files, and mesh, correct paths to salome and gmsh must be set.
also cfmesh-1.1.1 should be sourced for creating the mesh.

the Allrun.pre joins the mesh together and creates the boundary conditions, this should be run with OF-dev sourced.

the Allrun file decomposes the case and solves using simpleFoam.

