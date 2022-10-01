import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from datetime import datetime

service = Service(ChromeDriverManager().install())

##conexao com o Banco
from sqlalchemy import create_engine
import pymysql