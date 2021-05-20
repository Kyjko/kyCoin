from blockchain import Blockchain, Block, Transaction
import time

if __name__ == "__main__":
    b = Blockchain()
    tr1 = Transaction("kyjko0777", "badapple01", 100.0)
    tr2 = Transaction("hasherbox", "megachad", 35346)
    b.add_block(Block([tr1, tr2], 0))

    print(b)
