# coding=utf-8
import datetime
import logging

from management.rpc_client import RPCClient

from management.kv_store import DBController

logger = logging.getLogger()


def send_node_status_event(node_id, node_status):
    db_controller = DBController()
    logging.info(f"Sending event updates, node: {node_id}, status: {node_status}")
    node_status_event = {
        "timestamp": datetime.datetime.now().isoformat("T", "seconds") + 'Z',
        "event_type": "node_status",
        "UUID_node": node_id,
        "status": node_status}
    events = {"events": [node_status_event]}
    logger.debug(node_status_event)
    snodes = db_controller.get_storage_nodes()
    for node in snodes:
        if node.status != node.STATUS_ONLINE:
            continue
        logger.info(f"Sending to: {node.get_id()}")
        rpc_client = RPCClient(node.mgmt_ip, node.rpc_port, node.rpc_username, node.rpc_password)
        ret = rpc_client.distr_status_events_update(events)


def send_dev_status_event(storage_ID, dev_status):
    db_controller = DBController()
    logging.info(f"Sending event updates, device: {storage_ID}, status: {dev_status}")
    node_status_event = {
        "timestamp": datetime.datetime.now().isoformat("T", "seconds") + 'Z',
        "event_type": "device_status",
        "storage_ID": storage_ID,
        "status": dev_status}
    events = {"events": [node_status_event]}
    logger.debug(node_status_event)
    snodes = db_controller.get_storage_nodes()
    for node in snodes:
        if node.status != node.STATUS_ONLINE:
            continue
        logger.info(f"Sending to: {node.get_id()}")
        rpc_client = RPCClient(node.mgmt_ip, node.rpc_port, node.rpc_username, node.rpc_password)
        ret = rpc_client.distr_status_events_update(events)


def disconnect_device(device):
    db_controller = DBController()
    snodes = db_controller.get_storage_nodes()
    for node in snodes:
        if node.status != node.STATUS_ONLINE:
            continue
        new_remote_devices = []
        rpc_client = RPCClient(node.mgmt_ip, node.rpc_port, node.rpc_username, node.rpc_password)
        for rem_dev in node.remote_devices:
            if rem_dev.get_id() == device.get_id():
                ctrl_name = rem_dev.remote_bdev[:-2]
                rpc_client.bdev_nvme_detach_controller(ctrl_name)
            else:
                new_remote_devices.append(rem_dev)
        node.remote_devices = new_remote_devices
        node.write_to_db(db_controller.kv_store)
