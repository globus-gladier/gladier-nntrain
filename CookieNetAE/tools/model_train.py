from gladier import GladierBaseTool, generate_flow_definition

def model_train(train_wdir, train_cmde, **data):
    import subprocess, os

    os.chdir(train_wdir) 

    cmd = train_cmde.split('#')

    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             shell=True, executable='/bin/bash')

    return str(res.stdout), str(res.stderr)

@generate_flow_definition(modifiers={
    model_train: {'endpoint': 'fx_ep_train'}
})
class ModelTrain(GladierBaseTool):
    funcx_functions = [model_train]
    required_input = [
        'train_wdir',
        'train_cmde', 
        'fx_ep_train'
        ]


