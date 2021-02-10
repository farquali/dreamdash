#!/Users/alice/opt/miniconda3/bin/python
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd
import requests
from datetime import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
import files as f
import wclouds as wc

#global vars
df = pd.DataFrame()
rand_dream_txt = ""
dreamers_list = []
dream_count_list = []

def main():

	read_dream_file()
	set_random_dream(df)
	#data_manipulation()
	#configure_dash_layout()
	wc.word_clouds(df)


def set_random_dream(df):

	import random
	dream_count = df.shape[0]
	random_idx = random.randint(0,dream_count)
	title = df["Title"][random_idx]
	dream_txt = df["Dream"][random_idx]

	if title == "":
		title = "Unknown"

	global rand_dream_txt
	rand_dream_txt = f"{title}: {dream_txt}"
	#print(rand_dream_txt)

#Read in Mega Dream googlesheet as a dataframe
def read_dream_file():
	import googapi as go

	global df
	data = go.pull_sheet_data(f.SCOPES,f.MEGA_ID,f.MEGA_RANGE)
	df = pd.DataFrame(data[1:], columns=data[0])

	#replace null Dreamer col with 'Unknown'
	df["Dreamer"].fillna(value="Unknown",inplace=True)

def configure_dash_layout():

	external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
	app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

	fig = px.pie(df,
				values=dream_count_list,
				names=dreamers_list,
				title="Dream Ratios",
				color_discrete_sequence=px.colors.qualitative.T10
				)

	fig.update_traces(texttemplate="%{percent:%f}") #show percent rounded.
	fig.update_traces(textposition = "inside") #set labels to be inside, so tiny % isn't outside
	fig.update_layout(uniformtext_minsize=10, uniformtext_mode='hide') #min size for text for tiny %s

	app.layout = html.Div(children=[
    html.H1(children=''),

    html.Div(children=rand_dream_txt),

    dcc.Graph(
        id='example-graph',
        figure=fig
    					)
	])

	if __name__ == '__main__':
		app.run_server(debug=True)



def data_manipulation():

	global dreamers_list, dream_count_list
	dreamers_list = df['Dreamer'].value_counts().index.tolist()
	dream_count_list = df['Dreamer'].value_counts().values.tolist()

	print(dreamers_list)
	print(dream_count_list)



main()





