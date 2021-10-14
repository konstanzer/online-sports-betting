# Does a profitable betting algorithm exist? ⚾

## Background (long)

I placed my first bet when I was 12 years-old. I wagered five dollars that the New York Yankees would defeat the Arizona Diamondbacks in the World Series. I lost the bet - the Yankees lost in a seven-game heartbreaker. I, being a sore loser, paid my debt in a lunch bag filled with 500 pennies.

Despite the outcome, it was a prudent bet. No betting exchange would not have given me even odds on the heavily favorited Yankees. The truth is, on every event on which a betting exchange offers odds, the odds are offered at below fair value. It functions like an American roulette wheel: the probability of black is not 18/36 but 18/38 because the house claims 0 and 00 for itself. A bettor has no real chance to match, much leff outperform, the betting exchange's forecast models, which are created by teams of well-funded data scientists. The reality it that any sports betting strategy a long-term loser. Well, almost any strategy.

Betting algorithms are programs designed to identify profitable betting opportunities by analyzing large amounts of data. Most fall into one of two categories: **value** bets or **arbitrage** bets.

* **Value betting algorithms** are the commonest type of betting algorithm. These algorithms collect data from thousands of past sporting matches, estimate the probability of bettable outcomes, and identify bookmakers offering odds on those outcomes that are below **expected value**.

* **Arbitrage betting algorithms** take advantage of patterns in odds. The opportunity occurs when a better can guarantee a small profit by taking both sides of a bet. These algorithms do not try to predict the occurence of sporting outcomes but instead, the odds themselves. Mistakes with this approach are very costly.

Once the bet is chosen, the algorithm may also choose an appropriate bet size, also called **bankroll management**.

The above two approaches have been studied extensively and offer little reason for optimism to the novice bettor, but there is a third approach.

Lisandro Kaunitz, Shenjun Zhong & Javier Kreiner, the authors of **Beating the bookies with their own numbers - and how the online sports betting market is rigged (2016)**, attempt a novel and brilliant approach to sports betting. Rather than compete with the bookmakers predictions or hope to identify arbitrage opportunities, Kunitz et al. try to beat the bookmakers by using their own predictions against them. In this paper, they demonstrate how to take advantage of mispriced odds using the implicit information in bookmakers' aggregate odds. It turns out that sometimes bookmakers intentionally offer discounted odds to balance their books or make special offers.

But before you rush off to implement this method yourself, consider the authors real-world results. Five months of ten-hour days monitoring a server on which the model was deployed, and hastily placing the recommended bets, turned $4,000 into $5,000. After server fees, this worked out to having a job that pays $2/hour. The authors would have continued the experiment except for the fact that bookmakers began limiting the size and type of bets they were allowed to place, leading to the second conclusion of the paper: even if a bettor has a consistently profitable strategy, the bookies are under no obligation to continue taking his or her bets. The authors conclude that betting exchanges use discriminatory practices against successful gamblers, and that online sports betting remains a long-term losing proposition.

## Overview

Rather than spend months implementing a doomed strategy, I simply want to explore the odds data used in the 2016 paper mentioned above.



