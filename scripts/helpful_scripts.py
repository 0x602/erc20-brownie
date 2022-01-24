from brownie import network, accounts, config

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev", "mainnet-fork"]


def get_account(index=None):
    if index:
        return accounts[index]
    if env_is_forked_or_local():
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])

def env_is_local():
    return network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS

def env_is_forked():
    return network.show_active() in FORKED_LOCAL_ENVIRONMENTS

def env_is_forked_or_local():
    return env_is_local() or env_is_forked()