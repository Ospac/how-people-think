from wordcloud import WordCloud
from collections import Counter
import uuid
import matplotlib.pyplot as plt
def MakeWordCloud(wordList):
    counts = Counter(wordList)
    tags = counts.most_common(60)
    font_path = "static/assets/fonts/NotoSansKR-Medium.otf"
    wc = WordCloud(
        font_path = font_path,
        max_font_size=60, 
        background_color="white" 
    )
    cloud = wc.generate_from_frequencies(dict(tags))    
    img_path = 'static/assets/img/' + str(uuid.uuid4()) + '.png'
    cloud.to_file(img_path)
    return img_path
