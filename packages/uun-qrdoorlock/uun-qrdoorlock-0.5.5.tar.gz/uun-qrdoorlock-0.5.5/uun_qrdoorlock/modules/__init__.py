import logging

from uun_iot import UuAppClient

from .QrLock import QrLock


def init(config: dict, uuclient: UuAppClient):
    gconfig = config["gateway"]

    def cmd_get_public_key():
        # will be replaced by placing the publicKey directly into main configuration by server
        try:
            uucmd = config["uuApp"]["uuCmdList"]["getPublicKey"]
            return uuclient.get_ignore_http_err(uucmd)
        except KeyError:
            return None

    def cmd_send_used_qr(storage):
        failed = []
        uucmd = config["uuApp"]["uuCmdList"]["qrcodeLog"]
        for stuple in storage:
            (keycode, timestamp) = stuple
            dto_in = {"keyCode": keycode, "usageTs": timestamp}
            _, exc = uuclient.post(uucmd, dto_in, log_level=logging.DEBUG)
            if exc is not None:
                failed.append(stuple)

        return failed

    def cmd_send_doormonitor(storage):
        uucmd = "TODO"

    ret = [QrLock(gconfig, (cmd_send_used_qr, cmd_get_public_key))]
    # DoorMonitor is totally disabled in virtual mode
    if not gconfig["virtualMode"]:
        from .DoorMonitor import DoorMonitor

        ret.append(DoorMonitor(gconfig, cmd_send_doormonitor))

    return ret
