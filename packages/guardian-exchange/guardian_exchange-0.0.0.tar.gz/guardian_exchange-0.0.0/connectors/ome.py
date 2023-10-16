from dataclasses import dataclass
from typing import List
import random
import string
import inspect

from temporalio.client import Client

TASK_QUEUE = "ome-task-queue"


@dataclass
class OMEMatch:
    market_maker_user_id: int
    limit_order_id: int
    source_currency_amount: int
    target_currency_amount: int


@dataclass
class OMEMatchOutput:
    matched_market_orders: List[OMEMatch]


@dataclass
class AcquireMatchLockInput:
    market_id: int
    market_side: str
    order_id: int
    amount: str


@dataclass
class Matches:
    limit_order_id: str
    amount: str
    price: str
    partial: bool


class ClobList:
    price: str
    depth: str
    locked: str


@dataclass
class Clob:
    bids: List[ClobList]
    asks: List[ClobList]


@dataclass
class AcquireMatchLockOutput:
    result: bool
    error: str
    spec: List[Matches]
    clob: Clob


@dataclass
class PlaceLimitOrderInput:
    market_id: str
    market_side: str
    order_id: str
    amount: str
    price: str
    account_id: str


@dataclass
class PlaceLimitOrderOutput:
    result: bool
    error: str
    clob: Clob


@dataclass
class SimpleInput:
    market_id: str
    order_id: str


class OMEConnector:
    """ Order Matching Engine connector """

    def __init__(self, client: Client):
        self.client = client

    # Acquire Match Lock for Market Order
    # async def match_market_order(self, input: MarketOrderInput) -> OMEMatchOutput:
    #
    #     workflow_name = "ome_wf_match_lock_acquire"
    #     workflow_id = workflow_name + "".join(
    #         random.choices(string.ascii_uppercase + string.digits, k=6)
    #     )
    #     # Run workflow
    #     output = await self.client.execute_workflow(
    #         workflow_name,
    #         input,
    #         id=workflow_id,
    #         task_queue=TASK_QUEUE
    #     )
    #
    #     # TODO: we get dicts, need proper encoding to dataclasses
    #     if "matched_market_orders" in output:
    #         matches = []
    #         for item in output.get("matched_market_orders", []):
    #             match = OMEMatch(**item)
    #             matches.append(match)
    #
    #     result = OMEMatchOutput(matches)
    #
    #     # assert isinstance(result, OMEMatchOutput)
    #
    #     print(f"OMEConnector: {inspect.stack()[0][3]}: {result}")
    #     return result

    async def limit_order_place(self, input: PlaceLimitOrderInput) -> PlaceLimitOrderOutput:
        workflow_name = "ome_wf_limit_order_place"
        workflow_id = workflow_name + "".join(
            random.choices(string.ascii_uppercase + string.digits, k=6)
        )
        # Run workflow
        output = await self.client.execute_workflow(
            workflow_name,
            input,
            id=workflow_id,
            task_queue=TASK_QUEUE
        )

    async def limit_order_cancel(self, input: SimpleInput):
        workflow_name = "ome_wf_limit_order_cancel"
        workflow_id = workflow_name + "".join(
            random.choices(string.ascii_uppercase + string.digits, k=6)
        )
        output = await self.client.execute_workflow(
            workflow_name,
            input,
            id=workflow_id,
            task_queue=TASK_QUEUE
        )

    async def match_lock_acquire(self, input: AcquireMatchLockInput) -> AcquireMatchLockOutput:
        workflow_name = "ome_wf_match_lock_acquire"
        workflow_id = workflow_name + "".join(
            random.choices(string.ascii_uppercase + string.digits, k=6)
        )
        output = await self.client.execute_workflow(
            workflow_name,
            input,
            id=workflow_id,
            task_queue=TASK_QUEUE
        )
        result = output
        print(f"OMEConnector: {inspect.stack()[0][3]}: {result}")
        return result

    async def match_lock_cancel(self, input: SimpleInput):
        workflow_name = "ome_wf_match_lock_cancel"
        workflow_id = workflow_name + "".join(
            random.choices(string.ascii_uppercase + string.digits, k=6)
        )
        output = await self.client.execute_workflow(
            workflow_name,
            input,
            id=workflow_id,
            task_queue=TASK_QUEUE
        )

    async def match_lock_execute(self, input: SimpleInput):
        workflow_name = "ome_wf_match_lock_execute"
        workflow_id = workflow_name + "".join(
            random.choices(string.ascii_uppercase + string.digits, k=6)
        )
        output = await self.client.execute_workflow(
            workflow_name,
            input,
            id=workflow_id,
            task_queue=TASK_QUEUE
        )
        result = output
        print(f"OMEConnector: {inspect.stack()[0][3]}: {result}")
        return result
