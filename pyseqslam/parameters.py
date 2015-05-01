from attrdict import AttrDict

def defaultParameters():

    params = AttrDict()

    # switches
    params.DO_PREPROCESSING = 1
    params.DO_RESIZE        = 0
    params.DO_GRAYLEVEL     = 1
    params.DO_PATCHNORMALIZATION    = 1
    params.DO_SAVE_PREPROCESSED_IMG = 0
    params.DO_DIFF_MATRIX   = 1
    params.DO_CONTRAST_ENHANCEMENT  = 1
    params.DO_FIND_MATCHES  = 1


    # parameters for preprocessing
    class DS: pass
    params.downsample = DS()
    params.downsample.size = [32, 64]  # height, width
    params.downsample.method = 'lanczos3'
    params.normalization.sideLength = 8
    params.normalization.mode = 1
            
    
    # parameters regarding the matching between images
    params.matching.ds = 10 
    params.matching.Rrecent=5
    params.matching.vmin = 0.8
    params.matching.vskip = 0.1
    params.matching.vmax = 1.2  
    params.matching.Rwindow = 10
    params.matching.save = 1
    params.matching.load = 1
    
    # parameters for contrast enhancement on difference matrix  
    params.contrastEnhancement.R = 10

    # load old results or re-calculate? save results?
    params.differenceMatrix.save = 1
    params.differenceMatrix.load = 1
    
    params.contrastEnhanced.save = 1
    params.contrastEnhanced.load = 1
    
    # suffix appended on files containing the results
    params.saveSuffix=''
    
    return params
