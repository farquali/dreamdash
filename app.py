#!/Users/alice/opt/miniconda3/bin/python
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import requests
from datetime import datetime

import files as f


def main():

	import googapi as go

	data = go.pull_sheet_data(f.SCOPES,f.MEGA_ID,f.MEGA_RANGE)
	df = pd.DataFrame(data[1:], columns=data[0])

	#replace null Dreamer col with 'Unknown'
	df["Dreamer"].fillna(value="Unknown",inplace=True)
	print(df["Dreamer"][0])
	print(df.shape[0])


def get_random_dream(df):
	import random


print("Welcome to Dream Dash")

main()





