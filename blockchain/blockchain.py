# from https://www.geeksforgeeks.org/create-simple-blockchain-using-python/
import datetime
import hashlib
import json

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block 
    
    def print_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()

            if hash_operation[:5] == '00000':
                check_proof = True
            else:
                new_proof += 1
        
        return new_proof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block)
                return False
            
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()

            if hash_operation[:5] != '00000':
                return False
            previous_block = block
            block_index += 1
        
        return True

# CLI vs. server?? 
blockchain = Blockchain()

def mine():
    previous_block = blockchain.print_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)

    response = {'message': 'A block was mined',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    
    console.log(response)

def display():
    response = {'chain': blockchain.chain, 'length': len(blockchain.chain)}
    console.log(response)

def valid():
    valid = blockchain.chain_valid(blockchain.chain)

    if valid:
        response = {'message': 'The blockchain is valid.'}
    else:
        response = {'message': 'The blockchain is not valid.'}

    console.log(response)

# mine
# display chain
# check validity

def usage():
    print("Usage:")
    print("mine")
    print("display")
    print("verify ")
    sys.exit(1)

if len(sys.argv) != 1:
    usage()
elif sys.argv[1] == 'mine':
    mine()
elif sys.argv[1] == 'display':
    display()
elif sys.argv[1] == 'sign':
    verify()
else:
    usage()