import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly
import plotly.express as px
import plotly.graph_objects as go   
from plotly.subplots import make_subplots



data = pd.read_csv("covid_data.csv")

print(data.info())
print(data.describe())


data["Province_State"].fillna(value='',inplace=True)
print(data.info())




tendata=pd.DataFrame(data.groupby("Country_Region")["Confirmed"].sum().nlargest(10).sort_values(ascending=False))
print(tendata.info())

x=tendata.index
print(x)


#y=tendata["Confirmed"]
'''
plt.bar(x,y,color="b")
plt.xlabel("Countries")
plt.ylabel("Cases")
plt.show()
'''


#make plot nicer

figure1=px.scatter(tendata,x,y="Confirmed",size="Confirmed",size_max=120,color=tendata.index,title="Top 10 Countries by Confirmed Cases")
figure1.write_html('niceplot.html',auto_open=True)




#top 10 countries with most deaths

tenxdata=pd.DataFrame(data.groupby("Country_Region")["Deaths"].sum().nlargest(10).sort_values(ascending=False))

x=tenxdata.index

#figure2=px.scatter(tenxdata,x,y="Deaths",size="Deaths",size_max=100,color=tenxdata.index,title="Top 10 Countries by Most Deaths")


figure2=px.bar(tenxdata,x,y="Deaths",height=600,color="Deaths",orientation='v',color_continuous_scale=['deepskyblue','red'],title="Top 10 Countries by Most Deaths")

figure2.write_html('plotdeaths.html',auto_open=True)




#pick 1 counrty and analise according to states

dataus=data["Country_Region"]=="US"
databr=data["Country_Region"]=="Brazil"
dataru=data["Country_Region"]=="Russia"
datauk=data["Country_Region"]=="United Kingdom"

print(dataus)

#toptenus = pd.DataFrame(dataus.groupby("Province_State")["Confirmed"].sum().nlargest(10).sort_values(ascending=False))
#toptenstatesus= dataus["Province_State"].nlargest(10,"Confirmed")


usconf=data[dataus].nlargest(10,"Confirmed")

usdeath=data[dataus].nlargest(10,"Deaths")

brazil=data[databr].nlargest(10,"Confirmed")

print(data[dataru].nlargest(10,"Confirmed"))

print(data[datauk].nlargest(10,"Deaths"))




figure3= go.Figure(data=[go.Bar(name="US Confirmed",y=usconf['Confirmed'],x=usconf["Province_State"],orientation='v'),
                         go.Bar(name="US Deaths",y=usconf["Deaths"],x=usconf["Province_State"],orientation='v')
                         ])

figure3.update_layout(title="Most Affected States in US", height=800)

figure3.write_html('mostaffectedus.html',auto_open=True)



figure4= go.Figure(data=[go.Bar(name="BR Confirmed",y=brazil['Confirmed'],x=brazil["Province_State"],orientation='v'),
                         go.Bar(name="BR Recovered",y=brazil['Recovered'],x=brazil["Province_State"],orientation='v'),
                         go.Bar(name="BR Deaths",y=brazil["Deaths"],x=brazil["Province_State"],orientation='v')
                         ])

figure4.update_layout(title="Most Affected States in BR", height=800)

figure4.write_html('mostaffectedbr.html',auto_open=True)




#india

datain=data["Country_Region"]=="India"

india=data[datain].nlargest(10,"Confirmed")

figure5= go.Figure(data=[go.Bar(name="India Confirmed",y=india['Confirmed'],x=india["Province_State"],orientation='v'),
                         go.Bar(name="India Deaths",y=india["Deaths"],x=india["Province_State"],orientation='v')
                         ])

figure5.update_layout(title="Most Affected Cities in India", height=800)

figure5.write_html('mostaffectedindia.html',auto_open=True)











