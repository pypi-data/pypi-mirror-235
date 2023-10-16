import os

from loguru import logger
from .runtime_info import node_id, dataflow_id

logger = logger.opt()
log_rotation = os.getenv("log_rotation", "1 day")
log_retention = os.getenv("log_retention", "7 days")

log_path = os.path.join(".logs", dataflow_id, node_id, "node.log")
logger.add(log_path, rotation=log_rotation, retention=log_retention)
