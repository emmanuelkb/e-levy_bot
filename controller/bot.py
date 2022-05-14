from datetime import datetime, timedelta
import re


def get_mentions(twitter_module):
    time = {'start_time': (datetime.utcnow() - timedelta(minutes=100)).strftime('%Y-%m-%dT%H:%M:%SZ')}
    response = twitter_module.get_mentions(time)
    print(response)
    if response['meta']['result_count'] == 0:
        return
    mentions = response['data']
    print(mentions)
    response = list(map(calculate_levy, mentions))
    print(response)
    # for res in response:
    #     body = {"text": res['response'], "reply": {"in_reply_to_tweet_id": res['id']}}
    #     print(twitter_module.reply_mention(body))


def calculate_levy(mention):
    # r"[-+]?(?:\d*\.\d+|\d+)"
    # (?:-)?(?:\d+ | \d{1, 3}(?:, \d{3}) *)(?:\.\d{1, 2})?$
    amount = re.findall(r"(-?\d+(?:[\.,]\d+)*)", mention['text'])
    if amount:
        if len(amount) > 1:
            return {'id': mention['id'], 'response': "Oh boss?"}
        amount = amount[0].replace(',', '')
        amount = float(amount)
    else:
        return {'id': mention['id'], 'response': 'Aloha'}
    if amount < 0:
        return {'id': mention['id'], 'response': "Oh boss?"}
    if amount <= 100:
        return {'id': mention['id'], 'response': 'No charge... for now.'}
    charge = (amount - 100) * 0.015
    return {'id': mention['id'], 'response': f'Stupid tax. You will be charged {charge:.2f} cedis'}
