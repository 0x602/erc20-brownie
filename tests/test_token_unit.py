from brownie import BOOMToken
from scripts.helpful_scripts import *
import pytest

def test_deployed_and_minted():
    skip_if_not_local_env()
    INITIAL_SUPPLY = 777
    account = get_account()

    boom_token = BOOMToken.deploy(INITIAL_SUPPLY, {"from": account})

    assert INITIAL_SUPPLY == boom_token.balanceOf(account)

def skip_if_not_local_env():
    if not env_is_local():
        pytest.skip("Only for local testing")