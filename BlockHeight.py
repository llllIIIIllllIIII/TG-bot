import requests
import json


def get_block_height():
    paylaod = {"query": "{wcBlocks: blocks(workchain: 0, page_size: 1) { seqno }}"}
    r = requests.post('https://dton.io/graphql/',data = paylaod )
    data = json.loads(r.text)
    blockheight = data['data']['wcBlocks'][0]['seqno']
    return blockheight



