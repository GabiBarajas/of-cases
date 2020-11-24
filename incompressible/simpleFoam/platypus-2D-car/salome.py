# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 21:37:58 2014

@author: nl
"""

import pickle

def geometryAndMesh(*args,**kwargs):
    f = open(kwargs['caseDir']+'/salomeInput.pkl','wb')
    pickle.dump(kwargs, f)
    f.close()