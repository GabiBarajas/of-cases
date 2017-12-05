# -*- coding: iso-8859-1 -*-

import math
import salome
import collections

# INIT THE SALOME PART
salome.salome_init()
theStudy = salome.myStudy
from salome.geom import geomBuilder
geompy = geomBuilder.New(theStudy)

# STD GLOBAL VECTORS, CENTER AND PLANES
O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Plane_X = geompy.MakePlane(O, OX, 1)
Plane_Y = geompy.MakePlane(O, OY, 1)
Plane_Z = geompy.MakePlane(O, OZ, 1)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Plane_X, 'Plane_X' )
geompy.addToStudy( Plane_Y, 'Plane_Y' )
geompy.addToStudy( Plane_Z, 'Plane_Z' )


def linspace(a, b, n=50):
    '''Function used to make a linspace between two floats\
    as numpy cannot be imported easily into Salome because of\
    some hooks.py import errors'''
    if n < 2:
        return b
    diff = (float(b) - a)/(n - 1)
    return [diff * i + a  for i in range(n)]

def readXfoilProfile(filename="naca0012.txt"):
    pList = []
    with open(filename) as f:
        for l in f:
            x,y = l.split()
            pList.append([float(x),float(y)])
    return pList

def makeCurveFromPoints(pList):
    
    vList = []
    for i in pList:
        v = geompy.MakeVertex(i[0]-0.5,i[1],0)
        vList.append(v)
   
    curve = geompy.MakeInterpol(vList, False, False)
    
    return curve


def makePropeller(skewLine,pitchLine,coordLine,profile,coordLengthAtHub,nBlades,hubFillet,hubRadius=100,propRadius=500,hubLength=300):
    nCurves = 11
    skewList = []
    pitchList = []
    coordList = []
        
    hubVert = geompy.MakeVertex(0,-hubLength*5/2.0,0)
    
    for i in linspace(0,1,nCurves):
        skewList.append(geompy.PointCoordinates(geompy.MakeVertexOnCurve(skewLine, i, True))[1])
        pitchList.append(geompy.PointCoordinates(geompy.MakeVertexOnCurve(pitchLine, i, True))[1])
        coordList.append(geompy.PointCoordinates(geompy.MakeVertexOnCurve(coordLine, i, True))[1])
        
    
    bladeList=[]
    
    for i,j in enumerate(linspace(hubRadius-2,propRadius,nCurves)):
        scaleFactor = coordLengthAtHub*coordList[i]
        scale = geompy.MakeScaleTransform(profile,None,scaleFactor)
        geompy.TranslateDXDYDZ(scale,0,0,j)
        geompy.Rotate(scale, OZ, pitchList[i]*math.pi/180.0)
        geompy.Rotate(scale, OY, skewList[i]*math.pi/180.0)
        
        cylinder = geompy.MakeCylinder(hubVert,OY,j,hubLength*5)
        geompy.Rotate(cylinder, OY, 180*math.pi/180.0)
        
        face = geompy.GetSubShape(cylinder, [3])
        projection = geompy.MakeProjection(scale, face)
        li = geompy.ExtractShapes(projection, geompy.ShapeType["EDGE"], True)
        bladeList.append(li[0])


    compound = geompy.MakeCompound(bladeList)
    
    geompy.addToStudy(compound, 'Propellercompound')
    
    filling = geompy.MakeFilling(compound, theMinDeg=3, theMaxDeg=6, theNbIter=2)
    
    #geompy.addToStudy(filling, 'Propellerblade')

    [Edge_1,Edge_2,Edge_3,Edge_4] = geompy.SubShapes(filling, [6, 3, 8, 10])
    Edge_3_vertex_3 = geompy.GetSubShape(Edge_3, [3])
    Edge_2_vertex_3 = geompy.GetSubShape(Edge_2, [3])
    Line_1 = geompy.MakeLineTwoPnt(Edge_3_vertex_3, Edge_2_vertex_3)
    Edge_3_vertex_2 = geompy.GetSubShape(Edge_3, [2])
    Edge_2_vertex_2 = geompy.GetSubShape(Edge_2, [2])
    Line_2 = geompy.MakeLineTwoPnt(Edge_3_vertex_2, Edge_2_vertex_2)
    
    trailList = [Line_1, Line_2, Edge_2, Edge_3]
    tipList = [Line_1,Edge_4]
    hubList = [Line_2,Edge_1]
    
    trailFace = geompy.MakeFaceWires(trailList, 0)
    tipFace = geompy.MakeFaceWires(tipList, 0)
    hubFace = geompy.MakeFaceWires(hubList, 0)
    
    
    shellList = [filling,trailFace,tipFace,hubFace]
    
    propellerShell = geompy.MakeShell(shellList)
    
    propellerSolid = geompy.MakeSolid(propellerShell)
    
    propellersSolids = geompy.MultiRotate1DNbTimes(propellerSolid, OY, nBlades)
    
    trailRefinementFaces = geompy.MultiRotate1DNbTimes(trailFace, OY, nBlades)
    
    #geompy.addToStudy(propellersSolids, 'PropellerBlades')
    
    hubStarPoint = geompy.MakeVertex(0,-hubLength/2.0,0)
    hubSolid = geompy.MakeCylinder(hubStarPoint,OY,hubRadius,hubLength)
    
    #geompy.addToStudy(hubSolid, 'Hub')
    
    hubFillet = geompy.MakeFilletAll(hubSolid, hubFillet)
    
    #geompy.addToStudy(hubFillet, 'HubFillet')
    
    finalPropeller = geompy.MakeFuseList([propellersSolids, hubFillet], True, True)
    
    #geompy.addToStudy(finalPropeller, 'Propeller')
    
    amiStarPoint = geompy.MakeVertex(0,-hubLength,0)
    amiDomain = geompy.MakeCylinder(amiStarPoint,OY,propRadius*1.1,hubLength*2)
    
    #geompy.addToStudy(amiDomain, 'amiDomain')
    
    cfdDomain = geompy.MakeCutList(amiDomain, [finalPropeller], True)
    
    geompy.addToStudy(cfdDomain, 'cfdDomain')
    
    propellerFaces = geompy.SubShapeAll(finalPropeller, geompy.ShapeType["FACE"])
    amiFaces = geompy.SubShapeAll(amiDomain, geompy.ShapeType["FACE"])
    
    propellerGroupIDs = []
    
    for i in propellerFaces:
        propellerGroupIDs.append(geompy.GetSameIDs(cfdDomain, i)[0])
        
    rotatingWallPropeller = geompy.CreateGroup(cfdDomain, geompy.ShapeType["FACE"])
    geompy.UnionIDs(rotatingWallPropeller, propellerGroupIDs)
    
    geompy.addToStudyInFather( cfdDomain, rotatingWallPropeller, 'rotatingWallPropeller' )
    
    geompy.ExportBREP(rotatingWallPropeller, "./Propeller/rotatingWallPropellerMesh.brep" )
    
    geompy.ExportBREP(trailRefinementFaces, "./Propeller/refineTrailFacesMesh.brep" )
    
    
    amiGroupIDs = []
    
    for i in amiFaces:
        amiGroupIDs.append(geompy.GetSameIDs(cfdDomain,i)[0])
    
    amiPropeller = geompy.CreateGroup(cfdDomain, geompy.ShapeType["FACE"])
    geompy.UnionIDs(amiPropeller,amiGroupIDs)
    
    geompy.addToStudyInFather(cfdDomain, amiPropeller, 'amiPropeller')
    
    geompy.ExportBREP(amiPropeller, "./Propeller/amiPropellerMesh.brep" )
    geompy.ExportBREP(amiPropeller, "./Domain/amiDomainMesh.brep" )
    
    
    outerCylinderStartPoint = geompy.MakeVertex(0,-propRadius*5,0)
    outerCylinder = geompy.MakeCylinder(outerCylinderStartPoint,OY,propRadius*4,propRadius*10)
    
    #geompy.addToStudy(outerCylinder, 'outerCylinder')
    
    outerDomain = geompy.MakeCutList(outerCylinder, [amiDomain], True)
    
    geompy.addToStudy(outerDomain, 'outerDomain')
    
    inlet = geompy.CreateGroup(outerDomain, geompy.ShapeType["FACE"])
    geompy.UnionIDs(inlet, [12])
    outlet = geompy.CreateGroup(outerDomain, geompy.ShapeType["FACE"])
    geompy.UnionIDs(outlet, [10])
    slipOuter = geompy.CreateGroup(outerDomain, geompy.ShapeType["FACE"])
    geompy.UnionIDs(slipOuter, [3])
    
    geompy.ExportBREP(inlet, "./Domain/inletMesh.brep" )
    geompy.ExportBREP(outlet, "./Domain/outletMesh.brep" )
    geompy.ExportBREP(slipOuter, "./Domain/slipOuterMesh.brep" )
    
    
    
       

