import logging

from uun_iot import UuAppClient

from .GuardMan import GuardMan


def init(config: dict, uuclient: UuAppClient):
    def uucmd_get_progress_data(code):
        json_data = {"code": code}
        uucmd = config["uuApp"]["uuCmdList"]["guardManProgressGet"]
        return uuclient.get(uucmd, json_data, log_level=logging.DEBUG)

    return GuardMan(config["gateway"], uucmd_get_progress_data)
