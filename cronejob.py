# # # # def do_nothing():
# # # #     print("hi")

# # # # schedule.every(10).seconds.do(do_nothing)

# # # # while 1:
# # # #     schedule.run_pending()
# # # #     time.sleep(1)

#

from datetime import datetime
from datetime import timedelta
import json
from unittest import result
from sqlalchemy import true
from web3 import Web3
import asyncio
import time
import schedule

infura_url = "https://kovan.infura.io/v3/bdb81d50d772462da07cda7afcf3f695"
web3 = Web3(Web3.HTTPProvider(infura_url))
factstation_factory = "0xfbcb89b8858B32bbC162447A263E8ca668933BCa"
file = open("FactStation.json")
data = json.load(file)
abi = data["abi"]
contract = web3.eth.contract(address=factstation_factory, abi=abi)
# print("posts")
# print(contract.functions.getTotalPosts().call())
# print(contract.functions.getPost(2).call())
# print(contract.functions.getPost(3).call())

chain_id = 42
my_address = "0xFbb9E1Be77d97BD94A98e5441125Ef2bC2031aed"
private_key = "0x1c05e5bfd4e7670d40b9be28df5794f77423df37131dce12ba9c11e1bf75e030"
nonce = web3.eth.getTransactionCount(my_address)


def get_decision(id):
    nonce = web3.eth.getTransactionCount(my_address)
    store_transaction = contract.functions.decision(id).buildTransaction(
        {
            "chainId": chain_id,
            "from": my_address,
            "nonce": nonce,
            "gasPrice": web3.eth.gas_price,
        }
    )

    signed_store_txn = web3.eth.account.sign_transaction(
        store_transaction, private_key=private_key
    )
    send_store_tx = web3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
    print(send_store_tx)

    tx_receipt = web3.eth.wait_for_transaction_receipt(send_store_tx)
    print(tx_receipt)

    # sta = contract.functions.getPost(1).call()
    # print(sta)
    return


def cancelJob(job):
    schedule.cancel_job(job)


def handle_event(event):

    # print(Web3.toJSON(event))
    result = Web3.toJSON(event)
    y = json.loads(result)
    if (
        y["topics"][0]
        == "0xc396b8fdad1e5f78ba6abcfa6e1a1244dde7dd0d69b78d45d3ad8dbe35653a8e"
    ):

        print("---------------")
        print(y)
        ans = y["topics"][1]
        # print(final)
        id = int(ans, 0)
        print(id)
        # contract.functions.decision(id).call()
        print("hey")
        # time.sleep(300)
        current_time = datetime.now()
        n = 2
        future_time = current_time + timedelta(minutes=n)
        future_time_str = future_time.strftime("%H:%M:%S")
        job = schedule.every().day.at(future_time_str).do(get_decision, id=id)
        future_time = future_time + timedelta(minutes=1)
        future_time_str = future_time.strftime("%H:%M:%S")
        schedule.every().day.at(future_time_str).do(cancelJob, job=job)

        # job = schedule.every(900).seconds.do(get_decision(id))


def log_loop(event_filter, poll_interval):
    for event in event_filter.get_new_entries():
        handle_event(event)
        time.sleep(poll_interval)


def main():
    block_filter = web3.eth.filter(
        {"fromBlock": "latest", "address": factstation_factory}
    )
    while True:
        schedule.run_pending()
        log_loop(block_filter, 2)


if __name__ == "__main__":
    main()
