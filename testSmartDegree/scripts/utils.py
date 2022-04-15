from brownie import network, accounts, config, web3

def get_account(configWalletName):
    # check if active network is development (ganache)
    if network.show_active() == "development":
        return accounts[0]
    # if it's an active testnet, we need an actual account
    else:
        return accounts.add(config['wallets'][f'{configWalletName}'])
