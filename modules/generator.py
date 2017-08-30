#!/usr/bin/env python

# this piece of code is in charge of creatng blocks for our blockchain
# we create the blockhain before adding the first block - the genesis block

import GenesisBlock
import NewBlock

blockchain = [GenesisBlock.generate_genesis_block()]
previous_block = blockchain[0]
number_of_blocks = 25

# We add the blocks to the chain
for x in range(0, number_of_blocks):
    block_to_add = NewBlock.next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add

    # print the current block to the blockchain
    print("Block #{} has been added to the blockchain!".format(block_to_add.index))
    print("Hash: {}\n".format(block_to_add.hash))
