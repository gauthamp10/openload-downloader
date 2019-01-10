## Openload Downloader 

A python script which generates the download link for openload and it's other domains.

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

1.Chrome driver for selenium windows

Download:[chromedriver_win32.zip](https://chromedriver.storage.googleapis.com/2.45/chromedriver_win32.zip)

2.Extract the file content to C:/Windows


#### Linux

1. Chrome dirver for selenium linux
 
 Download: [chromedriver_linux64.zip](https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip)
 
 2.Extract the file any path and configure the same path in main.py as:
 
 
 3.driver = webdriver.Chrome(executable_path="/path/to/chromedriver")


#### Mac

1.Chrome dirver for selenium mac

Download: [chromedriver_mac64.zip](https://chromedriver.storage.googleapis.com/2.45/chromedriver_mac64.zip)

2.Extract the file to /usr/local/bin


### Usage

> python main.py


📝 *Please note pip installable python package will be avialable soon after further testing.*


###### Output

![Screenshot](https://raw.githubusercontent.com/gauthamp10/openload-downloader/master/screenie/out.png)


### Author

 **Gautham Prakash**
 
 My other projects:[github.com/gauthamp10](https://gauthamp10.github.io/)

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
