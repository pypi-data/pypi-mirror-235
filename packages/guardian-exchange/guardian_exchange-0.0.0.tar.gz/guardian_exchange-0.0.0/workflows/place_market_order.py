import string
import asyncio
import logging
import random
import inspect
import time
from queue import Queue
from dataclasses import dataclass
from datetime import timedelta
from typing import List

from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker


@dataclass
class AcquireMatchLockInput:
    market_id: int
    market_side: str
    order_id: int
    amount: str


@dataclass
class SimpleInput:
    market_id: str
    order_id: str


TASK_QUEUE_NAME = "place-market-order-task-queue"
market_orders_queue = Queue()


# While we could use multiple parameters in the activity, Temporal strongly
# encourages using a single dataclass instead which can have fields added to it
# in a backwards-compatible way.
@dataclass
class MarketOrderInput:
    id: int
    user_id: int
    currency_in_id: int
    currency_in_symbol: str
    amount_in: int  # UINT 512 bit
    currency_out_id: int
    currency_out_symbol: str

    # amount_out: int = None
    # status: str = "new"
    # initial_amount: int = None
    # id: int = None


@dataclass
class MarketOrderOutput:
    id: int
    user_id: int
    currency_in_id: int
    currency_in_symbol: str
    amount_in: int  # UINT 512 bit
    currency_out_id: int
    currency_out_symbol: str


# Basic activity that logs and does string concatenation
@activity.defn
async def match_order_and_lock_balances(input: dict) -> bool:
    activity.logger.info(f"Running '{inspect.stack()[0][3]}' activity with: {input}")

    from guardian.connectors.balance_db import BalanceDBConnector, SettleWorkflowInput, Settlements
    from guardian.connectors.clob import CLOBConnector
    from guardian.connectors.ome import OMEConnector

    client = await Client.connect("localhost:7233")
    balancedb = BalanceDBConnector(client)
    ome = OMEConnector(client)
    clob = CLOBConnector(client)

    # output = await ome.match_market_order(input)
    # if not output.matched_market_orders:
    #     return False
    match_acitivity_input = input.get("match_order_and_lock_balances_input")
    output = await ome.match_lock_acquire(match_acitivity_input)
    time.sleep(1)
    settls = []
    if output.get('error') == '':
        for match in output.get('spec').get('matches'):
            print(match)
            await balancedb.lock_amount("1+USD", match.get("amount"))
            await balancedb.lock_amount("3+EUR", f"{int(match.get('amount')) * int(match.get('price'))//100}")
            settls.append(Settlements("3+EUR", f"{int(match.get('amount')) * int(match.get('price'))//100}",
                                      "3+USD", match.get("amount")))
            time.sleep(1)
    else:
        return False
    lock_execute_input = SimpleInput(match_acitivity_input.get("market_id"), match_acitivity_input.get("order_id"))
    await ome.match_lock_execute(lock_execute_input)
    time.sleep(1)
    settle_input = SettleWorkflowInput(
        f"{input.get('market_order').get('user_id')}+{input.get('market_order').get('currency_in_symbol')}",
        f"{input.get('market_order').get('user_id')}+{input.get('market_order').get('currency_out_symbol')}",
        settls)
    await balancedb.settle(settle_input)
    return True
    # await balancedb.settle(output.spec, )

    # results = await asyncio.gather(
    #     balancedb.lock_liquidity(output.matched_market_orders, input.currency_out_symbol),
    #     clob.lock_liquidity(output.matched_market_orders, input.currency_out_symbol)
    # )
    # print(f"{inspect.stack()[0][3]}: {results}")
    # return all(results)


# @activity.defn
# async def lock_source_asset(input: MarketOrderInput) -> bool:
#     activity.logger.info(f"Running '{inspect.stack()[0][3]}' activity with: {input}")
#     from guardian.connectors.balance_db import BalanceDBConnector
#     from guardian.connectors.clob import CLOBConnector
#     from guardian.connectors.custodian import CustodianConnector
#     from guardian.connectors.ome import OMEConnector
#     client = await Client.connect("localhost:7233")
#     balancedb = BalanceDBConnector(client)
#     ome = OMEConnector(client)
#     clob = CLOBConnector(client)
#
#     output = await ome.match_market_order(input)
#     if not output.matched_market_orders:
#         return False
#
#     return True


