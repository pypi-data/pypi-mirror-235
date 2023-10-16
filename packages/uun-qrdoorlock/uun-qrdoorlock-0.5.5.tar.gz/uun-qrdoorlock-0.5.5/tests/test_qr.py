import pytest
import os
import pty

test_data_connection = "AaBbCc123QR"

class TestDataProcessing:
    @pytest.fixture(scope="class")
    def config_object(self, sconn, msg_generator):
        return {
            "gateway": {
                "virtualMode": True,
                "qrLock": {
                    "publicKey": msg_generator[0],
                    "qrReaderSerialDev": os.ttyname(sconn.sfd),
                    "lockOpenInterval": 2,
                    "lockType": "SZLDS92"
                }
            }
        }

    @pytest.fixture(scope="class")
    def init_modules(self, config_object):
        from uun_qrdoorlock.modules.QrLock import QrLock
        def uucmd(x):
            return []
        return QrLock(config=config_object["gateway"], uucmd=(uucmd,None)) # get public key, send uucmd

    def test_connection(self, init_modules, qr_reader_dev):
        """ Test connection to qr reader by forcing it to read a QR code and send it to client app. """
        qrlock = init_modules
        qr_code = test_data_connection

        # send a scanned qr code to the slave serial port - our tested application
        # no need to write to fifo
        qr_reader_dev.send_qr_to_slaves(qr_code) 

        # receive
        data = qrlock._qrreader.read()
        assert data == bytes(test_data_connection, 'ascii')

    def test_qr_code_processing(self, init_modules, msg_generator):
        """ Test if values are correctly decoded from QR code. """
        qrlock = init_modules
        valid, keycode, qr_code = msg_generator[1]

        # processed values
        pvalid, pkey = qrlock._process_and_validate_qr(qr_code)

        assert pvalid == valid
        if valid:
            assert pkey == keycode

    def test_qr_code_processing_bad_code(self, init_modules, msg_generator):
        """ Test if changing char in valid code results in invalid code. """
        qrlock = init_modules
        valid, keycode, qr_code = msg_generator[1]

        if not valid:
            return

        # change the signed message slightly
        ql = list(qr_code)
        ql[15] = '2' if ql[15] != '2' else '3'
        qr_code = "".join(ql)

        # processed values
        pvalid, pkey = qrlock._process_and_validate_qr(qr_code)

        assert pvalid == False
