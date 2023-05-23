import json
import requests
import logging


logging.basicConfig(format='%(asctime)s : %(message)s', datefmt='%d-%m-%Y %H:%M:%S', level=logging.INFO)

url_sentiment_api = "http://34.152.38.219:9090/sentiment-analyzer"
headers_sentiment_api = {"Content-Type": "application/json; utf-8",
                         "X-API-Token":
                             "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiQVBJIiwiaWF0IjoxNjUxODExOTE4LCJzZXJ2aWNlIjoic2VudGltZW50In0.E0p6r3YeMtPBgZ65K0xWsNgRXfTW-JtLd7GpqN_zl60"
                         }

def call_sentiment(id, text):
    try:
        doc = dict()
        doc["id"] = id
        doc["text"] = text
        data_request = []
        data_request.append(doc)
        response_data = None
        try:
            response_data = requests.post(url_sentiment_api, headers=headers_sentiment_api,
                                          json=data_request).json()
        except:
            logging.error("call api error: {}".format(json.dumps(data_request)))
        if response_data is not None:
            logging.info("response: {}".format(response_data[0]))
            return response_data[0]
        return None
    except Exception as e:
            print(str(e))

#output = call_sentiment('1','chuyeern tien maix khong duocj')
#print(output['aspects'])

import streamlit as st
st.set_page_config(
     page_title="Comment sentiment analysis online",
     page_icon="❄️",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )

html_temp = """
                <div style="background-color:{};padding:1px">

                </div>
                """


with st.sidebar:
    st.markdown("""
        Made by [@Viet Duc]() and [@Kim Toan]()
        """,
                unsafe_allow_html=True,
                )
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    # About 
    Tool that allows you to analyze the sentiment of any text-based 
    comments you may have. By leveraging state-of-the-art 
    natural language processing techniques, we are able to accurately determine the sentiment 
    of any given comment, whether it be positive, negative, or neutral. 
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    # How does it work
    Using our Comment Sentiment Analysis tool is easy! 
    Simply type in the comment that you want to analyze in the text 
    input field provided on our website. Once you've entered your comment, 
    click on the "Enter" button to start the analysis.
    """)


st.write('# Comment sentiment analysis online')
st.write(
    ":dog: Leave a comment and let us predict your feelings. This code is available [here](https://github.com/nvd4c/demo_thesis.git) on GitHub."
)


def main():
    user_question = st.text_input("Input text: ", disabled=False, placeholder="What's on your mind?")
    if user_question:
        with st.spinner('Processing...'):
            my_bar = st.progress(0)
            my_bar.progress(10)
            my_bar.progress(20)
            my_bar.progress(30)
            my_bar.progress(40)
            my_bar.progress(50)
            my_bar.progress(60)
            response_text = call_sentiment('1', user_question)
            my_bar.progress(70)
            my_bar.progress(80)
            my_bar.progress(90)
            my_bar.progress(100)
            noidungchinh = response_text['aspects'].keys()
            noidungchinh = str(noidungchinh).split("[")[1].split("]")[0]
            noidungchinh = noidungchinh.replace("_", " ").replace("'","")
            sacthai = response_text['overall']
            # dochinhxac = response_text['overall_score']
            st.write('Nội dung chính:', noidungchinh)
            if sacthai == 'Positive':
                st.write('Sắc thái: Tích cực')
            if sacthai == 'Negative':
                st.write('Sắc thái: Tiêu cực')
            if sacthai == 'Neutral':
                st.write('Sắc thái: Trung tính')
            # st.write('Độ chính xác:', dochinhxac)
main()
