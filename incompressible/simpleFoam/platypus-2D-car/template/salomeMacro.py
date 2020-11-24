# -*- coding: utf-8 -*-

import sys
import salome
import os
import pickle

fpath = os.path.dirname(sys.argv[0])

# INIT THE SALOME PART
salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, fpath)

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS

geompy = geomBuilder.New()

f = open('salomeInput.pkl', 'rb')
inputDict = pickle.load(f)
f.close()

r1 = inputDict['r1']
r2 = inputDict['r2']
r3 = inputDict['r3']
r4 = inputDict['r4']
r5 = inputDict['r5']
r6 = inputDict['r6']

# STL finenes
stlsize = 0.1

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_1 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)
sk = geompy.Sketcher2D()
sk.addPoint(0.000000, 0.000000)
sk.addSegmentAbsolute(0.000000, 67.000000)
sk.addSegmentAbsolute(50.000000, 67.000000)
sk.addSegmentAbsolute(67.000000, 114.000000)
sk.addSegmentAbsolute(200.000000, 114.000000)
sk.addSegmentAbsolute(205.000000, 67.000000)
sk.addSegmentAbsolute(242.000000, 67.000000)
sk.addSegmentAbsolute(242.000000, 0.000000)
sk.close()
Sketch_1 = sk.wire(geomObj_1)
Fillet_1D_1 = geompy.MakeFillet1D(Sketch_1, r1, [4])
Fillet_1D_2 = geompy.MakeFillet1D(Fillet_1D_1, r2, [6])
Fillet_1D_3 = geompy.MakeFillet1D(Fillet_1D_2, r3, [6])
Fillet_1D_4 = geompy.MakeFillet1D(Fillet_1D_3, r4, [6])
Fillet_1D_5 = geompy.MakeFillet1D(Fillet_1D_4, r5, [6])
Fillet_1D_6 = geompy.MakeFillet1D(Fillet_1D_5, r6, [6])
Extrusion_1 = geompy.MakePrismVecH(Fillet_1D_6, OZ, 5)
geomObj_2 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)
sk = geompy.Sketcher2D()
sk.addPoint(-500.000000, -50.000000)
sk.addSegmentAbsolute(-500.000000, 600.000000)
sk.addSegmentAbsolute(2000.000000, 600.000000)
sk.addSegmentAbsolute(2000.000000, -50.000000)
sk.close()
Sketch_2 = sk.wire(geomObj_2)
Extrusion_2 = geompy.MakePrismVecH(Sketch_2, OZ, 5)
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_2, geompy.ShapeType["FACE"])
inlet = geompy.CreateGroup(Extrusion_2, geompy.ShapeType["FACE"])
geompy.UnionIDs(inlet, [2])
slipTop = geompy.CreateGroup(Extrusion_2, geompy.ShapeType["FACE"])
geompy.UnionIDs(slipTop, [12])
outlet = geompy.CreateGroup(Extrusion_2, geompy.ShapeType["FACE"])
geompy.UnionIDs(outlet, [19])
wallGround = geompy.CreateGroup(Extrusion_2, geompy.ShapeType["FACE"])
geompy.UnionIDs(wallGround, [26])
geompy.ExportSTL(Extrusion_1, "wallCarMesh.stl", True, stlsize, False)
geompy.ExportSTL(inlet, "inletMesh.stl", True, stlsize, False)
geompy.ExportSTL(slipTop, "slipTopMesh.stl", True, stlsize, False)
geompy.ExportSTL(outlet, "outletMesh.stl", True, stlsize, False)
geompy.ExportSTL(wallGround, "wallGroundMesh.stl", True, stlsize, False)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Sketch_1, 'Sketch_1' )
geompy.addToStudy( Fillet_1D_1, 'Fillet 1D_1' )
geompy.addToStudy( Fillet_1D_2, 'Fillet 1D_2' )
geompy.addToStudy( Fillet_1D_3, 'Fillet 1D_3' )
geompy.addToStudy( Fillet_1D_4, 'Fillet 1D_4' )
geompy.addToStudy( Fillet_1D_5, 'Fillet 1D_5' )
geompy.addToStudy( Fillet_1D_6, 'Fillet 1D_6' )
geompy.addToStudy( Extrusion_1, 'Extrusion_1' )
geompy.addToStudy( Sketch_2, 'Sketch_2' )
geompy.addToStudy( Extrusion_2, 'Extrusion_2' )
geompy.addToStudyInFather( Extrusion_2, inlet, 'inlet' )
geompy.addToStudyInFather( Extrusion_2, slipTop, 'slipTop' )
geompy.addToStudyInFather( Extrusion_2, outlet, 'outlet' )
geompy.addToStudyInFather( Extrusion_2, wallGround, 'wallGround' )

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)