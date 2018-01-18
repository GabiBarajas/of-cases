# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v8.3.0 with dump python functionality
###

import sys
import os
import inspect
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)
scriptFileLocation = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print(scriptFileLocation)
os.chdir(scriptFileLocation)
sys.path.insert( 0, scriptFileLocation)

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Disk_1 = geompy.MakeDiskR(25, 2)
geomObj_1 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)
geomObj_2 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)
sk = geompy.Sketcher2D()
sk.addPoint(0.000000, 0.000000)
sk.addSegmentRelative(200.000000, 0.000000)
sk.addArcAngleRadiusLength(0, 75.000000, 90.000000)
sk.addSegmentAngleLength(0, 500.000000)
Sketch_1 = sk.wire(geomObj_2)
Vertex_1 = geompy.MakeVertex(253, 22, 0)
Disk_2 = geompy.MakeDiskPntVecR(Vertex_1, OY, 15)
Extrusion_1 = geompy.MakePrismVecH(Disk_2, OY, -200)
Pipe_1 = geompy.MakePipe(Disk_1, Sketch_1)
Fuse_1 = geompy.MakeFuseList([Extrusion_1, Pipe_1], True, True)
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Fuse_1, geompy.ShapeType["FACE"])
inletLarge = geompy.CreateGroup(Fuse_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(inletLarge, [30])
inletSmall = geompy.CreateGroup(Fuse_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(inletSmall, [3])
outlet = geompy.CreateGroup(Fuse_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(outlet, [32])
wallLarge = geompy.CreateGroup(Fuse_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(wallLarge, [25, 20, 12])
wallSmall = geompy.CreateGroup(Fuse_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(wallSmall, [7])
Face_1 = geompy.MakeFaceHW(60, 330, 3)
geompy.TranslateDXDYDZ(Face_1, 145, -185, 0)
Extrusion_2 = geompy.MakePrismVecH(Face_1, OY, 775)
[v4,v1,v8,v5,v3,v2,v7,v6] = geompy.ExtractShapes(Extrusion_2, geompy.ShapeType["VERTEX"], True)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Disk_1, 'Disk_1' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Disk_2, 'Disk_2' )
geompy.addToStudy( Extrusion_1, 'Extrusion_1' )
geompy.addToStudy( Sketch_1, 'Sketch_1' )
geompy.addToStudy( Pipe_1, 'Pipe_1' )
geompy.addToStudy( Fuse_1, 'Fuse_1' )
geompy.addToStudyInFather( Fuse_1, inletLarge, 'inletLarge' )
geompy.addToStudyInFather( Fuse_1, inletSmall, 'inletSmall' )
geompy.addToStudyInFather( Fuse_1, outlet, 'outlet' )
geompy.addToStudyInFather( Fuse_1, wallLarge, 'wallLarge' )
geompy.addToStudyInFather( Fuse_1, wallSmall, 'wallSmall' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Extrusion_2, 'Extrusion_2' )
geompy.addToStudyInFather( Extrusion_2, v4, 'v4' )
geompy.addToStudyInFather( Extrusion_2, v1, 'v1' )
geompy.addToStudyInFather( Extrusion_2, v8, 'v8' )
geompy.addToStudyInFather( Extrusion_2, v5, 'v5' )
geompy.addToStudyInFather( Extrusion_2, v3, 'v3' )
geompy.addToStudyInFather( Extrusion_2, v2, 'v2' )
geompy.addToStudyInFather( Extrusion_2, v7, 'v7' )
geompy.addToStudyInFather( Extrusion_2, v6, 'v6' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New(theStudy)
Mesh_1 = smesh.Mesh(Fuse_1)
NETGEN_1D_2D_3D = Mesh_1.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D)
NETGEN_3D_Parameters_1 = NETGEN_1D_2D_3D.Parameters()
NETGEN_3D_Parameters_1.SetMaxSize( 10 )
NETGEN_3D_Parameters_1.SetSecondOrder( 0 )
NETGEN_3D_Parameters_1.SetOptimize( 1 )
NETGEN_3D_Parameters_1.SetFineness( 3 )
NETGEN_3D_Parameters_1.SetMinSize( 0.1 )
NETGEN_3D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_3D_Parameters_1.SetFuseEdges( 1 )
NETGEN_3D_Parameters_1.SetQuadAllowed( 0 )
NETGEN_3D_Parameters_1.SetLocalSizeOnShape(inletSmall, 2)
NETGEN_3D_Parameters_1.SetLocalSizeOnShape(outlet, 3)
NETGEN_3D_Parameters_1.SetLocalSizeOnShape(wallLarge, 3)
NETGEN_3D_Parameters_1.SetLocalSizeOnShape(wallSmall, 2)
NETGEN_3D_Parameters_1.SetLocalSizeOnShape(inletLarge, 3)
isDone = Mesh_1.Compute()
inletLarge_1 = Mesh_1.GroupOnGeom(inletLarge,'inletLarge',SMESH.FACE)
inletSmall_1 = Mesh_1.GroupOnGeom(inletSmall,'inletSmall',SMESH.FACE)
outlet_1 = Mesh_1.GroupOnGeom(outlet,'outlet',SMESH.FACE)
wallLarge_1 = Mesh_1.GroupOnGeom(wallLarge,'wallLarge',SMESH.FACE)
wallSmall_1 = Mesh_1.GroupOnGeom(wallSmall,'wallSmall',SMESH.FACE)
try:
  print(os.getcwd())
  Mesh_1.ExportUNV( scriptFileLocation+'/elbow.unv' )
  pass
except:
  print 'ExportUNV() failed. Invalid file name?'

## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D_3D.GetAlgorithm(), 'NETGEN 1D-2D-3D')
smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(wallSmall_1, 'wallSmall')
smesh.SetName(wallLarge_1, 'wallLarge')
smesh.SetName(outlet_1, 'outlet')
smesh.SetName(inletSmall_1, 'inletSmall')
smesh.SetName(inletLarge_1, 'inletLarge')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)
