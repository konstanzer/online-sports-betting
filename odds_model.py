"""
Paper: https://www.researchgate.net/publication/320296375_Beating_the_bookies_with_their_own_numbers_-_and_how_the_online_sports_betting_market_is_rigged
The prepared dataset in the form of csv files is available for download at https://www.kaggle.com/austro/beat-the-bookie-worldwide-football-dataset
"""
import numpy as np
import pandas as pd

PATH = '~/data/'
close = pd.read_csv(PATH + 'closing_odds.csv', index_col=0)
"""
Kaunitz, Zhong, and Kreiner's strategy is explained in depth in their paper.
The optimal strategy maximizes expected payoff, which looks like this.

E(X) = (p-α)*Ω - 1

  where $X$ is a random variable representing the payoff of the bet,
  where $Ω$ are the odds paid by the bookmaker
  where $p$ is the underlying probability of the outcome
  and where $α$ is an adjustment term to account for the bookies' commission. 

You should bet when E(X) > 0.
Therefore, rearranging for odds, the betting condition is,

Ω > 1 / (p - α)

Notice that increasing α increases the expected value while decreasing the number of available bets 
"""

alpha = .05 #adjustment term
min_odds = 4 #minimum bookmakers offering odds
bet = 50 #bet size for every bet

#max odds represent the best available odds on that bet among all the bookmakers

def exp_payoff(res):
  return ((1 / close[f'avg_odds_{res}'] - alpha)\
          * close[f'max_odds_{res}'] - 1)\
          * (close[f'n_odds_{res}'] > min_odds)

exp_payouts = pd.DataFrame({'exp_payoff0': exp_payoff('home_win'),
                            'exp_payoff1': exp_payoff('away_win'),
                            'exp_payoff2': exp_payoff('draw')})

#highest payout per match
max_exp_payout = np.max(exp_payouts, axis=1)
#one-indexed column of highest payout
max_column = 1+np.argmax(np.array(exp_payouts), axis=1)

bets = []
for ix, i in enumerate(max_column):
  #place bet if max exp. value is positive
  if max_exp_payout.values[ix] > 0:
    bets.append(i)
  else:
    bets.append(0)

close['bet_result'] = bets

#create a list of relevant max odds based on game result
maximums = close.iloc[:,[9,11,10]] #order rearranged to match result column
max_odds = []

for i, j in zip(maximums.values, close.result):
  max_odds.append(i[j-1])

close['max_odds'] = max_odds

bet_df = close.iloc[:,18:21][close.bet_result > 0]
n_bets = len(bet_df)
bet_df['win'] = bet_df.bet_result == bet_df.result
bet_df['payoff'] = bet_df.win * bet_df.max_odds - 1
bet_df['gain'] = bet_df.payoff * bet
bet_df['cumulative'] = bet + bet_df.gain.cumsum()
             

mdl_accuracy = round(sum(bet_df.win)/n_bets,3)
mean_return_bet = mdl_profit/n_bets
mdl_profit = bet_df.cumulative.iloc[-1]

print(f'Matches bet on: {n_bets} ({round(n_bets/len(close)*100,1)} percent)')
print(f'Accuracy of bets: {mdl_accuracy}')
print(f'Profit of {mdl_profit} dollars generated on historical data.')

"""
* Implement a 'continuous odds' strategy using real-time data.
* Achieve success with paper (live simulated) trading and then finally real trading
* Create a live dashboard to alert bettor of picks.
"""

