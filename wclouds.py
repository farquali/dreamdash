#!/Users/alice/opt/miniconda3/bin/python
import files as f


indiv_theme_dict = {}
all_theme_dict = {}

def word_clouds(df):
	#individual_clouds(df)
	group_cloud(df)


def individual_clouds(df):
	print("calculating individual word clouds...")
	build_indiv_theme_dictionary(df)

	for dreamer, themes in indiv_theme_dict.items():
		build_word_frequency_list(themes)


def group_cloud(df):
	#for all dreamers, pick out the theme column
	all_themes = df['Themes'].tolist()

	global all_theme_dict

	tmp_list=[]
	for theme_str in all_themes:
		if theme_str != None:
				tmp_list += theme_str.split(",")

	all_theme_dict['All'] = [w.strip().lower() for w in tmp_list]

	for dreamer, themes in all_theme_dict.items():
		build_word_frequency_list(themes)




#create a word-frequency dictionary given a list of themes
def build_indiv_theme_dictionary(df):

	tmp_theme_dict = {}

	#for each of the dreamers, pick out all rows of their dreams
	for dreamer in f.ALL_DREAMERS:
		temp_df = df[df['Dreamer']==dreamer]
		tmp_theme_dict[dreamer] = temp_df['Themes'].tolist()
		#print(tmp_theme_dict[dreamer])

	#creates a dict with 4 dreamers as keys and values is a list of stripped themes
	for dreamer, themes in tmp_theme_dict.items():
		tmp_list = []
		for theme_str in themes:
			if theme_str != None:
				tmp_list += theme_str.split(",")

		tmp_list = [w.strip().lower() for w in tmp_list]

		global indiv_theme_dict
		indiv_theme_dict[dreamer]=tmp_list



def build_word_frequency_list(wordlist):
	import nltk
	from nltk import WordNetLemmatizer

	wnlemmatizer = WordNetLemmatizer()

	wordfreq_dict = {}

	lemlist = []
	#lemmatize words
	for theme in wordlist:
		if theme not in f.NO_LEMMATISE:
			lemlist.append(wnlemmatizer.lemmatize(theme))
		else:
			lemlist.append(theme)


	wordfreq = [lemlist.count(w) for w in lemlist]
	wordfreq_dict = dict(list(zip(lemlist,wordfreq)))
	print(wordfreq_dict)

	#remove any words that only appear once
	wordfreq_dict = remove_single_themes(wordfreq_dict)

	print(len(wordfreq_dict))

	print_cloud(wordfreq_dict)


#Given a word-frequency dictionary of themes, create an image of a wordcloud
def print_cloud(wordfreqdict):
	from wordcloud import WordCloud
	import matplotlib.pyplot as plt
	import matplotlib

	wordcloud = WordCloud(background_color="black", width = 800, height = 800,
                min_font_size = 10, margin = 10, colormap=matplotlib.cm.plasma).generate_from_frequencies(wordfreqdict)

	# plot the WordCloud image
	plt.figure(figsize = (8, 8), facecolor = None)
	plt.imshow(wordcloud, interpolation="bilinear")
	plt.axis("off")
	plt.tight_layout(pad = 0)

	plt.show()

def remove_single_themes(freqdict):

	delete = []
	for k,v in freqdict.items():
		if v == 1:
			delete.append(k)

	for k in delete:
		del freqdict[k]

	return freqdict

#set colours to be grey
def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    import random
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)





















