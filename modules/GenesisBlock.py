#!/usr/bin/env python
import datetime as date
from Block import Block

# We create a first genesis block in the chain.

def generate_genesis_block():
    #manually construct a block with index 0 and random previous hash
    return Block(0, date.datetime.now(), "Genesis Block", "0")


