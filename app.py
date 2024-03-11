import streamlit as st
import matplotlib.pyplot as plt
import json
import glob


file_path = glob.glob("jsonData/*.json")

def paper_data(f):
    data_json = f

    classes = list(data_json["class_mAP(50-95)"].keys())
    mAP_value = list(data_json["class_mAP(50-95)"].values())

    plt.bar(classes, mAP_value)
    plt.xlabel('Class')
    plt.ylabel('mAP(50-95)')
    plt.title(data_json["object_name"])
    plt.ylim(0.001, 1)
    st.pyplot()

def date_select(date):
    for file in file_path:
        if date in file:
            with open(file, 'r') as f:
                data = json.load(f)
                paper_data(data)


def main():
    dates = ['paper_20240202', 'paper_20240205', 'paper_20240206']
    selected_data = st.selectbox('날짜 선택', dates)
    date_select(selected_data)

if __name__ == "__main__":
    main()



# streamlit run app.py