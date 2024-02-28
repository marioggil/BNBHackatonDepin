from general import extractConfig
from web3 import Web3
rcpopbnb=extractConfig(nameModel="SystemData",dataOut="rcpopbnb")
import time, json
from datetime import datetime
web3 = Web3(Web3.HTTPProvider(rcpopbnb))


def getStatusRcp():
    return web3.is_connected()


def getBalanceWallet(address):
    balance = web3.eth.get_balance(address)
    balanceT = web3.from_wei(balance,"ether")
    return { "balance": balanceT}

def getBlock(number):
    return dict(web3.eth.get_block(number))

def getLastNumberBlock():
    Block=getBlock('latest')
    return Block["number"]

def getTransaction(hash):
    return dict(web3.eth.get_transaction(hash))

def getAllTransactionOfBlock(id):
    Block=getBlock(id)
    output=[]
    txs=Block['transactions']
    for tx in txs:
        output.append(getTransaction(tx))
    return output


class Transaction:
      
   'blockNumber','hash','from',"to",'gas','gasPrice','input','value','type','nonce','transactionIndex','v','r','s','mint'

class Block2:
    def __init__(self,number):
        self.number=number
        block=getBlock(number)
        self.hash=block["hash"].hex()
        self.miner=block["miner"]
        self.difficulty=block["difficulty"]
        self.gasLimit=block["gasLimit"]
        self.gasUsed=block["gasUsed"]
        self.timestamp=block["timestamp"]
        self.size=block["size"]
        self.totalDifficulty=block["totalDifficulty"]
        self.baseFeePerGas=block["baseFeePerGas"]
        self.transactions=block["transactions"]
        self.uncles=block["uncles"]
        self.year=datetime.fromtimestamp(self.timestamp).year
        self.month=datetime.fromtimestamp(self.timestamp).month
        self.day=datetime.fromtimestamp(self.timestamp).day
        self.hour=datetime.fromtimestamp(self.timestamp).hour
        self.minute=datetime.fromtimestamp(self.timestamp).minute
        self.Ntxs=len(self.transactions)
        self.Nuncles=len(self.uncles)
    def getDict(self):

        return self.__dict__
    def saveDb(self):
        pass



class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")