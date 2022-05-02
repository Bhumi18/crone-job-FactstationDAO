# import json
# from unittest import result
# from web3 import Web3
# import asyncio
# import time
# import schedule

# infura_url = "https://kovan.infura.io/v3/bdb81d50d772462da07cda7afcf3f695"
# web3 = Web3(Web3.HTTPProvider(infura_url))
# factstation_factory = "0x5Be6F27D7cEa370fEe2086fbEe61C86BD4f8566B"
# file = open("FactStation.json")
# data = json.load(file)
# abi = data["abi"]
# contract = web3.eth.contract(address=factstation_factory, abi=abi)
# # print("posts")
# print(contract.functions.getTotalPosts().call())

# chain_id = 42
# my_address = "0xFbb9E1Be77d97BD94A98e5441125Ef2bC2031aed"
# private_key = "0x1c05e5bfd4e7670d40b9be28df5794f77423df37131dce12ba9c11e1bf75e030"
# nonce = web3.eth.getTransactionCount(my_address)
# store_transaction = contract.functions.decision(1).buildTransaction(
#     {
#         "chainId": chain_id,
#         "from": my_address,
#         "nonce": nonce,
#         "gasPrice": web3.eth.gas_price,
#     }
# )

# signed_store_txn = web3.eth.account.sign_transaction(
#     store_transaction, private_key=private_key
# )
# send_store_tx = web3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
# print(send_store_tx)

# tx_receipt = web3.eth.wait_for_transaction_receipt(send_store_tx)
# print(tx_receipt)

# sta = contract.functions.getPost(1).call()
# print(sta)

from datetime import datetime
from datetime import timedelta
import schedule
import time


# def get_d():
#     print("hi")


# current_time = datetime.now()
# n = 2
# future_time = current_time + timedelta(minutes=n)
# future_time_str = future_time.strftime("%H:%M:%S")
# print(current_time)
# print(future_time)
# (print(future_time_str))
# # schedule.every().day.at(future_time_str).do(get_d())
# schedule.every(100).seconds.do(get_d())


# while True:
#     schedule.run_pending()
#     time.sleep(1)

import schedule
import time
from web3 import Web3
import json

infura_url = "https://kovan.infura.io/v3/bdb81d50d772462da07cda7afcf3f695"
web3 = Web3(Web3.HTTPProvider(infura_url))
factstation_factory = "0x5Be6F27D7cEa370fEe2086fbEe61C86BD4f8566B"
file = open("FactStation.json")
data = json.load(file)
abi = data["abi"]
contract = web3.eth.contract(address=factstation_factory, abi=abi)
# print("posts")
print(contract.functions.getTotalPosts().call())


chain_id = 42
my_address = "0xFbb9E1Be77d97BD94A98e5441125Ef2bC2031aed"
private_key = "0x1c05e5bfd4e7670d40b9be28df5794f77423df37131dce12ba9c11e1bf75e030"
nonce = web3.eth.getTransactionCount(my_address)


def cancelJob(job):
    schedule.cancel_job(job)


def get_decision(id):
    print(id)
    # nonce = web3.eth.getTransactionCount(my_address)
    # store_transaction = contract.functions.decision(id).buildTransaction(
    #     {
    #         "chainId": chain_id,
    #         "from": my_address,
    #         "nonce": nonce,
    #         "gasPrice": web3.eth.gas_price,
    #     }
    # )

    # signed_store_txn = web3.eth.account.sign_transaction(
    #     store_transaction, private_key=private_key
    # )
    # send_store_tx = web3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
    # print(send_store_tx)

    # tx_receipt = web3.eth.wait_for_transaction_receipt(send_store_tx)
    # print(tx_receipt)

    # # sta = contract.functions.getPost(1).call()
    # # print(sta)
    # return schedule.CancelJob


current_time = datetime.now()
n = 1
future_time = current_time + timedelta(minutes=n)
future_time_str = future_time.strftime("%H:%M:%S")
print(current_time)
print(future_time)
(print(future_time_str))

for i in range(2):
    current_time = datetime.now()
    n = 2
    future_time = current_time + timedelta(minutes=n)
    future_time_str = future_time.strftime("%H:%M:%S")
    job = schedule.every().day.at(future_time_str).do(get_decision, id=4)
    future_time = future_time + timedelta(minutes=1)
    future_time_str = future_time.strftime("%H:%M:%S")
    schedule.every().day.at(future_time_str).do(cancelJob, job=job)
    time.sleep(60)

while True:
    schedule.run_pending()
    time.sleep(1)
