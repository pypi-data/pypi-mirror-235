import os
from .runtime_info import get_node_id

storage_dir = os.path.join(".storage", get_node_id())
