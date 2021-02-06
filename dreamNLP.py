#!/Users/alice/opt/miniconda3/bin/python
import files as f

def word_clouds(df):
	print("calculating word clouds...")
	build_theme_dictionaries(df)


def build_theme_dictionaries(df):

	theme_dict = {}

	#for each of the 4 dreamers, pick out all rows of their dreams
	for dreamer in f.ALL_DREAMERS:
		temp_df = df[df['Dreamer']==dreamer]
		theme_dict[dreamer] = temp_df['Themes'].tolist()

	#creates a dict with 4 dreamers as keys and values is a list of stripped themes
	for dreamer, themes in theme_dict.items():
		tmp_list = []
		for theme_str in themes:
			if theme_str != None:
				tmp_list += theme_str.split(",")
		tmp_list = [x.strip().replace("\\","").title() for x in tmp_list if not x==""] #strip away empty space at start or end

		print(f"Before lemma: {tmp_list}")
		#Get the root word for each theme/standardise
		theme_dict[dreamer] = lemmatize(tmp_list)

	for k,v in theme_dict.items():
		print(f"{k}: {v}")

def lemmatize(theme_list):
	#import textblob
	pass
	#return [Word(x).lemmatize() for x in theme_list]
















