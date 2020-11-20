#!/usr/bin/env python
'''
'''

# =============================================================================
# Standard Python modules
# =============================================================================
import os, sys, time, subprocess, re
import pdb

import numpy as np

import salome

# =============================================================================
# Extension modules
# =============================================================================
#from pyOpt import *
from pyOpt import Optimization
from pyOpt import NSGA2


CASECOUNT=1


def fixBc(replaceDict):
    for line in 'constant/polyMesh/boundary':
        words = line.split()
        if wallObstacle in words:
            print line


def replace(fileIn,searchBC,subst):
    # Read contents from file as a single string
    file_handle = open(fileIn,'r')
    file_string = file_handle.read()
    file_handle.close()
    
    pattern=searchBC+'\n+\s*\{\n\s*type\s*(.+?)\;'
    subst = (searchBC+'\n\t{\n\t\ttype\t\t\t'+subst+';').expandtabs(4)
    # Use RE package to allow for replacement (also allowing for (multiline) REGEX)
    file_string = (re.sub(pattern, subst, file_string))

    # Write contents to file.
    # Using mode 'w' truncates the file.
    file_handle = open(fileIn, 'w')
    file_handle.write(file_string)
    file_handle.close()com



# =============================================================================
# 
# =============================================================================
def objfunc(x):
    print x
    
    global CASECOUNT
    
    os.chdir('workDir')
    
    caseDir='workdir_'+str(CASECOUNT)
    
    if os.path.exists(caseDir):
        print 'Case Folder already exists, removing'
        rmdirCommand='rm -rf '+caseDir
        subprocess.call(rmdirCommand,shell=True)
        
    print caseDir
    mkdirCommand='mkdir -p '+caseDir
    subprocess.call(mkdirCommand,shell=True)
    copyTemplateCase='cp -r ../template/* '+caseDir+'/'
    subprocess.call(copyTemplateCase,shell=True)
    
    salome.geometryAndMesh(r1=x[0],r2=x[1],r3=x[2],r4=x[3],r5=x[4],r6=x[5],caseDir=caseDir)
    
    os.chdir(caseDir)
    
    runSalomeCommand='xterm -e "module load salome/9.5.0 && salome start -t --server-launch-mode=fork --shutdown-servers=1 salomeMacro.py"'
    subprocess.call(runSalomeCommand,shell=True)
    
    createStl='xterm -e "./renameStl.sh"'
    subprocess.call(createStl,shell=True)
    
    createMesh='xterm -e "module load openfoam/com/20.06 && surfaceToFMS joined.stl && surfaceFeatureEdges -angle 80 joined.fms joined2.fms && cartesian2DMesh"'
    subprocess.call(createMesh,shell=True)
    
    setupCase='xterm -e bash -c \'module load openfoam/com/20.06 && transformPoints -scale "(0.001 0.001 0.001)" && createPatch -overwrite\''
    subprocess.call(setupCase,shell=True)
    
    
    runSimul='xterm -e "module load openfoam/com/20.06 && simpleFoam 2>&1 | tee log.simpleFoam"'
    subprocess.call(runSimul,shell=True)
#    
    try:
        f = np.mean(np.loadtxt('postProcessing/forceCoeffs/0/forceCoeffs.dat',skiprows=10,usecols=(2,),unpack=True)[:-10])
        print "drag =",f
        fail = 0
        g=[]
    except:
        f=0
        g=[]
        fail=1

    os.chdir('../..')
    
    CASECOUNT+=1
        
    return f,g,fail
    

# =============================================================================
# 
# =============================================================================

# Instantiate Optimization Problem 
opt_prob = Optimization('Minimize Drag',objfunc)
opt_prob.addVar('x1','c',lower=1.,upper=25.,value=12.0)
opt_prob.addVar('x2','c',lower=1.,upper=30.,value=15.0)
opt_prob.addVar('x3','c',lower=1.,upper=30.,value=15.0)
opt_prob.addVar('x4','c',lower=1.,upper=25.,value=12.0)
opt_prob.addVar('x5','c',lower=1.,upper=25.,value=12.0)
opt_prob.addVar('x6','c',lower=1.,upper=13.,value=6.0)
opt_prob.addObj('f')
#opt_prob.addCon('g','i')
print opt_prob

mkdirCommand='mkdir -p workDir'
subprocess.call(mkdirCommand,shell=True)

# Instantiate Optimizer (NSGA2) & Solve Problem
nsga2 = NSGA2()
nsga2.setOption('PopSize',8)
nsga2.setOption('maxGen',5)
nsga2.setOption('PrintOut',2)
nsga2(opt_prob,store_hst=True)
print opt_prob.solution(0)
