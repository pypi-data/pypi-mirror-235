from typing import List
from enum import Enum
from dataclasses import dataclass
import random
import string
import inspect

from temporalio.client import Client

from guardian.workflows.place_market_order import MarketOrderInput 
from guardian.connectors.ome import OMEMatch

TASK_QUEUE = "clob-task-queue"

class CLOBConnector:
    """ Central Limit Order Book connector """

    def __init__(self, client: Client):
        self.client = client

    def check_liquidity(self, input: MarketOrderInput, currency_out_id: int) -> bool:
        return True


    async def lock_liquidity(self, matches: List[OMEMatch], currency_out_id: int) -> bool:

        class AccountAction(Enum):
            Balance = "Balance"
            AccountCredit = "AccountCredit"
            AccountDebit = "AccountDebit"
            LockAmount = "LockAmount"
            CancelLock = "CancelLock"
            ExecuteLock = "ExecuteLock"

        @dataclass
        class WorkflowInput:
            action: AccountAction
            account: str
            amount: str

        @dataclass
        class WorkflowOutput:
            action: AccountAction
            account: str
            amount: str

        # TODO: process the whole list of matches
        # This may require to refactor the API to get the whole list at onces
        match = matches[0]
        
        input = WorkflowInput(
            AccountAction.AccountDebit.value,
            f"{match.market_maker_user_id}-{currency_out_id}",
            str(match.target_currency_amount)
        )

        workflow_name = "LockLiquidityWorkflow"
        workflow_id = workflow_name + "".join(
            random.choices(string.ascii_uppercase + string.digits, k=6)
        )
        # Run workflow
        result = await self.client.execute_workflow(
            workflow_name,
            input,
            id=workflow_id,
            task_queue=TASK_QUEUE
        )
    
        #assert isinstance(result, WorkflowOutput)
    
        print(f"CLOBConnector: {inspect.stack()[0][3]}: {result}")
        return True
