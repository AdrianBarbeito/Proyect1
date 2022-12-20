from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'cTqBnC3WcNLhjY5jMYN3W86n9qLWHNHNP14xtHeSFFt2TiYPf3i6')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cTosVYKpSohFi5gCn492hNNPPTa2osramcbHE2Ysh9AsTjBckxe9')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cP9nZ1VirKwg6Az8xCMEDtnzzYSQVTNLdvw8mDaj7Vj3aSbprMu3')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

Q3a_txout_scriptPubKey = [
OP_2, my_public_key, cust1_public_key, cust2_public_key, cust3_public_key, OP_4, OP_CHECKMULTISIG]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00054584-0.000004545 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        'f853c0e293144db43146781187fdd354422d454d')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, 
        utxo_index, Q3a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
