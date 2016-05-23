#!/bin/bash
options="-format stl"

rm joined.stl

for filename in *.brep ## or *.stp, change clscale and clmin/clmax to refine/coarsen mesh, lower values result in finer mesh.
do
  echo $filename
  gmsh $filename -2 -o ./${filename%\.*}.stl $options -clscale 0.8 -clmin 1 -clmax 3;
  sed -i "s/Created by Gmsh/${filename%\.*}/g" "./${filename%\.*}.stl"
  cat "./${filename%\.*}.stl" >> "./joined.stl"
  rm "./${filename%\.*}.stl"  # to remove the individual stl files.
done;

