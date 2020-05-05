import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import os
'''
Since, pexels is a client of clouflare, it is not possible for us to make requests using "requests" module from python.
We use selenium in this matter to overcome the difficulties of the situation.
We use firefox in this code.
'''

#Creating a class for our Pexels Scraper
class pexelScraper():


    def scroll(self,driver, timeout):
        scroll_pause_time = timeout
        # Get scroll height
        last_height =driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(scroll_pause_time)
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                # If heights are the same it will exit the function
                break
            last_height = new_height

    def queryRequest(self, QUERY):
        # Instantiating a firefox profile
        profile = webdriver.FirefoxProfile()
        # Setting this  preference makes sure that without images being loaded on the browser, less data is being used while scraping.
        # Unnecssary data consumption is reduced
        profile.set_preference("permissions.default.image", 2)
        # Instantiating the webdriver the profile we created earlier
        driver = webdriver.Firefox(firefox_profile=profile)
        #This will the main url
        URL = "http://www.pexels.com/search/"+QUERY
        #GET request is sent
        driver.get(URL)
        #Creating a list which will then have links.
        linkLIST = []
        #Infinite scrolling with timeout
        self.scroll(driver,2)
        #Getting all the <img> tags at once
        images_link = driver.find_elements_by_class_name("photo-item__img")
        # Traversing all <img> tags
        for image in images_link:
            #Going to the parent tag just to have the title for the particular image
            parent = image.find_element_by_xpath("..")
            #getting both image url and title and making a new string containing a proper url
            namedURL = "%s?cs=srgb&dl%s.jpg&fm=jpg"%(str(image.get_attribute("src")).split('?')[0], str(parent.get_attribute("title")).replace(".", ""))
            #Appending it to our list
            linkLIST.append(namedURL)
            #Printing each and every link just to make sure that you are supervising the process properly
            print(namedURL)
        #Calling a function which will save the links to a file
        self.saveQueryLink(QUERY, linkLIST)
        #printing the number of total collected images
        print("Total images collected: %d"%(len(images_link)))
        #closing the tab which we opened for our use
        driver.close()

    def saveQueryLink(self, QUERY, linkLIST):
        #Obtaining the current path form the os
        CUR_PATH = os.path.abspath(os.curdir)
        #Making a path for a new folder named "testFiles" in which all the results are saved
        PATH = CUR_PATH + os.path.sep + "textFiles"
        #Creating a folder using the previous path, only if it doesnt exist
        if not os.path.exists(PATH):
            os.makedirs(PATH)
        dirFILE = PATH+os.path.sep+QUERY+".txt"
        #Creating a new textfile which will contain the links of all images related to the QUERY
        linkFILE = open(dirFILE, "w+")
        #Exporting the list of links to the newly created textfile
        for link in linkLIST:
            linkFILE.write(link+"\n")
        print("All links got saved to a new textfile : %s"%(dirFILE))

