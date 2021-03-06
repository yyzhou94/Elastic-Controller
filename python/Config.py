"""
Configuration
"""
NODE_NUMBER_PER_SWITCH = 1      # N1-N5
CONTROLLERS = [
    {
        'name':"C1",
        'ip':'127.0.0.1',
        'port':6633
    },
    {
        'name':"C2",
        'ip':'127.0.0.1',
        'port':6634
    }
]                 # sn1 + sn2 = 8

SWITCHES = {
    'http://127.0.0.1:8081':['s','m','m','m','m','m','m','m'],
    'http://127.0.0.1:8080':['m','s','s','s','s','s','s','s']
}

SWITCH_NUMBER = 8



MONITOR = {
    "PORT":9200,
    "METHODS":{
        "STAT":["/stat","POST"],
        "FINISH_MIGRATION":["/change_topo","POST"],
        "TOPO_REPORT":["/report_topo","POST"]
    },
    "CHECK_INTERVAL":40         # seconds
}

CONTROLLER = {
    'STAT_SUBMIT_INTERVAL':2,
    'METHODS':{
        'INIT_ROLE':['/init_role','POST'], # because the util.Http_Request only use POST
        'START_MIGRATION':['/migrate','POST'],
	'MIGRATION_BEGIN':['/begin','POST'],
	'MIGRATION_READY':['/ready','POST'],
	'MIGRATION_END':['/end','POST']
    }
}



# USE_TOPO = 'cube'
USE_TOPO = 'tree'

TOPO = {}
TOPO['tree'] = [[1,2],[1,3],
                [2,4],[2,5],
                [3,6],[3,7],[3,8]];

TOPO['cube'] = [[1,2],[1,4],[1,5],
                [2,3],[2,6],
                [3,4],[3,7],
                [4,8],
                [5,6],[5,8],
                [6,7],
                [7,8]];



