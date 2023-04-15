"""
This script reads a batch of peptide sequences via stdin, e.g., a digestet protein,
composes a query and returns dlomix services.

Christian Panse <cp@fgcz.ethz.ch> 2023-04-15
"""

import sys
import json
import requests

def composeQuery(peptidesSequences):

    n = len(peptidesSequences)
    query = {
        "id": "CP 2023-04-15 n={}".format(n),
        "inputs": [
            {"name": "peptides_in_str:0", "shape": [n, 1], "datatype": "BYTES",
             "data": peptidesSequences},
            {"name": "collision_energy_in:0", "shape": [n, 1], "datatype": "FP32", "data": [25] * n},
            {"name": "precursor_charge_in_int:0", "shape": [n, 1], "datatype": "INT32", "data": [2] * n}
        ]
    }

    return query

def testQuery():
    url = "https://dlomix.fgcz.uzh.ch/v2/models/Prosit_2019_intensity_ensemble/infer"
    query = {
        "id": "LGGNEQVTR_GAGSSEPVTGLDAK",
        "inputs": [
            {"name": "peptides_in_str:0", "shape": [3, 1], "datatype": "BYTES",
             "data": ["LGGNEQVTR", "GAGSSEPVTGLDAK", "ELVISR"]},
            {"name": "collision_energy_in:0", "shape": [3, 1], "datatype": "FP32", "data": [25, 25, 25]},
            {"name": "precursor_charge_in_int:0", "shape": [3, 1], "datatype": "INT32", "data": [2, 2, 2]}
        ]
    }
    #jsonQueryStr = json.dumps(query, indent=2)
    print("query url: {}", url)
    x = requests.post(url, json=query)
    print("status: {}".format(x.status_code))
    print("response: {}".format(json.dumps(x.json(), indent=2)))

if __name__ == '__main__':
    #testQuery()
    #sys.exit(0)
    p = []
    for l in sys.stdin:
        p.append(l.strip())
    print (len(p))
    url = "https://dlomix.fgcz.uzh.ch/v2/models/Prosit_2019_intensity_ensemble/infer"
    x = requests.post(url, json = composeQuery(p))
    print("response: {}".format(json.dumps(x.json())))
    #print("response: {}".format(json.dumps(x.json(), indent=2)))


