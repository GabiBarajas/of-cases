#!/bin/bash

# Use cfmesh here #

surfaceToFMS joined.stl

surfaceFeatureEdges -angle 80 joined.fms joined2.fms

cartesianMesh

# Use cfmesh or OF here

transformPoints -scale "(0.001 0.001 0.001)"

# Use OF here

createPatch -overwrite

# simpleFoam

