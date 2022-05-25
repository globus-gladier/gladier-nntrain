from gladier import GladierBaseTool


class TransferModel(GladierBaseTool):

    flow_definition = {
        'Comment': 'Transfer a file or directory in Globus',
        'StartAt': 'TransferModel',
        'States': {
            'TransferModel': {
                'Comment': 'Transfer a file or directory in Globus',
                'Type': 'Action',
                'ActionUrl': 'https://actions.automate.globus.org/transfer/transfer',
                'Parameters': {
                    'source_endpoint_id.$': '$.input.comp_endpoint',
                    'destination_endpoint_id.$': '$.input.dest_endpoint',
                    'transfer_items': [
                        {
                            'source_path.$': '$.input.mdl_path',
                            'destination_path.$': '$.input.dest_path',
                            'recursive': True,
                        }
                    ]
                },
                'ResultPath': '$.TransferModel',
                'WaitTime': 600,
                'End': True
            },
        }
    }

    flow_input = {}
    required_input = [
        'comp_endpoint',
        'mdl_path',
        'dest_endpoint',
        'dest_path',
    ]
