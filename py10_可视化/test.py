from pyecharts import WordCloud
import pandas as pd

post_data = pd.read_csv('C:\data\post_data.csv')

post_data2 = post_data.groupby(by=['category']).agg({'views': sum}).reset_index()
print(post_data2)

wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("",
              post_data2['category'],
              post_data2['views'],
              word_size_range=[20, 100]
              )
wordcloud.render("wordcloud.html")
