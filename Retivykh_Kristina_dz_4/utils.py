import requests
import json
from decimal import Decimal
import datetime as dt
from bs4 import BeautifulSoup

URL = "https://www.cbr-xml-daily.ru/daily_json.js"
URL_XML = "http://www.cbr.ru/scripts/XML_daily.asp"
URL_XML_UTF8 = "https://www.cbr-xml-daily.ru/daily_utf8.xml"


def currency_rates(code):
    """Возвращает курс валюты по отношению к рублю."""
    responce = requests.get(URL)
    data = json.loads(responce.text)
    return data.get("Valute", {}).get(code.upper(), {}).get("Value")


def currency_rates_decimal(code):
    """Возвращает курс валюты по отношению к рублю."""
    responce = requests.get(URL)
    data = json.loads(responce.text)
    return Decimal(str(data.get("Valute", {})
                           .get(code.upper(), {})
                           .get("Value")))


def currency_rates_adv(code):
    """Возвращает словарь, состоящий из курса валюты по отношению к рублю
    и даты, которая возвращается в ответе сервера"""
    responce = requests.get(URL)
    data = json.loads(responce.text)
    return {"value": data.get("Valute", {}).get(code.upper(), {}).get("Value"),
            "date": dt.datetime.fromisoformat(data.get("Date"))}


def currency_rates_str_only(code):
    """Возвращает курс валюты по отношению к рублю.
    Решение задачи методами строк"""
    code = code.upper()
    resp = requests.get(URL_XML)
    if code in resp.text:
        code_index = resp.text.find(code)
        start_str = resp.text[:code_index].split("<Valute ")[-1]
        end_str = resp.text[code_index:].split("</Valute>")[0]
        data_str = start_str + end_str
        start_index = data_str.find("<Value>") + len("<Value>")
        end_index = data_str.find("</Value>")
        return float(data_str[start_index:end_index].replace(',', "."))
    return None


def currency_rates_xml(code):
    """Возвращает курс валюты по отношению к рублю.
    Решение задачи через работу с xml"""
    code = code.upper()
    resp = requests.get(URL_XML_UTF8)
    soup = BeautifulSoup(resp.text, "xml")
    for valute in soup.ValCurs:
        if valute.CharCode.text == code:
            return float(valute.Value.text.replace(',', "."))
    return None