# @activity.defn
# async def settle_order(input: MarketOrderInput) -> bool:
#     activity.logger.info(f"Running '{inspect.stack()[0][3]}' activity with: {input}")
#
#     from guardian.connectors.balance_db import BalanceDBConnector
#     from guardian.connectors.clob import CLOBConnector
#     from guardian.connectors.custodian import CustodianConnector
#     from guardian.connectors.ome import OMEConnector
#
#     client = await Client.connect("localhost:7233")
#     balancedb = BalanceDBConnector(client)
#     ome = OMEConnector(client)
#     clob = CLOBConnector(client)
#
#     output = await ome.match_market_order(input)
#     if not output.matched_market_orders:
#         return False
#
#     results = await asyncio.gather(
#         balancedb.settle(output.matched_market_orders, input.currency_out_symbol),
#     )
#     print(f"{inspect.stack()[0][3]}: {results}")
#     return all(results)


@activity.defn
async def test_credit() -> bool:
    from guardian.connectors.balance_db import BalanceDBConnector
    client = await Client.connect("localhost:7233")
    balancedb = BalanceDBConnector(client)
    results = await asyncio.gather(
        balancedb.test_workflow_credit(),
    )
    print(f"{inspect.stack()[0][3]}: {results}")
    return all(results)


@activity.defn
async def test() -> bool:
    from guardian.connectors.balance_db import BalanceDBConnector
    client = await Client.connect("localhost:7233")
    balancedb = BalanceDBConnector(client)
    results = await asyncio.gather(
        balancedb.test_workflow(),
    )
    # print(f"{inspect.stack()[0][3]}: {results}")
    return all(results)


@activity.defn
async def execute_on_chain_transfer(input: MarketOrderInput) -> bool:
    activity.logger.info(f"Running '{inspect.stack()[0][3]}' activity with: {input}")
    return True


# Basic workflow that logs and invokes an activity
@workflow.defn
class PlaceMarketOrderWorkflow:
    def __init__(self) -> None:
        self._greeting = "<no greeting>"

    @workflow.run
    async def run(self, input: dict) -> List[bool]:
        # Run activities at the same time
        # todo: remake to sync run
        results = await asyncio.gather(
            workflow.execute_activity(
                match_order_and_lock_balances,
                input,
                start_to_close_timeout=timedelta(seconds=5)
            ),
        )

        # Sort the results because they can complete in any order
        return list(sorted(results))


async def main():
    # Uncomment the line below to see logging
    logging.basicConfig(level=logging.INFO)

    # Start client
    client = await Client.connect("localhost:7233")

    id: int
    user_id: int
    currency_in_id: int
    currency_in_symbol: str
    amount_in: int  # UINT 512 bit
    currency_out_id: int
    currency_out_symbol: str

    market_order = MarketOrderInput(1, 1, 1, "USD", 100, 2, "EUR")
    match_order_and_lock_balances_input = AcquireMatchLockInput(1, "Bid", 6, "500")
    print("INPUT DATA")
    print(market_order)
    print(match_order_and_lock_balances_input)

    # Run a worker for the workflow
    async with Worker(
            client,
            task_queue=TASK_QUEUE_NAME,
            workflows=[PlaceMarketOrderWorkflow],
            activities=[
                match_order_and_lock_balances,
                # settle_order,
                execute_on_chain_transfer,
                test,
                test_credit
            ],
    ):
        workflow_name = "PlaceMarketOrderWorkflow"
        workflow_id = workflow_name + "".join(
            random.choices(string.ascii_uppercase + string.digits, k=6)
        )

        # While the worker is running, use the client to run the workflow and
        # print out its result. Note, in many production setups, the client
        # would be in a completely separate process from the worker.
        input = {
            "market_order": market_order,
            "account": "1+USD",
            "match_order_and_lock_balances_input": match_order_and_lock_balances_input
        }
        result = await client.execute_workflow(
            workflow=PlaceMarketOrderWorkflow.run,
            arg=input,
            id=workflow_id,
            task_queue=TASK_QUEUE_NAME,
        )

        print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
