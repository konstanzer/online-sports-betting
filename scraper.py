from selenium import webdriver
import pandas as pd
from datetime import datetime
import time


def scrape_odds(url, xpaths):
    """
    Args:
        URL where odds are (str)
        xpaths to teams and odds (list)
    Returns:
        Dictionary - keys: teams (list), values: odds (list)
    """
    with webdriver.Firefox() as driver:
        driver.get(url)
        
        #American odds & teams
        teams_elems = driver.find_elements_by_xpath(xpaths[0])
        mlines_elems = driver.find_elements_by_xpath(xpaths[1]) 
        
        mlines, teams = [], []
        for m, t in zip(mlines_elems, teams_elems):
            mlines.append(m.text)
            teams.append(t.text)
        
        driver.close()
        
    mline_df = pd.DataFrame.from_dict(dict(team=teams, moneyline=mlines))
    mline_df['date'] = datetime.today().strftime("%m-%d-%y")
    print(mline_df)
    
    return mline_df


def save_odds(url, xpaths, bookie, subdir="odds"):
    """
    Args:
        teams (list)
        moneylines (list)
        bookie (str)
        subdirectory (str)
    Returns:
        None
    """
    mline_df = scrape_odds(url, xpaths)
    
    try:
        old_df = pd.read_csv(f"{subdir}/{bookie}", index_col=0)
        pd.concat([old_df, mline_df]).to_csv(f"{subdir}/{bookie}")
    except:
        mline_df.to_csv(f"{subdir}/{bookie}")
    
    
if __name__ == "__main__":
    
    bookie = "DraftKings"
    url = "https://sportsbook.draftkings.com/leagues/football/88670561"
    xpaths = ["//div[@class='event-cell__name-text']",
              "//span[@class='sportsbook-odds american no-margin default-color']"]
    
    save_odds(url, xpaths, bookie)
    
    bookie = "BetMGM"
    url = "https://sports.va.betmgm.com/en/sports/football-11/betting/usa-9"
    xpaths = ["//div[@class='participant']",
              "//div[@class='option option-value']"]
    
    save_odds(url, xpaths, bookie)