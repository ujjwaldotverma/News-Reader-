from newsapi import NewsApiClient
import json
myapi=NewsApiClient(api_key='73edbc8e73a24f379fefabc7454ff3b2')

def speak2(str):
    from win32com.client import Dispatch
    say=Dispatch("SAPI.Spvoice")
    say.Speak(str)
country1 = input("enter the country:: ")
print(country1)
category1 = input("Category? sports, business, science, technolofy, health, entertainment::  ")
print(category1)
TOP_HEADLINES=myapi.get_top_headlines(country=country1,category=category1)
jsson=json.dumps(TOP_HEADLINES,indent=3)
print(jsson)
speak2(jsson)
speak2(TOP_HEADLINES)
print(TOP_HEADLINES.q)
