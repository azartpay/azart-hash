import azart_hash
from binascii import unhexlify, hexlify

import unittest

# azart block #1
# dev@a1:~/.azartcore$ azartd getblockhash 1
# 0000044ce2afe736c7e6a2d2cf6eedd5f21299f80700aba9e27640582531a78a
# dev@a1:~/.azartcore$ azartd getblock 0000044ce2afe736c7e6a2d2cf6eedd5f21299f80700aba9e27640582531a78a
#{
#  "hash": "0000044ce2afe736c7e6a2d2cf6eedd5f21299f80700aba9e27640582531a78a",
#  "confirmations": 727,
#  "size": 179,
#  "height": 1,
#  "version": 536870912,
#  "merkleroot": "9b21ce49e532d803c29ee1396871630a0bed298479a9a7323eac50c88941c903",
#  "tx": [
#    "9b21ce49e532d803c29ee1396871630a0bed298479a9a7323eac50c88941c903"
#  ],
#  "time": 1526562640,
#  "mediantime": 1526562640,
#  "nonce": 71865,
#  "bits": "1e0fffff",
#  "difficulty": 0.0002441371325370145,
#  "chainwork": "0000000000000000000000000000000000000000000000000000000000200011",
#  "previousblockhash": "000009b9903dae4466d48db6c264d711ac554492da34cd0bfa4c0b6d230f29c9",
#  "nextblockhash": "000002a0288fa36fd12f76703a68729dc50d140581d150965cdd1df83c7cfe21"
#}

header_hex = ("02000000" +
    "b67a40f3cd5804437a108f105533739c37e6229bc1adcab385140b59fd0f0000" +
    "a71c1aade44bf8425bec0deb611c20b16da3442818ef20489ca1e2512be43eef"
    "814cdb52" +
    "f0ff0f1e" +
    "dbf70100")

best_hash = '434341c0ecf9a2b4eec2644cfadf4d0a07830358aed12d0ed654121dd9070000'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_azart_hash(self):
        self.pow_hash = hexlify(azart_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash.decode(), self.best_hash)


if __name__ == '__main__':
    unittest.main()

