"""Initialize modules."""
from typing import Dict
import logging
from uun_iot.UuAppClient import UuAppClient
from .Heartbeat import Heartbeat
from .BaseHealthCheck import BaseHealthCheck

def init(config: Dict, uuclient: UuAppClient):

    def cmd_heartbeat(dto_in):
        uucmd = config["uuApp"]['uuCmdList']['gatewayHeartbeat']
        resp, exc = uuclient.post(uucmd, dto_in, log_level=logging.DEBUG)
        if exc is not None:
            return False
        return resp

    return [Heartbeat(cmd_heartbeat)]
