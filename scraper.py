from selenium import webdriver
import pandas as pd
import time


def scrape_odds(url, xpaths):
    """
    Args:
        URL where odds are (str)
        xpaths to teams and odds (list)
    Returns:
        Teams (list), odds (list)
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
        
    return teams, mlines


def get_strtime():
    """Return a string of GMT time"""
    gmt = time.gmtime()[:6]
    strtime = f"{gmt[0]}{gmt[1]}{gmt[2]}_{gmt[3]}:{gmt[4]}:{gmt[5]}"
    return strtime


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
    teams, mlines = scrape_odds(url, xpaths)
    odds_df = pd.DataFrame.from_dict(dict(team=teams, moneyline=mlines))
    print(odds_df)
    odds_df.to_csv(f"{subdir}/{bookie}_" + get_strtime())
    
    
if __name__ == "__main__":
    
    #DraftKings
    url = "https://sportsbook.draftkings.com/leagues/football/88670561?category=game-lines&subcategory=game"
    xpaths = ["//div[@class='event-cell__name-text']",
              "//span[@class='sportsbook-odds american no-margin default-color']"]
    
    save_odds(url, xpaths, "draftkimgs")