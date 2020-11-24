#!/opt/Paraview-5.0.1/bin/pvpython

try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

import os
import numpy as np

i=1

for direc in sorted(os.listdir('workDir/'),key = lambda x: int(x.split("_")[1])):
    
    os.chdir('workDir/'+direc)
    print os.getcwd()
    
    # create a new 'OpenFOAMReader'
    #casefoam = OpenFOAMReader(FileName='/home/nl/openfoam-cases/incompressible/simpleFoam/pyOpt-2D-car/workDir/workdir_1/case.foam')
    casefoam = OpenFOAMReader( FileName='./case.foam' )
    casefoam.MeshRegions = ['internalMesh']
    casefoam.CellArrays = ['U', 'epsilon', 'k', 'nut', 'p']

    # get animation scene
    animationScene1 = GetAnimationScene()

    # update animation scene based on data timesteps
    animationScene1.UpdateAnimationUsingDataTimeSteps()

    animationScene1.GoToLast()

    # Properties modified on casefoam
    casefoam.CellArrays = ['U']

    # get active view
    renderView1 = GetRenderView()
    # uncomment following to set a specific view size
    renderView1.ViewSize = [1611, 796]

    # show data in view
    casefoamDisplay = Show(casefoam, renderView1)
    # trace defaults for the display properties.
    #casefoamDisplay.ColorArrayName = [None, '']
    #casefoamDisplay.GlyphType = 'Arrow'
    #casefoamDisplay.ScalarOpacityUnitDistance = 0.06534395462396458
    #casefoamDisplay.SetScaleArray = [None, '']
    #casefoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    #casefoamDisplay.OpacityArray = [None, '']
    #casefoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    casefoamDisplay.ScaleTransferFunction.Points = [-6.5099101066589355, 0.0, 0.5, 0.0, 5.212724685668945, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    casefoamDisplay.OpacityTransferFunction.Points = [-6.5099101066589355, 0.0, 0.5, 0.0, 5.212724685668945, 1.0, 0.5, 0.0]

    # reset view to fit data
    #renderView1.ResetCamera()

    ## set scalar coloring
    #ColorBy(casefoamDisplay, ('FIELD', 'vtkBlockColors'))

    # show color bar/color legend
    casefoamDisplay.SetScalarBarVisibility(renderView1, True)

    # set scalar coloring
    #ColorBy(casefoamDisplay, ('POINTS', 'U'))

    # rescale color and/or opacity maps used to include current data range
    casefoamDisplay.RescaleTransferFunctionToDataRange(True)

    # show color bar/color legend
    casefoamDisplay.SetScalarBarVisibility(renderView1, False)

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.16171788078172056, 0.0816585843735611, 0.5091341213497879]
    renderView1.CameraFocalPoint = [0.16171788078172056, 0.0816585843735611, 0.0024999999441206455]
    renderView1.CameraParallelScale = 1.291561557956286
    
    caseNum = 'case_'+str(i).zfill(3)
    f = np.mean(np.loadtxt('postProcessing/forceCoeffs/0/forceCoeffs.dat',skiprows=10,usecols=(2,),unpack=True)[:-10])
    
    # create a new '3D Text'
    a3DText1 = a3DText()
    a3DText2 = a3DText()
    a3DText1.Text = caseNum
    a3DText2.Text = 'cd ='+str("{0:.3f}".format(f))
    # show data in view
    a3DText1Display = Show(a3DText1, renderView1)
    a3DText2Display = Show(a3DText2, renderView1)
    
    # Properties modified on a3DText1Display
    a3DText1Display.Scale = [0.01, 0.01, 0.05]
    a3DText2Display.Scale = [0.01, 0.01, 0.05]
    
    # Properties modified on a3DText1Display
    a3DText1Display.Origin = [0.01, 0.01, 0.005]
    a3DText2Display.Origin = [0.1, 0.01, 0.005]
    
    SaveScreenshot('../../'+caseNum+'.png', magnification=1, quality=100, view=renderView1)
    
#    Delete(AnimationScene1)
#    Delete(a1_p_PVLookupTable)
#    Delete(a1_p_PiecewiseFunction)
#    Delete(DataRepresentation1)
    Delete(casefoam)
    Delete(a3DText1)
    Delete(a3DText2)
#    Delete(RenderView1)
    Render()
    
    os.chdir('../..')
    i+=1



