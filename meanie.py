#!/usr/bin/env pypy3

'''
  Market data mean calculator
  For each market keep track of:
  - Total volume
  - Mean price
  - Mean volume
  - Volume-Weighted mean price
  - Percentage buy orders
'''

from json import loads
from sys import stdin

market_ids = set()
markets = {}

'''
  We're going to track the following data items per market:
  - Total Volume
  - Total Price
  - Total (Volume * Price)
  - Total Orders
  - Total Buy Orders

  The results are calculated as follows:
  - Total Volume (Total Volume)
  - Mean Price (Total Price / Total Orders)
  - Mean Volume (Total Volume / Total Orders)
  - Volume-Weighted Mean Price (Total (Volume * Price) / Total Volume)
  - Percentage Buy Orders: (Total Buy Orders * 100.0 / Total Orders)
'''

def process_trade(InputString):
  # take JSON string and calculate over it
  trade = loads(InputString)
  market_id = trade['market']
  price = trade['price']
  volume = trade['volume']
  buy = 1 if trade['is_buy'] else 0

  if market_id not in market_ids:
    market_ids.add(market_id)
    markets[market_id] = {
      'volume': volume,
      'price': price,
      'vp': price * volume,
      'orders': 1,
      'buys': buy
    }
  else:
    markets[market_id]['volume'] += volume
    markets[market_id]['price'] += price
    markets[market_id]['vp'] += price * volume
    markets[market_id]['orders'] += 1
    markets[market_id]['buys'] += buy

  if trade['id'] % 1000000 == 0:
    print(f"Processed trade # {trade['id']}")


def main():
  for line in stdin:
    #print(line)
    if line[0] == '{':
      process_trade(line)

  # Report results
  for market in range(1, max(market_ids)+1):
    if market in market_ids:
      print(f'{{ "market":{market}, '
            f'"total_volume":{markets[market]["volume"]}, '
            f'"mean_price":{markets[market]["price"] / markets[market]["orders"]}, '
            f'"mean_volume":{markets[market]["volume"] / markets[market]["orders"]}, '
            f'"volume_weighted_average_price":{markets[market]["vp"] / markets[market]["volume"]}, '
            f'"percentage_buy":{markets[market]["buys"] * 100.0 / markets[market]["orders"]} }}')


if __name__ == '__main__':
  main()

