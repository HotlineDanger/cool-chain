#!/usr/bin/env python

from Block import Block
from datetime import datetime

def next_block(last_block):
    block_id = last_block.index + 1
    block_timestamp = datetime.now()
    block_data = "Block " + str(block_id)
    block_hash = last_block.hash

    return Block(block_id, block_timestamp, block_data, block_hash)


