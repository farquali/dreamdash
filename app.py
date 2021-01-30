#!/Users/alice/opt/miniconda3/bin/python
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import requests
from datetime import datetime

import files as f

df = pd.DataFrame()

def main():

	read_dream_file()
	print(get_random_dream(df))



def get_random_dream(df):

	import random

	dream_count = df.shape[0]
	return df["Dream"][random.randint(0,dream_count)]

def read_dream_file():
	import googapi as go

	global df
	data = go.pull_sheet_data(f.SCOPES,f.MEGA_ID,f.MEGA_RANGE)
	df = pd.DataFrame(data[1:], columns=data[0])

	#replace null Dreamer col with 'Unknown'
	df["Dreamer"].fillna(value="Unknown",inplace=True)




main()





