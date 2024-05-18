import shutil
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

BOT_NAME = "videokarty"

SPIDER_MODULES = ["videokarty.spiders"]
NEWSPIDER_MODULE = "videokarty.spiders"

ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = shutil.which('chromedriver')
SELENIUM_DRIVER_ARGUMENTS = ['--headless']  # Удалите '--headless', если хотите видеть браузер

def get_selenium_driver():
    options = Options()
    for argument in SELENIUM_DRIVER_ARGUMENTS:
        options.add_argument(argument)
    service = Service(executable_path=SELENIUM_DRIVER_EXECUTABLE_PATH)
    return webdriver.Chrome(service=service, options=options)

SELENIUM_DRIVER = get_selenium_driver()