def main():
    ## START OF PROGRAM
    profilePoints = readXfoilProfile("naca0022.txt") # make one from xfoil or use 1 of the 3 included
    profileCurve = makeCurveFromPoints(profilePoints)
    
    nBlades = 4 # Enter blade numbers [integer]
    hubRadius = 100 # radius of the hub [mm]
    hubFillet = 75 # fillet radius on the hub cylinder [mm]
    propRadius = 500 # final propeller radius [mm]
    hubLength = 300 # length of the hub [mm]
    coordLengthAtHub = 100 # the coord length at the hub [mm], the scaling is based on this length
    
    skewAngleList = [[0,0],[0.5,0],[1,20]] # these points are used to control the skewAngle [deg] you can add more but x values have to be in accending order from 0-1
    pitchAngleList = [[0,40],[0.2,20],[1,10]] # these points are used to control the pitchAngle [deg] you can add more but x values have to be in accending order from 0-1
    coordLengthScaleList = [[0,1],[0.5,2],[1,0.8]] # these points are used to control the coord scaling [float] you can add more but x values have to be in accending order from 0-1
    
    skewControlLine = makeCurveFromPoints(skewAngleList)
    pitchControlLine = makeCurveFromPoints(pitchAngleList)
    coordControlLine = makeCurveFromPoints(coordLengthScaleList)
    
    makePropeller(skewControlLine,pitchControlLine,coordControlLine,profileCurve,coordLengthAtHub,nBlades,hubFillet,hubRadius,propRadius,hubLength)

if __name__ == '__main__':
    main()
