# pexels-qldl
A Query Link Downloader for [www.pexels.com]<br>
Written in: Python<br>
*Only for educational purpose*

## Instruction Video on Youtube.
###### Shall be released soon.

## What is qldl?
qldl is a acronym for Query Link Downloader.<br>
Here, you get links of images. Later these links are used to download using third party apps.
## Why we use IDM?
Here we use Internet Download Manager to download with blazing speed. Since it is meant to download, it has tonnes of features to use.
## What is it?
It is a python based downloader used to download high quality images from [www.unsplash.com] official site.
## Why is it in python?
Since python is one of the programming languages which is very popular and very powerful. We use python for our tool's development.
## Why we use ["Selenium"](https://pypi.org/project/selenium/) but neither ["BeautifulSoup"](https://pypi.org/project/beautifulsoup4/) nor ["Requests"](https://pypi.org/project/requests/)?
Since https://www.pexels.com is a client of https://www.cloudflare.com, It is better to use a webdriver instead of requests. You will get captchas if you go through requests. 
We could have used [bs4](https://pypi.org/project/beautifulsoup4/ "Beautiful Soup"), but we chose Selenium. 

----

## Prerequisite (for Windows)
* Firstly you need python in your computer.<br>
* Download these modules: [requests](https://pypi.org/project/requests/), [Beautifulsoup](https://pypi.org/project/bs4/), [urllibs](https://pypi.org/project/urllib3/), [click](https://pypi.org/project/click/), [selenium](https://pypi.org/project/selenium/)<br>
* Run the given commands on windows command-line. This instruction is particularly for Windows user. If you use any other machine, please see the documentations of the following modules.
```Python
pip install requests
pip install beautifulsoup4
pip install urllib3
pip install click
pip install selenium
```
* We recommend to use firefox browser, so please download [firefox](https://www.mozilla.org/en-US/firefox/new/ "Firefox Official") for your machine.
* Download geckodriver.exe [here](https://github.com/mozilla/geckodriver/releases "Mozilla Github").
* Add the path of geckodriver.exe file to the environment variable in Windows OS. 
----

## Download a database related to a query
1. Download the files as it is.
2. Open command prompt from the directory in which your downloaded files are present.
3. Use your url to download as given : 
<br>`python pexels-qldl.py --query [search for something]`<br>For example: <br>
`python pexels-qldl.py --query nature`<br>
4. OR you can simply do this:<br>`python pexels-qldl.py`<br>

![screenshot_1](https://github.com/arg-z/pexels-qldl/blob/master/images/1.PNG?raw=true)<br>

![screenshot_2](https://github.com/arg-z/pexels-qldl/blob/master/images/2.PNG?raw=true)<br>

4. You will get a text file containing urls of the query. Copy the urls to your clipboard.<br>
5. Open IDM on your computer, go to Tasks >> Add batch download from clipboard >> Select all >> Download<br>

#### Thank You
