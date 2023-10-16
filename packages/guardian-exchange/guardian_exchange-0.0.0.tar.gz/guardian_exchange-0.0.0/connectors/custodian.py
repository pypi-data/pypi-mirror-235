from temporalio.client import Client

from ..workflows.place_market_order import MarketOrderInput 

class CustodianConnector:
    """ Custodian connector """

    def __init__(self, client: Client):
        self.client = client

    def check_liquidity(input: MarketOrderInput) -> bool:
        return True


    def lock_liquidity(input: MarketOrderInput) -> bool:
        return True
