import unittest
from ethereum import tester
from ethertdd import FileContractStore

fs = FileContractStore("/build")

class Owned(unittest.TestCase):
    def setUp(self):
        self.contract = fs.Owned.create()

    def test_set_owner(self):
        original_owner = tester.a0.encode('hex')
        new_owner = tester.a1.encode('hex')
        not_owner = tester.k2

        # Make sure we actually know who owns this contract.
        assert self.contract.owner() == original_owner

        # Make sure non-owners cannot set a new owner.
        assert not self.contract.setOwner(new_owner, sender=not_owner)
        assert not self.contract.owner() == new_owner

        # Make sure the owner can set a new owner.
        assert self.contract.setOwner(new_owner)
        assert self.contract.owner() == new_owner
