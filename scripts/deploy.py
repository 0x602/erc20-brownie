from brownie import BOOMToken, config, network
from scripts.helpful_scripts import get_account

INITIAL_SUPPLY = 10000_000000000000000000

def deploy():
    account = get_account()
    boom_token = BOOMToken.deploy(
        INITIAL_SUPPLY,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False)
    )
    print(f"New token {boom_token.name()} ({boom_token.symbol()}) has been created!")

def main():
    deploy()
