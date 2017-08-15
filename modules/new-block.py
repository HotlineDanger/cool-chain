#!/usr/bin/env python

def next_block(last_block):
    block_id = last_block.index + 1
    block_timestamp = date.datetime.now()
    block_data = "Block " + str(block_id)
    block_hash = last_block.hash

    return Block(block_id, block_timestamp, block_data, block_hash)


