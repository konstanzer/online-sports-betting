# Online Sports Betting: Beating the Bookie

## INTRODUCTION

I made my first sports bet in the eighth grade. I was sure the New York Yankees would crush the Arizona Diamondbacks in that year's World Series. It was not to be. I lost a five-dollar bet with a classmate and, being a sore loser, paid in pennies. Even so, no betting exchange would have given me those odds on the heavily favored Yankees. It was a good bet.

The fact is, every pro betting exchange offers odds at fair value minus a commission. They wouldn't stay in business otherwise. The bet functions like a roulette wheel: the probability of you winning a bet on black is not 18/36 (one-half) but 18/38 (less than one-half) because the house claims 0 and 00 for itself. Online sports bookies pay their data scientists well to make sure the exchange's odds are accurately estimating the probabilities of sporting event outcomes. For this reason, most value betting strategies are long-term losers.

**Betting algorithms** are statistical and machine learning models attempting to identify undervalued odds, usually by analyzing large amounts of data. Most fall into one of two classes: **value betting** or **arbitrage betting** bets. Value betting algorithms collect data from thousands of past sporting matches, estimate the probability of an outcome, and identify bookmakers offering odds below **expected value**, a key concept in any form of betting. Arbitrage betting algorithms, on the other hand, take advantage of patterns detected in odds. A risk-free betting opportunity occurs when a bettor take both sides of a bte and lock in a small profit.

There exists a third approach, not widely used, which does not require any historical knowledge either of the event itself or the odds. In **Beating the bookies with their own numbers - and how the online sports betting market is rigged (2017)**, the authors introduce a brilliant method of  online sports betting. Rather than compete with the bookmakers predictions, they beat the bookmakers by using their predictions against them. More specifically, they take advantage of mispriced odds using the implicit information in bookmakers' aggregate odds. It turns out that bookmakers sometimes intentionally offer discounted odds eithr to balance their books or make special offers.

Lisandro Kaunitz details his team's real-world results on his personal blog. Five months of ten-hour days monitoring a server and hastily placing the recommended bets turned $4,000 into $5,000. After server fees, this worked out to having a job that pays two-dollars an hour. Nevetheless, the team was having a blast and would have continued the experiment if not for the fact that bookmakers began limiting the size and type of bets they were allowed to place. Bookies are under no obligation to continue taking bets if they don't believe it's in there best interest. Kaunitz was barred from most bookmakers' platforms, leading to the paper's second conclusion: any bettor who finds a consistently profitable strategy will encounteer discriminatory practices at the hands of betting exchanges. 

Link to paper: https://www.researchgate.net/publication/320296375_Beating_the_bookies_with_their_own_numbers_-_and_how_the_online_sports_betting_market_is_rigged

Kaunitz's Blog: https://www.lisandrokaunitz.com/index.php/en/category/beatthebookies-en/

---

## SUMMARY 

I set out to create an online sports betting algorithm. I soon realized that strategies based on team, player, and other sporting event attributes are directly competing with bookmakers' models used to make odds, and that these models are very good. Perhaps unbeatable. Aggregating many bookmakers' odds, however, produces a consensus probability that indicates which bookmakers are offering mispriced odds. Furthermore, a strategy that exploits these opportunities repeatedly can significantly outperform random betting in the long-term. In this repo, I create such a model using 2005-2015 soccer match data while following closely the method described in the paper I have linked to above.

*Figure 1*.  A bettor making $50 bets using the recommended strategy would have made $97 thousand between 2005 and 2015. The random better (using prior probabilities of soccer match outcomes and placing an equal number bets) loses $129 thousand over the same period. (y-axis in US dollars, x-axis represents a ten year span of time)
<img src="img/two_bettors.png" width="900"/>

## DATA

Kaunitz, et al. collected historical closing odds (i.e. odds provided at game-time) for 479,440 soccer matches between 2005 and 2015 from 32 online bookmakers. The hard part of scraping the data off bookies' websites and cleaning it has been done for me.


| Feature       | Description    |
|---------------|----------------|
| 'league'      |  pro soccer league |
| 'match_date'  |  match date        |
| 'home_team'   |  home team         |
| 'home_score'  |  home team goals scored    |
| 'away_team'   |  away team                 |
| 'away_score'  |  away team goals scored    |
| 'avg_odds_home_win'   |  average odds for bet on home team win at game start|
| 'max_odds_home_win'   |  best odds for bet on home team win at game start   |
| 'top_bookie_home_win' | bookmaker offering max odds                 |
| 'n_odds_home_win'     | number of bookmakers providing odds for bet |

**Home win** data repeats for **away win** and **draw** (not shown), the other two possible outcomes of a soccer match.

A full list of the bookmakers:
---
Interwetten https://www.interwetten.com/en/sportsbook, bwin https://sports.bwin.com/en/sports, bet-at-home https://www.bet-at-home.com/en/sport, Unibet https://www.bet-at-home.com/en/sport, Stan James http://stanjames-betting.com/, Expekt https://www.expekt.com/en-fi, 10Bet https://www.10bet.com/sports/, William Hill https://www.williamhill.com/, bet365 https://www.nj.bet365.com/#/HO/, Pinnacle Sports https://www.pinnacle.com/en/, DOXXbet https://m.doxxbet.com.lr/ui/#/, Betsafe https://www.betsafe.com/en, Betway https://betway.com/en/sports, 888sport https://www.888sport.com, Ladbrokes https://sports.ladbrokes.com/, Betclic https://www.betclic.com/en/sports-betting/, Sportingbet https://sports.sportingbet.com/en/sports, myBet , Betsson, 188BET, Jetbull, Paddy Power, Tipico, Coral, SBOBET, BetVictor, 12BET, Titanbet, Youwin, ComeOn, Betadonis, Betfair

## REPRODUCE IT

1. Acquire the prepared data

The prepared dataset in the form of csv files is available for download at https://www.kaggle.com/austro/beat-the-bookie-worldwide-football-dataset. The notebook included in this repository uses only the file "closing_odds.csv". The csv file is a matrix of soccer games (rows) x features (teams, scores, league, etc).

2. Exploration of odds data.

Code or visualizing the odds is contained in the notebook. I used a linear regression (OLS) model and Pearson correlation to evaluate the consensus probabilities of bookmakers. I confirmed the hypothesis that aggregate odds are a strong predictor of the underlying probabilty of sporting event outcomes.

*Figure 2*.  The key point underlying the strategy. Bookie's provide odds of a soccer team winning, losing, or drawing the match at game time. The average of these odds is almost exactly the true, underlying probability of the event. Any bookie offering odds implicitly above this underlying probability, after accounting for a commission, is likely undervaluing their odds. (cutoff text of y-axis is the actual percentage of correct predictions at the given estimated probability)
<img src="img/cons_prob.png" width="540"/>

3. Build a model to identify mispriced odds.

The original model was built in MATLAB while my notebook is in Python. I encourage the interested reader to follow along with the paper mentioned in this readme's introduction. There you will find full mathematical explanations of the betting strategy. 

## RESULTS

The mispriced odds identification model *significantly outperforms* a random betting strategy using the prior probabilities of game outcomes, as confirmed in the notebook using a Welch's t-test comparing bet results.

<img src="img/results.png" width="900"/>

The next step is to create a model capable of evaluating bookmakers' continuous odds in order to make predictions in real-time.






