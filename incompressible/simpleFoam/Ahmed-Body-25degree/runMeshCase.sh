#!/bin/bash

surfaceToFMS joined.stl

surfaceFeatureEdges -angle 80 joined.fms joined2.fms

transformPoints -scale "(0.001 0.001 0.001)"

createPatch -overwrite

# simpleFoam

