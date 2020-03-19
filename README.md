# CS 105 Final Project

Fantasy Premier League is a free to play fantasy football game based on the English Premier League. 
Users manage a team of Premier League players, whose performances in real-life fixtures determines the user’s points. 
Users have restrictions on budget, team formation, and transfers. Users compete in various leaderboards, the most 
prestigious being overall-rank; a leaderboard with all 6 million+ users competing for glory and prizes.

![Image of workflow](https://github.com/CS-UCR/cs105-prj-phase3-yeah-nah/mindmap.png)
## Phase 1
### Data Obtained
* API: https://fantasy.premierleague.com/api/bootstrap-static/ (API for FPL data)
* Web Crawling on: https://understat.com/league/EPL (Website for EPL data)

These two data sources are useful in conjunction. FPL source has useful data on FPL points, 
transfer history of player etc. EPL source has predictive data on expected goals, expected assists, etc. 
which are useful for predicting how a player will perform in FPL.

With this data, there are many analysis questions that could be answered. Predictive models for transferring, 
or which player to captain each week (2x score for that player) are possible products. These questions could 
also be answered with basic EDA. A machine-learning algorithm could also be created to completely manage a 
FPL team, this would incorporate all facets of team management, including transfers, captaining, chip usage etc. 
A complete machine learning algorithm for team management might be out of the scope of this project,
considering time and difficulty constraints. However, facets of such an algorithm could be developed.

### API
Data was obtained from the above FPL API link. Relevant datasets were created. The data was obtained with a simple python function using pandas, requests and json libraries. The data can be retrieved by running apiretrieve.py 

* `events`: dataset provides information on each FPL gameweek. This includes data on most captained, most transferred and highest scoring player, as well as other useful information.

* `elements`: dataset provides information on individual players. This includes data on total season FPL points, total minutes played, goals scored etc.

* `teams`: dataset provides information on EPL teams. Useful information in this dataset is rankings of attack/defence/overall strength while at home or away.

### Scraping/Crawling

The data obtained from crawling the English Premier League's official website (link provided above). The selenium web crawling software was used along with BeautifulSoup web scraping techinueqes to gather two datasets for this portion of the project. Some knowledge of HTML/CSS and XPath commands were needed for accessing the links and data that was provided in the webpaged scraped from.
The two data sets were: 
* `playersinfo.csv`: Provides infromation on all the players in the leaguge, allowing us to see the total goals scored by each player, how much time they spent on the field, and information like how many goals or assist they are predicted to make.

* `teaminfo.csv`: This provides detailed standings report compared to other teams, like overalls goals scored, win/loss/draw ratios, predicted goals scored per teams as well as assists.

#### Running the script

- Install Beautiful soup and Selenium Webdriver and unicodedata
- `pip install selenium` 
- `pip install bs4`
- `pip install unicodedata`
- get the link you want to scrape from input it in both `player_weekly.py` and `teams.py`
- run the `player_weekly.py` script to gather all the weekly information and stats on the players, and saves them into their respective 
game weeks in csv files.
- run the `team.py` script to gather the stats from each team.


## Phase 2
