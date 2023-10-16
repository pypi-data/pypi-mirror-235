import pytest
import time
import os

class TestPackageRun:
    @pytest.fixture(scope="class")
    def config_object(self, sconn, msg_generator):
        return {
            "gateway": {
                "virtualMode": True,
                "qrLock": {
                    "publicKey": msg_generator[0],
                    "qrReaderSerialDev": os.ttyname(sconn.sfd),
                    "lockOpenInterval": .5,
                    "lockType": "SZLDS92"
                }
            }
        }

    def test_config(self, gateway, msg_generator, qr_reader_dev):
        with gateway as g:
            valid, keycode, qr_code = msg_generator[1]
            qr_reader_dev.send_qr_to_slaves(qr_code)
            time.sleep(2)

            # change the signed message slightly
            ql = list(qr_code)
            ql[12] = '1'
            qr2 = "".join(ql)
            qr_reader_dev.send_qr_to_slaves(qr2)
            print("in", gateway.runev.is_set(), gateway.stopev.is_set())

        print(gateway.runev.is_set(), gateway.stopev.is_set())
        time.sleep(1)
