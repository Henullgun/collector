from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException, StaleElementReferenceException
# from selenium.webdriver.common.alert import Alert
from tqdm import tqdm
import os
import time
import base64
import urllib.request

class Crawler():

    downloadPath = "./python/download/"

    def __init__(self, url):
        self.url = url
        self.startCrawler()
    
    def creatDriver(self):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option.add_argument('log-level=3')
        driver = webdriver.Chrome('./python/chromedriver.exe', chrome_options = option)
        return driver
    
    def dirCheck(self):
        if not os.path.isdir(self.downloadPath):                                                           
            os.mkdir(self.downloadPath)

    def scrollDown(self, driver):
        driver.execute_script("window.scrollBy(0,10000)")
        time.sleep(1)
        driver.execute_script("window.scrollBy(0,10000)")
        # time.sleep(1)
        # driver.execute_script("window.scrollBy(0,10000)")
        # time.sleep(1)
        # driver.execute_script("window.scrollBy(0,10000)")
        # time.sleep(1)

    def getHTML(self, driver):
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def getImage(self, soup):
        img = soup.find_all("img")
        img_src = []
        for i in img:
            if(i.get("src") == None):
                img_src.append(i.get("data-src"))
            else:
                img_src.append(i.get("src"))
                
        # print(len(img_src))
        # for i in img_src:
        #     print(i)
        return img_src

    def imgDownload(self, imgs):
        count = 1
        for img in imgs:
            if(img.find("base64") != -1):
                continue
            else:
                # print(img)
                urllib.request.urlretrieve(img, self.downloadPath + str(count)+".jpg")
                count += 1
        print("Done")
            

    def startCrawler(self):
        driver = self.creatDriver()
        driver.get(self.url)
        self.scrollDown(driver)
        soup = self.getHTML(driver)
        imgs = self.getImage(soup)
        self.dirCheck()
        self.imgDownload(imgs)

if __name__=='__main__':
    print("URL입력")
    url = input()
    crawler = Crawler(url)
    input()