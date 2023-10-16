import logging

from uun_iot import UuAppClient

from .WindSurfGuru import WindSurfGuru


def init(config, uuclient: UuAppClient):
    def uucmd_get_last_data(code):
        json_data = {"code": code}
        uucmd = config["uuApp"]["uuCmdList"]["weatherConditionsGetLast"]
        return uuclient.get(uucmd, json_data, log_level=logging.DEBUG)

    return WindSurfGuru(config["gateway"], uucmd_get_last_data)
