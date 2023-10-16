import os

import yaml

conf_str = os.environ.get('DORA_RUNTIME_CONFIG')

if not conf_str:
    raise Exception(f"DORA_RUNTIME_CONFIG is not set, please check")


def load_dora_runtime_config():
    return yaml.safe_load(conf_str)


_runtime_config = yaml.safe_load(conf_str)

dataflow_id = _runtime_config['node']['dataflow_id']
node_id = _runtime_config['node']['node_id']
run_config = _runtime_config['node']['run_config']
