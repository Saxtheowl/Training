# ############## PLEASE RUN THIS CELL FIRST! ###################

# # import everything and define a test runner function
# from importlib import reload
# from helper import run, little_endian_to_int
# from block import Block
# from io import BytesIO
# #from script# import Script
# import script
# import ecc
# import helper
# import tx

# #genesis coinbase scriptsig

# stream = BytesIO(bytes.fromhex('4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73'))

# #random block coinbase scriptsig

# stream2 = BytesIO(bytes.fromhex('03a1891d04e89f2760425443506f6f6cfabe6d6da0aefff9e18bf39db0132957d331a87713bdd0357ceed6613bd361d307086baa0100000000000000012d279ba3cc000000000000'))

# stream3 = BytesIO(bytes.fromhex('03a8891d20706f6f6c2e656e6a6f79626f646965732e636f6d2037383834636163346130b7ac702c467188000001'))

# #s = script.Script.parse(stream3)


############## PLEASE RUN THIS CELL FIRST! ###################

# import everything and define a test runner function
from importlib import reload
from helper import run
import network

from block import GENESIS_BLOCK
from helper import calculate_new_bits
from network import (
    NetworkEnvelope,
    VersionMessage,
)
