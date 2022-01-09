from blockchain import Blockchain

block_one_transactions = {"sender": "Alice", "receiver": "Bob", "amount": "50"}
block_two_transactions = {"sender": "Bob", "receiver": "Cole", "amount": "25"}
block_three_transactions = {"sender": "Alice", "receiver": "Cole", "amount": "35"}
fake_transactions = {"sender": "Bob", "receiver": "Cole, Alice", "amount": "25"}

local_blockchain = Blockchain()
local_blockchain.print_blocks()

# can also add the 3 dicts in a list, i.e.
# my_blockchain.add_block(new_transactions)
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.print_blocks()

local_blockchain.chain[2].transactions = fake_transactions
local_blockchain.validate_chain()
