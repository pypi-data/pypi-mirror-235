# coding=utf-8
import logging
import os

import time
import sys


SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(SCRIPT_PATH, "../.."))

from management import constants, kv_store, utils, rpc_client
from management.controllers import events_controller


# configure logging
logger_handler = logging.StreamHandler(stream=sys.stdout)
logger_handler.setFormatter(logging.Formatter('%(asctime)s: %(levelname)s: %(message)s'))
logger = logging.getLogger()
logger.addHandler(logger_handler)
logger.setLevel(logging.DEBUG)

# get DB controller
db_controller = kv_store.DBController()

hostname = utils.get_hostname()
logger.info("Starting Distr event collector...")
logger.info(f"Node:{hostname}")
while True:
    time.sleep(constants.DISTR_EVENT_COLLECTOR_INTERVAL_SEC)

    snode = db_controller.get_storage_node_by_hostname(hostname)
    if not snode:
        logger.error("This node is not part of the cluster, hostname: %s" % hostname)
        continue

    client = rpc_client.RPCClient(
        snode.mgmt_ip,
        snode.rpc_port,
        snode.rpc_username,
        snode.rpc_password)

    events = client.distr_status_events_get()
    logger.info(f"Found events: {len(events)}")
    for ev in events:
        logger.debug(ev)
        event_type = ev['event_type']
        status = ev['status']
        events_controller.log_distr_event(snode.cluster_id, snode.get_id(), event_type, ev, status)
