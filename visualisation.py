import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def waffle_chart(categories, values, height, width):
    total_values = sum(values)
    category_proportions = [(float(value)/total_values) for value in values]
    total_num_tiles = width*height
    tiles_per_category = [round(proportion*total_num_tiles) for proportion in category_proportions]
    waffle_chart = np.zeros((height,width))
    category_index = 0
    tile_index = 0
    for col in range(width):
        for row in range(height):
            tile_index += 1
            if tile_index > sum(tiles_per_category[0:category_index]):
                category_index += 1
            waffle_chart[row,col] = category_index   
    fig = plt.figure()
    colormap = plt.cm.coolwarm
    plt.matshow(waffle_chart,cmap=colormap)
    plt.colorbar()
    ax = plt.gca()
    ax.set_xticks(np.arange(-.5,(width),1),minor=True)
    ax.set_yticks(np.arange(-.5,(height),1),minor=True)
    ax.grid(which='minor',color='w',linestyle='-',linewidth=2)
    plt.xticks([])
    plt.yticks([])
    values_cumsum = np.cumsum(values)
    total_values = values_cumsum[len(values_cumsum)-1]
    legend_handles = []
    for i,category in  enumerate(categories):
        label_str = category + ' (' + str(values[i]) + ')'
        color_val = colormap(float(values_cumsum[i]/total_values))
        legend_handles.append(mpatches.Patch(color=color_val,label=label_str))
    plt.legend(handles=legend_handles,
               loc='lower center',
               ncol=len(categories),
               bbox_to_anchor=(0,-0.2,0.95,0.1)
              )

def word_cloud(words,background,maxwords,img_mask):
    from wordcloud import WordCloud, STOPWORDS
    #texts = open(words,'r').read()
    texts = words
    stopwords = set(STOPWORDS)
    texts_wc = WordCloud(background_color=background,max_words=maxwords,stopwords=stopwords,mask=img_mask)
    texts_wc.generate(texts)
    plt.imshow(texts_wc,interpolation='bilinear')
    plt.axis('off')
    plt.show()