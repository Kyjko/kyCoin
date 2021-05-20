import json
import hashlib
import time
from typing import List


class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []

    def get_last_block(self) -> "Block":
        return self.chain[-1]

    def add_block(self, block) -> None:
        if len(self.chain) > 0:
            block.prev = self.get_last_block().hash
        else:
            block.prev = "none"
        self.chain.append(block)

    def __str__(self):
        os: str = ""
        for b in self.chain:
            os += str(b)

        return os


class Block:
    def __init__(self, transactions: List["Transaction"], index: int):
        self.transactions: List["Transaction"] = transactions
        self.time = time.time()
        self.prev: str = ''
        self.index = index
        self.hash: str = self.calculate_hash()

    def calculate_hash(self) -> str:
        hash_transactions = ""
        for tr in self.transactions:
            hash_transactions += tr.hash

        hash_str = str(self.time) + hash_transactions + self.prev + str(self.index)
        hash_enc = json.dumps(hash_str, sort_keys=True).encode()
        return hashlib.sha256(hash_enc).hexdigest()

    def __str__(self):
        os: str = str(self.time) + "\n" + self.prev + "\n" + str(self.index) + "\n" + self.hash
        for tr in self.transactions:
            os += str(tr)
            os += "\n"

        return os


class Transaction:
    def __init__(self, sender: str, receiver: str, amount: float):
        self.sender: str = sender
        self.receiver: str = receiver
        self.amount: float = amount
        self.time = time.time()
        self.hash: str = self.calculate_hash()

    def __str__(self):
        return self.sender + "\n" + self.receiver + \
               "\n" + str(self.amount) + "\n" + str(self.time) + "\n" + self.hash

    def calculate_hash(self) -> str:
        hash_str = self.sender + self.receiver + str(self.amount) + str(self.time)
        hash_enc = json.dumps(hash_str, sort_keys=True).encode()
        return hashlib.sha256(hash_enc).hexdigest()