import streamlit as st
import requests
import pandas as pd
import datetime

st.title('conpass IT勉強会カレンダー')

now = datetime.date.today().strftime('%Y%m%d')
url = 'https://connpass.com/api/v1/event/?order=2&count=100&ymd=' + now
r = requests.get(url)

events = r.json()['events']


df = pd.DataFrame()
for i, event in enumerate(events):
    event.pop('series', None)
    started_at = datetime.datetime.fromisoformat(event['started_at'])
    event['started_at'] = started_at.strftime('%Y/%m/%d %H:%M')
    _df = pd.DataFrame(event, index=[i, ])
    df = df.append(_df)
#    print(i, channel)

st.table(df[["title","started_at","place","limit","accepted","event_url"]].iloc[::-1])
