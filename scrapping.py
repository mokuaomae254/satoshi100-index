import pandas as pd
import numpy as np
import streamlit as st
import requests

#cert_path = 'path/to/your/certificate.pem'
r=requests.get("https://cryptoslate.com/coins/",verify=False)
#r=requests.get("https://cryptoslate.com/coins/",verify=cert_path)
dataframe=pd.read_html(r.text)[0]
dataframe=dataframe[["Name","Price","Market Cap","24H Vol","24H %","7D %","30D %","ATH","% ATH"]]


dataframe["Name"]=dataframe["Name"].apply(lambda x: x.split("  ")[0])#modify elements(entries) in x
dataframe["Price"]=dataframe["Price"].apply(lambda x:x.replace(",","").replace("$",""))
#df["Revenue"] = pd.to_numeric(df["Revenue"]).abs()

dataframe['Market Cap'] = dataframe['Market Cap'].str.replace(',', '').str.replace('$', '')
dataframe["Market Cap"] = pd.to_numeric(dataframe["Market Cap"]).abs()
dataframe["24H Vol"]=dataframe["24H Vol"].str.replace(',', '').str.replace('$', '')
dataframe["24H Vol"] = pd.to_numeric(dataframe["24H Vol"]).abs()
dataframe["ATH"]=dataframe["ATH"].str.replace(',', '').str.replace('$', '')




#TO add % comment 

dataframe["24H %"]=dataframe["24H %"].str.replace('%', '')
dataframe["24H %"] = pd.to_numeric(dataframe["24H %"])
dataframe["7D %"]=dataframe["7D %"].str.replace('%', '')
dataframe["7D %"] = pd.to_numeric(dataframe["7D %"])
dataframe["30D %"]=dataframe["30D %"].str.replace('%', '')
dataframe["30D %"] = pd.to_numeric(dataframe["30D %"])
dataframe["% ATH"]=dataframe["% ATH"].str.replace('%', '')
dataframe["% ATH"] = pd.to_numeric(dataframe["% ATH"])

data=dataframe.to_csv("satoshi 100 index data28.csv",index=True )#index true 0-99
st.dataframe(data)
#streamlit run scrapping.py
"""to this code add column investor confidence that is computed and filled by an if else statement that checks the 24 H% for btc and eth and if on the day they are down -5 % and another coin is up 0-5% on the same column it prints out low investor confidence .using an increment of 5 % for other coins and a decrement of -5 % for btc and eth print out "low investor confidence" "medium investor confidence" "high investor confidence" "very high investor confidence" "extremely high investor confidence""""