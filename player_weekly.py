import requests
from bs4 import BeautifulSoup as soup
from selenium import webdriver
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import unicodedata


#url that we will be crawling on
driver = webdriver.Firefox()



links = ["team/Liverpool/2019", "team/Manchester_City/2019", "team/Leicester/2019", "team/Chelsea/2019",
"team/Manchester_United/2019", "team/Wolverhampton_Wanderers/2019", "team/Sheffield_United/2019",
"team/Burnley/2019", "team/Arsenal/2019", "team/Everton/2019", "team/Crystal_Palace/2019", "team/Southampton/2019",
"team/Newcastle_United/2019", "team/Brighton/2019", "team/West_Ham/2019", "team/Watford/2019", "team/Bournemouth/2019",
"team/Aston_Villa/2019", "team/Norwich/2019" ]

dates_start  = ["Aug 9, 2019", "Aug 17, 2019", "Aug 23, 2019", "Aug 31, 2019", "Sep 14, 2019", "Sep 20, 2019", "Sep 28, 2019",
"Oct 5, 2019", "Oct 19, 2019", "Oct 25, 2019", "Nov 2, 2019", "Nov 8, 2019", "Nov 23, 2019", "Nov 30, 2019",
 "Dec 3, 2019", "Dec 7, 2019", "Dec 14, 2019", "Dec 21, 2019", "Dec 26, 2019", "Dec 28, 2019", "Jan 1, 2020",
 "Jan 10, 2020", "Jan 18, 2020", "Jan 21, 2020", "Feb 1, 2020", "Feb 8, 2020", "Feb 22, 2020"]


dates_end  = ["Aug 11, 2019", "Aug 19, 2019", "Aug 25, 2019", "Sep 1, 2019", "Sep 16, 2019", "Sep 22, 2019", "Sep 30, 2019",
"Oct 6, 2019", "Oct 21, 2019", "Oct 27, 2019", "Nov 3, 2019", "Nov 10, 2019", "Nov 25, 2019", "Dec 1, 2019",
 "Dec 5, 2019", "Dec 9, 2019", "Dec 16, 2019", "Dec 22, 2019", "Dec 27, 2019", "Dec 29, 2019", "Jan 2, 2020",
 "Jan 12, 2020", "Jan 19, 2020", "Jan 29, 2020", "Feb 2, 2020", "Feb 19, 2020", "Feb 24, 2020"]



#### NEEDED 3, 5, 6, 8, 6, 10, 12, 13, 14, 15, 16, 17, 18
time_zone = True
i = 0
# for i in range(5,27):
file = "Player Info - Weekly/playerinfo_week"+ str(i + 1) + ".csv"
pf = open(file, 'w')
player_file = csv.writer(pf)


flag = True

x=1
for n in links:
    x += 1
    url = "https://understat.com/" + n
    driver.get(url)
    page_soup = soup(driver.page_source,'html.parser')
    if time_zone:
        driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/div/label[3]")[0].click()
        time_zone = False
    if flag:
        hnames = []
        page_soup = soup(driver.page_source,'html.parser')

        for header in page_soup.findAll('table')[1].tr.findAll('th'):
            hname = header.findAll('span')[0].contents[0]
            print(hname)
            hnames.append(hname)
        player_file.writerow(["Team", "First Name", "Last Name", hnames[2], hnames[3], hnames[4], hnames[5], hnames[6],
         hnames[7], hnames[8], hnames[9], hnames[10]])
        flag = False

    driver.execute_script("window.scrollTo(0, 400)")
    page_soup = soup(driver.page_source,'html.parser')
    # page_soup = soup(driver.page_source,'html.parser')

    begin_date = driver.find_elements(By.CLASS_NAME, "datepicker.hasDatepicker")[0]
    end_date = driver.find_elements(By.CLASS_NAME, "datepicker.hasDatepicker")[1]
    rand = driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/div[4]/div/div[1]/div[1]/div/div")
    end_date.send_keys(dates_end[i])
    if(i > 0):
        begin_date.send_keys(dates_start[i])

    driver.execute_script("window.scrollTo(0, 400)")
    page_soup = soup(driver.page_source,'html.parser')

    driver.implicitly_wait(500)# seconds
    rand[0].click()
    driver.find_elements(By.ID, "team-players-filter")[0].click()

    driver.implicitly_wait(900)# seconds

    page_soup = soup(driver.page_source,'html.parser')
    page_soup = soup(driver.page_source,'html.parser')
    page_soup = soup(driver.page_source,'html.parser')
    page_soup = soup(driver.page_source,'html.parser')
    page_soup = soup(driver.page_source,'html.parser')
    page_soup = soup(driver.page_source,'html.parser')
    page_soup = soup(driver.page_source,'html.parser')

    team = page_soup.findAll('ul', {"class":"breadcrumb"})[0].findAll('li')[2].contents[0]

    for row in page_soup.findAll('table')[1].tbody.findAll('tr'):
        # /html/body/div[1]/div[3]/ul/li[3]
        player = row.findAll('a')[0].contents[0]
        player = (unicodedata.normalize('NFKD', player).encode('ascii', 'ignore')).decode('utf-8')
        names = player.split(" ", 1)
        if(len(names) > 1):
            fname = names[0]
            lname = names[1]
        else:
            fname = names[0]
            lname = " "
        pos = row.findAll('td')[2].contents[0]
        apps = row.findAll('td')[3].contents[0]
        min = row.findAll('td')[4].contents[0]
        goals = row.findAll('td')[5].contents[0]
        a = row.findAll('td')[6].contents[0]
        sh90 = row.findAll('td')[7].contents[0]
        kp90 = row.findAll('td')[8].contents[0]
        xg = row.findAll('td')[9].contents[0]

        xa = row.findAll('td')[10].contents[0]

        print(team, fname, lname, pos, apps, min, goals, a, sh90,kp90, xg, xa)

        player_file.writerow([team, fname, lname, pos, apps, min, goals, a, sh90,kp90, xg, xa])
    print(x)
pf.close()



driver.close()
