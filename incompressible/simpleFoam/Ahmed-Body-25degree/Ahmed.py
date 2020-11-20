# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v7.7.1 with dump python functionality
###

import sys
import salome
import os

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS

# STL finenes
stlsize = 0.1

ahmedLength = 1044
ahmedWidth = 389
ahmedLegHeight = 50
ahmedBodyHeight = 288
ahmedSlantAngle = 25
ahmedslantLength = 222
ahmedFrontFilletRadius = 100
legpositionx1 = -372
legpositionx2 = -842
legpositiony = -163.5
legRadius = 15

domainMultiplierBeforeBody = 3
domainMultiplierAfterBody = 3
domainMultiplierWidth = 3
domainMultiplierHeight = 3


geompy = geomBuilder.New(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Vertex_1 = geompy.MakeVertex(0, 0, ahmedLegHeight)
Vertex_2 = geompy.MakeVertex(-ahmedLength, -ahmedWidth/2, ahmedLegHeight+ahmedBodyHeight)
Box_1 = geompy.MakeBoxTwoPnt(Vertex_1, Vertex_2)
Vertex_3 = geompy.MakeVertex(legpositionx1, legpositiony, 0)
Vertex_4 = geompy.MakeVertex(legpositionx2, legpositiony, 0)
Cylinder_1 = geompy.MakeCylinder(Vertex_4, OZ, legRadius, ahmedLegHeight)
Cylinder_2 = geompy.MakeCylinder(Vertex_3, OZ, legRadius, ahmedLegHeight)
Fillet_1 = geompy.MakeFillet(Box_1, ahmedFrontFilletRadius, geompy.ShapeType["EDGE"], [5, 8, 12])

angleInRadians = math.radians(90-ahmedSlantAngle) 
chamferHeight = math.cos(angleInRadians)*ahmedslantLength

Chamfer_1 = geompy.MakeChamferEdgeAD(Fillet_1, chamferHeight, angleInRadians, 42, 47)
Fuse_1 = geompy.MakeFuseList([Cylinder_1, Cylinder_2, Chamfer_1], True, True)
Vertex_5 = geompy.MakeVertex(ahmedLength*domainMultiplierAfterBody, 0, 0)
Vertex_6 = geompy.MakeVertex(-ahmedLength-ahmedLength*domainMultiplierBeforeBody, -ahmedWidth*domainMultiplierWidth, (ahmedBodyHeight+ahmedLegHeight)*domainMultiplierHeight)
Box_2 = geompy.MakeBoxTwoPnt(Vertex_5, Vertex_6)
Cut_1 = geompy.MakeCutList(Box_2, [Fuse_1], True)

inlet = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(inlet, [3])
wallGround = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(wallGround, [45])
symmetry = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(symmetry, [25])
slipwallTop = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(slipwallTop, [20])
slipwallSide = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(slipwallSide, [13])
wallLegs = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(wallLegs, [100, 97])
wallFront = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(wallFront, [84, 106, 89, 79])
wallUnder = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(wallUnder, [68])
wallSlant = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(wallSlant, [56])
wallBehind = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(wallBehind, [63])
wallTop = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(wallTop, [94])
wallSide = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(wallSide, [103])
outlet = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(outlet, [54])

geompy.ExportSTL(wallGround, "./wallGroundMesh.stl", True, stlsize, False )
geompy.ExportSTL(inlet, "./inletMesh.stl", True, stlsize, False )
geompy.ExportSTL(symmetry, "./symmetryMesh.stl", True, stlsize, False )
geompy.ExportSTL(slipwallTop, "./slipwallTop.stl", True, stlsize, False )
geompy.ExportSTL(slipwallSide, "./slipwallSide.stl", True, stlsize, False )
geompy.ExportSTL(wallLegs, "./wallLegs.stl", True, stlsize, False )
geompy.ExportSTL(wallFront, "./wallFront.stl", True, stlsize, False )
geompy.ExportSTL(wallUnder, "./wallUnder.stl", True, stlsize, False )
geompy.ExportSTL(wallSlant, "./wallSlant.stl", True, stlsize, False )
geompy.ExportSTL(wallBehind, "./wallBehind.stl", True, stlsize, False )
geompy.ExportSTL(wallTop, "./wallTop.stl", True, stlsize, False )
geompy.ExportSTL(wallSide, "./wallSide.stl", True, stlsize, False )
geompy.ExportSTL(outlet, "./outletMesh.stl", True, stlsize, False )


geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Vertex_3, 'Vertex_3' )
geompy.addToStudy( Vertex_4, 'Vertex_4' )
geompy.addToStudy( Cylinder_1, 'Cylinder_1' )
geompy.addToStudy( Cylinder_2, 'Cylinder_2' )
geompy.addToStudy( Fillet_1, 'Fillet_1' )
geompy.addToStudy( Chamfer_1, 'Chamfer_1' )
geompy.addToStudy( Fuse_1, 'Fuse_1' )
geompy.addToStudy( Vertex_5, 'Vertex_5' )
geompy.addToStudy( Vertex_6, 'Vertex_6' )
geompy.addToStudy( Box_2, 'Box_2' )
geompy.addToStudy( Cut_1, 'Cut_1' )

geompy.addToStudyInFather( Cut_1, wallGround, 'wallGround' )
geompy.addToStudyInFather( Cut_1, inlet, 'inlet' )
geompy.addToStudyInFather( Cut_1, symmetry, 'symmetry' )
geompy.addToStudyInFather( Cut_1, slipwallTop, 'slipwallTop' )
geompy.addToStudyInFather( Cut_1, slipwallSide, 'slipwallSide' )
geompy.addToStudyInFather( Cut_1, wallLegs, 'wallLegs' )
geompy.addToStudyInFather( Cut_1, wallFront, 'wallFront' )
geompy.addToStudyInFather( Cut_1, wallUnder, 'wallUnder' )
geompy.addToStudyInFather( Cut_1, wallSlant, 'wallSlant' )
geompy.addToStudyInFather( Cut_1, wallBehind, 'wallBehind' )
geompy.addToStudyInFather( Cut_1, wallTop, 'wallTop' )
geompy.addToStudyInFather( Cut_1, wallSide, 'wallSide' )
geompy.addToStudyInFather( Cut_1, outlet, 'outlet' )



if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
