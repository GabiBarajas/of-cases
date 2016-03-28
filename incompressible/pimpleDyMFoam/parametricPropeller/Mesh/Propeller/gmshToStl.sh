#!/bin/bash
options="-format stl"

rm joined.stl

for filename in *.brep ## or *.stp, change clscale and clmin/clmax to refine/coarsen mesh, lower values result in finer mesh.
do
  echo $filename
  if [[ "$filename" == rotating* ]] || [[ "$filename" == refine* ]]; 
  then
     gmsh $filename -2 -o ./${filename%\.*}.stl $options -clscale 0.8 -clmin 2 -clmax 5;
  elif [[ "$filename" == ami* ]]; 
  then
     gmsh $filename -2 -o ./${filename%\.*}.stl $options -clscale 1 -clmin 5 -clmax 20;
  else
     gmsh $filename -2 -o ./${filename%\.*}.stl $options -clscale 2 -clmin 20 -clmax 50;
  fi
  
  
  sed -i "s/Created by Gmsh/${filename%\.*}/g" "./${filename%\.*}.stl"
  
  if [[ "$filename" != refine* ]]; 
  then
     cat "./${filename%\.*}.stl" >> "./joined.stl"
     rm "./${filename%\.*}.stl"  # to remove the individual stl files.
  fi
  
done;

