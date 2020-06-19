# CS 105 Final Project

Fantasy Premier League is a free to play fantasy football game based on the English Premier League. 
Users manage a team of Premier League players, whose performances in real-life fixtures determines the user’s points. 
Users have restrictions on budget, team formation, and transfers. Users compete in various leaderboards, the most 
prestigious being overall-rank; a leaderboard with all 6 million+ users competing for glory and prizes.

![Image of workflow](https://github.com/CS-UCR/cs105-prj-phase3-yeah-nah/blob/master/mindmap.png)

### Note
Project originally created for CS105 at UC Riverside, instructed by Professor Mariam Salloum. Project partner Ivannovi Jordan credited for web crawling implementation. Project will inform team management and player FPL points predictive algorithms for 2021 FPL season.

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
considering time and difficulty constraints. However, aspects of such an algorithm could be developed for this project.

### API
Data was obtained from the above FPL API link. Relevant datasets were created. The data was obtained with a simple python function using pandas, requests and json libraries. The data can be retrieved by running apiretrieve.py. To run this script one should change the save directories appropriately. 

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
### Cleaning Data
To reproduce results simply run through cleanapi.ipynb, cleanscraped.ipynb. unicodedata, pandas and numpy libraries are used. Again, change read and save directories in code blocks that are appropriate to your system/file management.

Api data is cleaned to remove unnecessary features and modify others for analysis. Fixture_gw files and player_gw files for all 27 game-weeks are concatenated into one file. Details of this process are commented in the notebook.

Scraped data has minimal cleaning process, primarily it creates a full name feature. This full name feature is used to map the fpl id to these csv files. Some names are different in api and scraped data, with no identifiable and/or consistent pattern of this difference. This lead to a failure to map ids. This was resolved with manual entry (in notebook) to create a resolute map.csv file. The data for 27 game-weeks is also combined into one large file.

### EDA
To reproduce results run EDA.ipynb with pandas, numpy, matplotlib and seaborn installed. Edit save and read directories as apporpriate.

The EDA process begins with merging csv files to create a dataframe containing target features (G,A,CS) and other key influential and identification features. This is followed by correlation matricies and a pairplot to view target features dependencies on other influential variables. Important trends in the pairplot are further explored and evaluated. Extensive commentary of the EDA details are found in the notebook. EDA dataframes are exported for phase 3 (machine learning processes).
![Pairplot](https://github.com/CS-UCR/cs105-prj-phase3-yeah-nah/blob/master/Phase%202/pairplot.png)

## Phase 3
Reproduce results by running ml.ipynb with pandas, sklearn and numpy installed.

EDA data is read in and classification piplines are created for logistic regression, SVM and decision tree models. The accuracy of these models are compared for each target feature, and a superior pipeline is chosen for each. 

An input is taken of an FPL player's team including player ids, position, team ids, opposition team id for the game-week and whether the player is home or away. Relevant data thats used in predictive models is merged to this dataframe from previous cleaned csv files. Predictions are made for G,A,and CS for each player in the team and ultimately calculates each players predicted FPL points for that game-week. There is also a codeblock that outputs suggested captain/vice-captain choices and predicted total points. Commentary of these processes are located within the notebook.

## Further development
We intend to further this project and improve accuracy of predictions through optimization of ml pipelines, feature creation etc. Eventually we desire to create a complete application that builds and manages its own FPL team that is competitive against real players.
