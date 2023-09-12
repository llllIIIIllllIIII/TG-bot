import requests
paylaod = {"query": "{wcBlocks: blocks(workchain: 0, page_size: 1) { seqno }}"}
r = requests.post('https://dton.io/graphql/',data = paylaod )
r.text
