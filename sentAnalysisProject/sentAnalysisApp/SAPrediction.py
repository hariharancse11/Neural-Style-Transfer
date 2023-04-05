from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis",model='finiteautomata/bertweet-base-sentiment-analysis')

def SAPredict(txt):
    data = txt
    result = sentiment_pipeline(data)
    score = str(result[0]['score'])[:4]
    if result[0]['label']=='POS':
        return('Sentiment: {}, Score: {}'.format('POSITIVE',score))
    if result[0]['label']=='NEG':
        return('Sentiment: {}, Score: {}'.format('NEGATIVE',score))
    if result[0]['label']=='NEU':
        return('Sentiment: {}, Score: {}'.format('NEUTRAL',score))