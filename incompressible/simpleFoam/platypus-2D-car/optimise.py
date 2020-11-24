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
from platypus import NSGAII, Problem, Real

CASECOUNT=1


def fixBc(replaceDict):
    for line in 'constant/polyMesh/boundary':
        words = line.split()
        if wallObstacle in words:
            print(line)


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
    file_handle.close()



# =============================================================================
# 
# =============================================================================
def objfunc(x):
    print(x)
    
    global CASECOUNT
    
    os.chdir('workDir')
    
    caseDir='workdir_'+str(CASECOUNT)
    
    if os.path.exists(caseDir):
        print('Case Folder already exists, removing')
        rmdirCommand='rm -rf '+caseDir
        subprocess.call(rmdirCommand,shell=True)
        
    print(caseDir)
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
        f = np.mean(np.loadtxt('./postProcessing/forceCoeffs/0/coefficient.dat',comments='#',usecols=(1,),unpack=True)[:-10])
        print('drag =',f)
    except:
        f=0
        print('Case Failed')


    os.chdir('../..')
    
    CASECOUNT+=1
        
    return [f]
    

# =============================================================================
# 
# =============================================================================

# Instantiate Optimization Problem 
# Instantiate Optimization Problem 
problem = Problem(6, 1)
problem.directions[0] = Problem.MINIMIZE  
problem.types[0] = Real(1., 25.)
problem.types[1] = Real(1., 30.)
problem.types[2] = Real(1., 30.)
problem.types[3] = Real(1., 25.)
problem.types[4] = Real(1., 25.)
problem.types[5] = Real(1., 13.)

problem.function = objfunc


mkdirCommand='mkdir -p workDir'
subprocess.call(mkdirCommand,shell=True)

algorithm = NSGAII(problem, population_size=8, log_frequency=1)

#algorithm.initialize()
algorithm.run(5)

for solution in algorithm.result:
    print(solution.objectives)
