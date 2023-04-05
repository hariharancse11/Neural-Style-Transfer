import streamlit as st
from transformers import pipeline
import tensorflow as tf

def predict_sa(txt):

    sentiment_pipeline = pipeline("sentiment-analysis", model='finiteautomata/bertweet-base-sentiment-analysis')
    data = txt
    return sentiment_pipeline(data)

def main():
    st.title("Sentiment Analysis using BERT")

    txt = st.text_input("Text","Type Here")
    result = ""
    if st.button('predict'):
        result=predict_sa(txt)
        if result[0]['label']=='POS':
            st.success('The sentiment of text is {}, Confidence is {}'.format('POSITIVE',result[0]['score']))
        if result[0]['label']=='NEG':
            st.success('The sentiment of text is {}, Confidence is {}'.format('NEGATIVE',result[0]['score']))
        if result[0]['label']=='NEU':
            st.success('The sentiment of text is {}, Confidence is {}'.format('NEUTRAL',result[0]['score']))



if __name__ == '__main__':
	main()
