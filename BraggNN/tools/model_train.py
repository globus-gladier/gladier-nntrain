from gladier import GladierBaseTool, generate_flow_definition

def model_train(wdir, cmde, **data):
    cmd_aug = cmde.split('#')
    import subprocess, os
    os.chdir(wdir) 
    result = subprocess.run(cmd_aug, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')


@generate_flow_definition
class ModelTrain(GladierBaseTool):
    funcx_functions = [model_train]
    required_input = [
        'wdir',
        'cmde', 
        'funcx_endpoint_compute'
        ]
