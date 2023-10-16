from typing import List
from enum import Enum
from dataclasses import dataclass
import random
import string
import inspect

from temporalio.client import Client

from guardian.workflows.place_market_order import MarketOrderInput
from guardian.connectors.ome import OMEMatch

TASK_QUEUE = "balancedb-task-queue"
GENERAL_WORKFLOW = "balancedb_general_workflow"
SETTLE_WORKFLOW = "balancedb_settle_workflow"


class AccountAction(Enum):
    Balance = "Balance"
    AccountCredit = "AccountCredit"
    AccountDebit = "AccountDebit"
    LockAmount = "LockAmount"
    CancelLock = "CancelLock"
    ExecuteLock = "ExecuteLock"


@dataclass
class Settlements:
    source_account: str
    source_amount: str
    target_account: str
    target_amount: str


@dataclass
class SettleWorkflowInput:
    customer_account_in: str
    customer_account_out: str
    #     todo: SWAP TO ARRAY (ADD LIST BEFORE Settlements)
    settlements: List[Settlements]


class BalanceDBConnector:
    """ Balance DB connector """

    def __init__(self, client: Client):
        self.client = client

    async def check_liquidity(self, input: MarketOrderInput, check=None) -> bool:
        if check is not None:
            return False
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

        workflow_name = "balancedb_general_workflow"
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

        # assert isinstance(result, WorkflowOutput)

        print(f"BalanceDBConnector: {inspect.stack()[0][3]}: {result}")
        return result

    async def unlock_liquidity(self, matches: List[OMEMatch], currency_out_id: int) -> bool:
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

        match = matches[0]
        input = WorkflowInput(
            AccountAction.CancelLock.value,
            f"{match.market_maker_user_id}-{currency_out_id}",
            str(match.target_currency_amount)
        )

        workflow_name = GENERAL_WORKFLOW
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

        print(f"BalanceDBConnector: {inspect.stack()[0][3]}: {result}")
        return result

    async def execute_lock_liquidity(self, matches: List[OMEMatch], currency_out_id: int) -> bool:
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

        match = matches[0]
        input = WorkflowInput(
            AccountAction.ExecuteLock.value,
            f"{match.market_maker_user_id}-{currency_out_id}",
            str(match.target_currency_amount)
        )

        workflow_name = GENERAL_WORKFLOW
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

        print(f"BalanceDBConnector: {inspect.stack()[0][3]}: {result}")
        return result

    async def settle(self, input: SettleWorkflowInput) -> bool:
        @dataclass
        class WorkflowOutput:
            result: bool

        workflow_name = SETTLE_WORKFLOW
        workflow_id = workflow_name + "".join(
            random.choices(string.ascii_uppercase + string.digits, k=6)
        )

        result = await self.client.execute_workflow(
            workflow_name,
            input,
            id=workflow_id,
            task_queue=TASK_QUEUE
        )

        print(f"BalanceDBConnector: {inspect.stack()[0][3]}: {result}")
        return result

    async def test_workflow(self) -> bool:
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

        input = WorkflowInput(
            AccountAction.AccountCredit.value,
            f"1-USD",
            "1000"
        )

        workflow_name = GENERAL_WORKFLOW
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

        print(f"BalanceDBConnector: {inspect.stack()[0][3]}: {result}")
        return result

    async def test_workflow_credit(self) -> bool:
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

        input = WorkflowInput(
            AccountAction.AccountCredit.value,
            f"1-USD",
            "100000000"
        )

        workflow_name = GENERAL_WORKFLOW
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

        print(f"BalanceDBConnector: {inspect.stack()[0][3]}: {result}")
        return result

    async def lock_amount(self, account, amount):
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

        input = WorkflowInput(
            AccountAction.LockAmount.value,
            account,
            amount
        )
        workflow_name = GENERAL_WORKFLOW
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

        print(f"BalanceDBConnector: {inspect.stack()[0][3]}: {result}")
        return result
