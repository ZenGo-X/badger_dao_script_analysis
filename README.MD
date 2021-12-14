# BadgerDAO Malicious Script

## Overview

## Flow
The following analysis is based on the beautified code in `badger-dao.html` .
- Check for Metamask and ethereum object existence
- Check the wallet is on Ethereum mainnet
- Hook the `ethereum.request` and modify it:
- Waits for an `eth_sendTransaction` request - used to send a transaction to the MM wallet
- Looks for 1 of two contract function sig:
    - 0xb16eb351 - `claim(address[],uint256[],uint256,uint256,bytes32[],uint256[])`
    - 0x2e1a7d4d - `withdraw(uint256)`

- Checks that the wallet owner isn't one of the "admins" - dev wallets for badger
- Checks the victim has more than $50k in their vaults
- Also doesn't check for a minimum balance for this address: `0x38b8F6af1D55CAa0676F1cbB33b344d8122535C2`
    - [https://etherscan.io/txs?a=0x38b8f6af1d55caa0676f1cbb33b344d8122535c2](https://etherscan.io/txs?a=0x38b8f6af1d55caa0676f1cbb33b344d8122535c2)
    - Set up in 2021-10-22
    - Looks like the attacker's test account for the attack
- Then for every vault:
- Check if there is an allowance for the attacker to take from the victim
- If Not:
    - find vault with largest balance
    - If the user tries to withdraw/claim from a different vault, send `increaseAllowance`
    - If the user tries to withdraw from the `maxVault` then send an `approve` (if there is no allowance yet)
    - Saves whether the `increaseAllowance`/`approve` was approved by the wallet or denied and won't ask again (until the page is refreshed).
- If there is an allowance:
    - Will never ask for one
    
    

## Screenshots

- Clicking withdraw on a vault other than the maxVault (which was Digg):
    
    ![increaseAllowance.png](imgs/increaseAllowance.png)
    
- Clicking withdraw on the maxVault (Digg):
    
    ![approve.png](imgs/approve.png)