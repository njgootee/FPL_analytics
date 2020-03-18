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
url = 'https://understat.com/league/EPL'
driver = webdriver.Firefox()
driver.get(url)

#file to create csv files
tf = open('teaminfo.csv', 'w')
team_file = csv.writer(tf)


#Gather source code from webpage
page_soup = soup(driver.page_source,'html.parser')

button_path = "/html/body/div[1]/div[3]/div[3]/div/div[2]/div/div[1]/button"
try:
    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button_path)))
except TimeoutException:
    print("Loading took to long")

driver.find_elements(By.XPATH, button_path)[0].click()

label = ["11", "13", "14", "15", "16", "17","18"]
for i in label:
    page_soup = soup(driver.page_source,'html.parser')
    label_number = "/html/body/div[1]/div[3]/div[3]/div/div[2]/div/div[2]/div[2]/div/div["+ i + "]/div[2]/label"
    driver.find_elements(By.XPATH, label_number)[0].click()

driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div[3]/div/div[2]/div/div[2]/div[3]/a[2]")[0].click()
flag = True
if (flag == True):
    hnames = []
    page_soup = soup(driver.page_source,'html.parser')
    for header in page_soup.findAll('table')[0].tr.findAll('th'):
        hname = header.findAll('span')[0].contents[0]
        hnames.append(hname)
    team_file.writerow([hnames[1], hnames[2], hnames[3], hnames[4], hnames[5], hnames[6],
     hnames[7], hnames[8], hnames[9], "xG Change", hnames[10] , hnames[11], "xGA Change",hnames[12],
     hnames[13], hnames[14], hnames[15], hnames[16], hnames[17], hnames[18], "xPTS Change"])
    flag = False

for row in page_soup.findAll('table')[0].tbody.findAll('tr'):
    team = row.findAll('a')[0].contents[0]
    m = row.findAll('td')[2].contents[0]
    w = row.findAll('td')[3].contents[0]
    d = row.findAll('td')[4].contents[0]
    l = row.findAll('td')[5].contents[0]
    g = row.findAll('td')[6].contents[0]
    ga = row.findAll('td')[7].contents[0]
    pts = row.findAll('td')[8].contents[0]
    xg = row.findAll('td')[9].contents[0]
    xg_change = row.findAll('sup')[0].contents
    if xg_change:
        xg_change = xg_change[0]
    else:
        xg_change = 0

    npxg = row.findAll('td')[10].contents[0]
    xga = row.findAll('td')[11].contents[0]
    xga_change = row.findAll('sup')[1].contents
    if xga_change:
        xga_change = xga_change[0]
    else:
        xga_change = 0
    npxga = row.findAll('td')[12].contents[0]
    npxgd = row.findAll('span')[0].contents[0]

    ppda = row.findAll('td')[14].contents[0]
    oppda = row.findAll('td')[15].contents[0]
    dc = row.findAll('td')[16].contents[0]
    odc = row.findAll('td')[17].contents[0]
    xpts = row.findAll('td')[18].contents[0]
    xpts_change = row.findAll('sup')[2].contents
    if xpts_change:
        xpts_change = xpts_change[0]
    else:
        xpts_change = 0


    print(team, m, w, d, l, g, ga, pts, xg, xg_change, npxg, xga, xga_change, npxga,
     npxgd, ppda, oppda, dc, odc, xpts, xpts_change )

    team_file.writerow([team, m, w, d, l, g, ga, pts, xg, xg_change, npxg, xga,
     xga_change, npxga, npxgd, ppda, oppda, dc, odc, xpts, xpts_change])
tf.close()
