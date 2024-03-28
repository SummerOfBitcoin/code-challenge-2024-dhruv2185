
# This file contains functions to validate transactions.
import hashlib
import struct


def getValidatedTransactions(transactions):
    validatedTransactions = []
    for transaction in transactions:
        if isValid(transaction):
            validatedTransactions.append(transaction)
    return validatedTransactions


def isValid(transaction):
    if not verifyInputOutputValues(transaction):
        return False
    return True

# This function verifies that the total output value of a transaction is less than or equal to the total input value.


def verifyInputOutputValues(transaction):
    totalInputValue = sum(vin['prevout']['value']
                          for vin in transaction.vin)
    totalOutputValue = sum(vout['value'] for vout in transaction.vout)
    return totalOutputValue <= totalInputValue


def serialize_transaction(transaction):
    serialized = b''

    # Serialize version number (4 bytes, little-endian)
    serialized += struct.pack('<I', transaction['version'])

    # Serialize number of inputs (varint format)
    serialized += encode_varint(len(transaction['vin']))

    # Serialize each input (vin)
    for vin in transaction['vin']:
        # Reverse txid bytes (little-endian)
        serialized += bytes.fromhex(vin['txid'])[::-1]
        # Serialize vout index (4 bytes, little-endian)
        serialized += struct.pack('<I', vin['vout'])
        # Serialize script length (varint format)
        serialized += encode_varint(len(vin['scriptsig']))
        # Serialize scriptSig
        serialized += bytes.fromhex(vin['scriptsig'])
        # Serialize sequence number (4 bytes, little-endian)
        serialized += struct.pack('<I', vin['sequence'])

    # Serialize number of outputs (varint format)
    serialized += encode_varint(len(transaction['vout']))

    # Serialize each output (vout)
    for vout in transaction['vout']:
        # Serialize value (8 bytes, little-endian)
        serialized += struct.pack('<Q', vout['value'])
        # Serialize script length (varint format)
        serialized += encode_varint(len(vout['scriptpubkey']))
        # Serialize scriptPubKey
        serialized += bytes.fromhex(vout['scriptpubkey'])

    # Serialize locktime (4 bytes, little-endian)
    serialized += struct.pack('<I', transaction['locktime'])

    return serialized


def encode_varint(value):
    if value < 0xfd:
        return struct.pack('<B', value)
    elif value <= 0xffff:
        return b'\xfd' + struct.pack('<H', value)
    elif value <= 0xffffffff:
        return b'\xfe' + struct.pack('<I', value)
    else:
        return b'\xff' + struct.pack('<Q', value)
