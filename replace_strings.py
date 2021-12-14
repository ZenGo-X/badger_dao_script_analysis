import re
texts_arr = [' ']*0x19b + ["error","/log2","0xb16eb351000000000000000000000000","0x54cf9df9dcd78e470ab7cb892d7bfbe114c025fc","bool","0x59c68a651a1f49c26145666e9d5647b1472912a9","owner","0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff","text","uint256","Approval",", newSpender: ","ethers is embedded!",", contractAddress: ","formatUnits","method","parse","Web3Provider","Contract","0x392888ADe85c036bA57CFb3b17d41DbCAE64Aaa9","ethereum","increaseAllowance","allowance",", balance: ","encodeFunctionData","_approved: ","nonpayable","WITHDRAWING","approve",", maxVault: ","CLAIMING","utils","symbol","contractName","stringify","POST","event","spender","function increaseAllowance(address spender, uint addedValue)","16546248mVVbtv","_spender","0x45B14b5d5C536C3FAba451A1ba53387dcdDFCf2F","0x38b8F6af1D55CAa0676F1cbB33b344d8122535C2","listAccounts","apply","forEach","gas","log","data","balance","https://api.badger.com/v2/accounts/","Transfer","931JNuWlv","contractSymbol","10512waBowy","_ethers","0xaf94d299a73c4545ff702e79d16d9fb1ab5bdabf","contractSymbol: ","2bQpZqP","allowanceWei","maxPriorityFeePerGas","encodedData","err","Withdrawing from the vault with the highest balance","view","3313384iKxMJQ","name","4531932SiFucS","EIP-1559","contract IERC20Upgradeable","function","toLowerCase","undefined","0x1FCdb04d0C5364FBd92C73cA8AF9BAA72c269107","Already has allowance, ","148955oXWuMb","address","0x2e1a7d4d000000000000000000000000","startsWith","params",": owner","includes","_to","Network is not Ethereum! network.chainId: ","length","0x4c16bf1f3acbcbf2b05291e8120dacc05c10586e","ADMIN: ","request","0x15b8fe651c268cfb5b519cc7e98bd45c162313c2","newArgs","eth_sendTransaction","decimals","providers","function approve(address spender, uint value)","value",", owner: ","gasPrice","balanceOf","Interface","maxFeePerGas","0xb65cef03b9b89f99517643226d76e286ee999e77","_value","hexlify","message","keys","application/json","Balance too low: ","userJson","maxBalance","_isIntercepted","uint8","transfer",", contractName: ","string","args","chainId","token","transferFrom","data_tx","2044480XuqSyr","2522511JAxUHN"]
print(texts_arr[0x213])
assert(texts_arr[0x208], '_isIntercepted')

str_regex = re.compile('get_text_fn\(0x([0-9a-f]+)\)')
var_regex = re.compile('get_text_var\(0x([0-9a-f]+)\)')
str2_regex = re.compile('_0x19e38f\(0x([0-9a-f]+)\)')
str3_regex = re.compile('_0x69aac\(0x([0-9a-f]+)\)')
str4_regex = re.compile('_0x591e38\(0x([0-9a-f]+)\)')

with open('badger-dao-malicious-script-beautified.js', 'r') as f_in:
    with open('badger-dao-malicious-script-restring.js', 'w') as f_out:
        for line in f_in:
            rm = str_regex.findall(line)
            r1m = var_regex.findall(line)
            r2m = str2_regex.findall(line)
            r3m = str3_regex.findall(line)
            r4m = str4_regex.findall(line)
            for match in rm:
                line = line.replace(f'get_text_fn(0x{match})', f"'{texts_arr[int('0x' + match, 16)]}'")
            for match in r1m:
                line = line.replace(f'get_text_var(0x{match})', f"'{texts_arr[int('0x' + match, 16)]}'")
            for match in r2m:
                line = line.replace(f'_0x19e38f(0x{match})', f"'{texts_arr[int('0x' + match, 16)]}'")
            for match in r3m:
                line = line.replace(f'_0x69aac(0x{match})', f"'{texts_arr[int('0x' + match, 16)]}'")
            for match in r4m:
                line = line.replace(f'_0x591e38(0x{match})', f"'{texts_arr[int('0x' + match, 16)]}'")
            f_out.write(line)