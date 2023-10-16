import unittest
from pyappi.client import use_test_client, RealtimeHttpClient
from pyappi.client.sync import RawClientEvents, UserChanges
import time

#https://www.bing.com/search?pglt=161&q=fastapi+test+file+upload&cvid=5a67e0bf46164170b316959b92701fa3&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDkwNTNqMGoxqAIAsAIA&FORM=ANNTA1&PC=ASTS
#https://github.com/tiangolo/fastapi/issues/1536
"""_test_upload_file = Path('/usr/src/app/tests/files', 'new-index.json')
    _files = {'upload_file': _test_upload_file.open('rb')}
    with TestClient(app) as client:
        response = client.post('/_config',
                                files=_files)
        assert response.status_code == HTTPStatus.CREATED

    # remove the test file from the config directory
    _copied_file = Path('/usr/src/app/config', 'new-index.json')
    _copied_file.unlink()
"""


class TestSync(unittest.TestCase):
    def setUp(self):
        use_test_client()

        RealtimeHttpClient("test_sync").delete()

    def test_tail(self):
        with UserChanges(interval=.3):

            time.sleep(1)

            with RealtimeHttpClient("test_sync") as doc:
                u = doc.update

                u.nested.value = "CAsfawojgaw"
                u.name = "TEST"
                u.here = "HERE"

            time.sleep(1)

            self.assertTrue(True)
 
    def test_events(self):
        update = None
        def handler(_update, _parent):
            nonlocal update
            update = _update

        service = RawClientEvents(handler, interval=.3)

        time.sleep(1)

        with RealtimeHttpClient("test_sync") as doc:
            u = doc.update

            u.nested.value = "CAsfawojgaw"
            u.name = "TEST"
            u.here = "HERE"

        while update is None:
            time.sleep(.3)

        self.assertIsNotNone(update.get("test_sync",None))

        service.stop()


if __name__ == "__main__":
    unittest.main()
