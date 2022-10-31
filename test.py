from datetime import datetime
from datetime import timedelta
import schedule
import time
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
my_address = ""
private_key = ""
nonce = web3.eth.getTransactionCount(my_address)


def cancelJob(job):
    schedule.cancel_job(job)


def get_decision(id):
    print(id)

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
