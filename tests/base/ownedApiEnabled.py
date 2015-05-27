import unittest
from ethereum import tester
from ethertdd import FileContractStore

fs = FileContractStore("/build")

class OwnedApiEnabled(unittest.TestCase):
    def setUp(self):
        self.contract = fs.OwnedApiEnabled.create()

    def test_remove_fail_without_api(self):
        assert self.contract.remove(sender=tester.k2) is False

    def test_remove_without_api(self):
        assert self.contract.remove() is not False

    def test_set_api_address(self):
        permissions = fs.OwnedPermissionsProvider.create()
        api = fs.ProtectedApi.create()
        assert self.contract.setApiAddress()

    def test_remove_fail_without_api(self):
        assert self.contract.remove(sender=tester.k2) is False

