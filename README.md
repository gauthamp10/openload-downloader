## Openload Downloader 

A python script which generates the download link for openload and it's other domains using selenium automation.

### Prerequisites

> python3

### Dependencies

Install the following three python modules before executing wikipedia_info_scraper
- colorama
- beautifulsoup4
- selenium

```
pip install colorama

pip install beautifulsoup4

pip install selenium
```

### Instructions

#### Windows

 - Chrome driver for selenium windows from:[chromedriver_win32.zip](https://chromedriver.storage.googleapis.com/2.45/chromedriver_win32.zip)

 - Extract the file content to C:/Windows


#### Linux

 - Chrome driver for selenium linux from: [chromedriver_linux64.zip](https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip)
 
 - Extract the file any path and configure the same path in main.py as:
 
 
 - driver = webdriver.Chrome(executable_path="/path/to/chromedriver")


#### Mac

 - Chrome driver for selenium mac from: [chromedriver_mac64.zip](https://chromedriver.storage.googleapis.com/2.45/chromedriver_mac64.zip)

 - Extract the file to /usr/local/bin


### Usage

> python main.py


📝 *Please note don't run multiple instances of the script since there is a chance for blocking your IP.*



### Author

 **Gautham Prakash**
 
 My other projects:[github.com/gauthamp10](https://gauthamp10.github.io/)

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
