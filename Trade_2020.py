#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np


# In[112]:


import plotly.graph_objects as go
from colour import Color


# In[3]:


df=pd.read_excel(r"c:\Users\Sten\Documents\Trade\Data\Exports 2013 to 2020.xlsx")
df1=df.round(2)
df1


# In[4]:


p1=make_subplots(specs=[[{"secondary_y": True}]])
p1.add_trace(go.Scatter(x=df1["Date"], y=df1["Value"], 
                          mode="lines", line=dict(color="darkblue", width=3),
                          name="Exports £bn"), secondary_y=False)
p1.add_trace(go.Bar(x=df1["Date"], y=df1["Change on previous quarter"], 
                      name="% Change on previous quarter", marker=dict(color="dodgerblue",opacity=0.5)),
                     secondary_y=True)
p1.add_trace(go.Bar(x=df1["Date"], y=df1["Change on previous year"], 
                      name="% Change on previous year", marker=dict(color="lightsteelblue",opacity=0.5)),
                     secondary_y=True)
p1.update_layout({'plot_bgcolor':'white','paper_bgcolor':'white'},
                    title={'text': 'NI Quaterly Goods Exports 2013 to 2020'},
                    font=dict(family='Helvetica'))

p1.update_xaxes(title_text='Quarter')
p1.update_yaxes(title_text='% Change', secondary_y=True)
p1.update_yaxes(title_text='£bn', secondary_y=False)

p1



# In[5]:


df2=pd.read_excel(r"c:\Users\Sten\Documents\Trade\Data\Imports 2013 to 2020.xlsx")
rdf2=df2.round(2)


# In[6]:


p2=make_subplots(specs=[[{"secondary_y": True}]])
p2.add_trace(go.Scatter(x=rdf2["Date"], y=rdf2["Value"], 
                          mode="lines", line=dict(color="darkblue", width=3),
                          name="Imports £bn"), secondary_y=False)
p2.add_trace(go.Bar(x=rdf2["Date"], y=rdf2["Change on previous quarter"], 
                      name="% Change on previous quarter", marker=dict(color="dodgerblue",opacity=0.5)),
                     secondary_y=True)
p2.add_trace(go.Bar(x=rdf2["Date"], y=rdf2["Change on previous year"], 
                      name="% Change on previous year", marker=dict(color="lightsteelblue",opacity=0.5)),
                     secondary_y=True)
p2.update_layout({'plot_bgcolor':'white','paper_bgcolor':'white'},
                    title={'text': 'NI Quaterly Goods Imports 2013 to 2020'},
                    font=dict(family='Helvetica'))

p2.update_xaxes(title_text='Quarter')
p2.update_yaxes(title_text='% Change', secondary_y=True)
p2.update_yaxes(title_text='£bn', secondary_y=False)

p2


# In[7]:


df3=pd.read_excel(r"c:\Users\Sten\Documents\Trade\Data\Sector Exports 2013 to 2020.xlsx")
rdf3=df3.round(2)


# In[8]:


tidy_df3=pd.melt(rdf3,['Good'], var_name="Date", value_name="Export £m")


# In[9]:


p3=px.line(tidy_df3, x="Date", y="Export £m", color="Good",
                         color_discrete_sequence=px.colors.cyclical.Phase)
p3.layout=go.Layout(template='plotly_white', title='Value of NI quarterly exports of goods by sector 2013 to 2020')
p3.update_xaxes(title_text='Quarter', tickangle=90, showgrid=False)
p3.update_yaxes(title_text='£m', showgrid=False)
p3.for_each_trace(lambda t: t.update(name=t.name.replace('Good=','')))

p3.update_layout(font=dict(family='Helvetica'))


# In[10]:


df4=pd.read_excel(r"c:\Users\Sten\Documents\Trade\Data\Sector Imports 2013 to 2020.xlsx")
rdf4=df4.round(2)
tidy_df4=pd.melt(rdf4,['Good'], var_name="Date", value_name="Import £m")


# In[11]:


p4=px.line(tidy_df4, x="Date", y="Import £m", color="Good",
                         color_discrete_sequence=px.colors.cyclical.Phase)
p4.layout=go.Layout(template='plotly_white', title='Value of NI quarterly imports of goods by sector 2013 to 2020')
p4.update_xaxes(title_text='Quarter', tickangle=90, showgrid=False)
p4.update_yaxes(title_text='£m', showgrid=False)
p4.for_each_trace(lambda t: t.update(name=t.name.replace('Good=','')))

p4.update_layout(font=dict(family='Helvetica'))


# In[12]:


df5=pd.read_excel(r"c:\Users\Sten\Documents\Trade\Data\EU ROW Exports 2013 to 2020.xlsx")
rdf5=df5.round(2)
tidy_df5=pd.melt(rdf5,['EU / NON EU'], var_name="Date", value_name="Export £m")


# In[13]:


p5=px.line(tidy_df5, x="Date", y="Export £m", color="EU / NON EU",
                         color_discrete_sequence=px.colors.diverging.Portland)
p5.layout=go.Layout(template='plotly_white', title='Value of NI quarterly exports of goods by destination 2013 to 2020')
p5.update_xaxes(title_text='Quarter', tickangle=90, showgrid=False)
p5.update_yaxes(title_text='£m', showgrid=False)
p5.for_each_trace(lambda t: t.update(name=t.name.replace('EU / NON EU=','')))
p5.update_layout(font=dict(family='Helvetica'))


# In[14]:


df6=pd.read_excel(r"c:\Users\Sten\Documents\Trade\Data\EU ROW Imports 2013 to 2020.xlsx")
rdf6=df6.round(2)
tidy_df6=pd.melt(rdf6,['EU / NON EU'], var_name="Date", value_name="Import £m")
p6=px.line(tidy_df6, x="Date", y="Import £m", color="EU / NON EU",
                         color_discrete_sequence=px.colors.diverging.Portland)
p6.layout=go.Layout(template='plotly_white', title='Value of NI quarterly imports of goods by source 2013 to 2020')
p6.update_xaxes(title_text='Quarter', tickangle=90, showgrid=False)
p6.update_yaxes(title_text='£m', showgrid=False)
p6.for_each_trace(lambda t: t.update(name=t.name.replace('EU / NON EU=','')))
p6.update_layout(font=dict(family='Helvetica'))


# In[15]:


import panel as pn
pn.extension('plotly')


# In[16]:


pane1=pn.pane.Plotly(p1)
pane2=pn.pane.Plotly(p2)
pane3=pn.pane.Plotly(p3)
pane4=pn.pane.Plotly(p4)
pane5=pn.pane.Plotly(p5)
pane6=pn.pane.Plotly(p6)


# In[17]:


tab=pn.Tabs(
("Exports", pane1),
("Exports EU/NON EU", pane5),
("Exports by sector", pane3),
("Imports", pane2),
("Exports EU/NON EU", pane6),
("Imports by sector", pane4),
).servable()
tab
   



# In[159]:


Export_dict={
    'Value of NI quarterly exports of goods 2013 to 2020':p1,
    'Value of NI quarterly exports by EU and Non-EU':p5,
    'Value of NI quarterly exports by sector': p3}
Import_dict={
    'Value of NI quarterly imports of goods 2013 to 2020':p2,
    'Value of NI quarterly imports by EU and Non-EU':p6,
    'Value of NI quarterly imports by sector': p4
}  

