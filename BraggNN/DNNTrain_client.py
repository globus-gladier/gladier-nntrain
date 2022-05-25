#!/usr/bin/env python

##Basic Python import's
import argparse
import yaml

##Base Gladier imports
from gladier import GladierBaseClient, generate_flow_definition

#debugging messages
#import gladier.tests

##Import tools that will be used on the flow definition
from tools.transfer_data import TransferData
from tools.model_train import ModelTrain
from tools.transfer_model import TransferModel

##Generate flow based on the collection of `gladier_tools` 
@generate_flow_definition
class DNN_Train_Client(GladierBaseClient):
    globus_group = '0bbe98ef-de8f-11eb-9e93-3db9c47b68ba'
    gladier_tools = [
        TransferData,
        ModelTrain,
        TransferModel,
    ]

def create_input_cfg(cfg):
    wf_cfg = yaml.load(open(cfg, 'r'), Loader=yaml.CLoader)
        
    flow_args = {
        "input": {
            ##local globus ep
            "data_endpoint": wf_cfg['src_data_fabric']['UUID'],
            "data_path": wf_cfg['src_data_fabric']['PATH'],
            ##remote globus ep
            "comp_endpoint":wf_cfg['dst_data_fabric']['UUID'],
            "comp_path":wf_cfg['dst_data_fabric']['PATH'],
            "mdl_path":wf_cfg['src_model_fabric']['PATH'],
            ##final?? globus ep
            "dest_endpoint": wf_cfg['dst_model_fabric']['UUID'],
            "dest_path": wf_cfg['dst_model_fabric']['PATH'],
            ##Funcx endpoints
            "funcx_endpoint_compute": wf_cfg['computing_fabric']['EUUID'],
            ##Train params
            'wdir': wf_cfg['computing_fabric']['WDIR'],
            'cmde': wf_cfg['computing_fabric']['TrCMD']
        }
    }
    return flow_args

def train_flow(cfg):
   ##The first step Client instance
    trainClient = DNN_Train_Client()

    if cfg==None:
        print("bad cfg")
        return
    else:
        flow_input = create_input_cfg(cfg)
    
    client_run_label = 'Gladier BraggNN Example'

    flow_run = trainClient.run_flow(flow_input=flow_input, label=client_run_label)

    print('Run started with ID: ' + flow_run['action_id'])
    print('https://app.globus.org/runs/' + flow_run['action_id'])

##  Arguments for the execution of this file as a stand-alone client
def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help='YAML config File', default=None)
    return parser.parse_args()

## Main execution of this "file" as a Standalone client
if __name__ == '__main__':

    args = arg_parse()
    train_flow(args.config)