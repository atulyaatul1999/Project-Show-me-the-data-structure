import hashlib
from datetime import datetime as dt


class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = self.get_utc_time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.data)
        self.next = None

    def get_utc_time(self):
        return dt.now()

    def calc_hash(self,str):
        sha = hashlib.sha256()
        str = str.encode('utf-8')
        sha.update(str)
        return sha.hexdigest()


class Blockchain:

    def __init__(self):
        self.root = None

    def add_block(self, data):

        if self.root == None:
            self.root = Block(data, 0)

        else:
            current = self.root

            while current.next:
                current = current.next

            previous_hash = current.hash
            current.next = Block(data, previous_hash)

    def print_Blockchain(self):

        if self.root == None:
            print("There is no block!")
            return
        else:
            current = self.root
            index = 0
            print("blockchain is-")
            while current:
                print("Index:", index)
                print("Timestamp:", current.timestamp)
                print("Data:", current.data)
                print("SHA256 Hash:", current.hash)
                print("Prev_Hash:", current.previous_hash)
                current = current.next
                index += 1
            print("")
            print("")


mycoin = Blockchain()
mycoin.add_block("block1")
mycoin.add_block("block2")
mycoin.add_block("block3")
mycoin.add_block("block4")
mycoin.print_Blockchain()
# here we will get the blockchain with 4 blocks
mycoin.add_block("block5")
mycoin.add_block("block6")
mycoin.add_block("block7")
mycoin.add_block("block8")
mycoin.print_Blockchain()
#now we will get the output of 8 blocks in blockchain


bitcoin = Blockchain()
bitcoin.add_block("this_is_block1")
bitcoin.add_block("this_is_block2")
bitcoin.print_Blockchain()
#here we get the output of bitcoin blockchain with 2 blocks

None_coin=Blockchain()
None_coin.print_Blockchain()
# as there is no block in our blockchain so it will return There is no block!



