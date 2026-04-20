import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load cleaned dataset
df = pd.read_csv("data/cleaned_poll_data.csv")

st.title("📊 Poll Results Visualizer")

# Sidebar filters
st.sidebar.header("Filter Responses")
selected_tool = st.sidebar.multiselect(
    "Select Preferred Tool(s):",
    df['Preferred Tool'].unique(),
    default=df['Preferred Tool'].unique()
)

filtered_df = df[df['Preferred Tool'].isin(selected_tool)]

# Show dataset preview
if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)

# Bar chart - Tool Preference
st.subheader("Tool Preference")
tool_counts = filtered_df['Preferred Tool'].value_counts()
st.bar_chart(tool_counts)

# Histogram - Satisfaction Ratings
st.subheader("Satisfaction Ratings")
fig, ax = plt.subplots()
sns.histplot(filtered_df['Satisfaction (1-5)'], bins=5, kde=True, ax=ax)
st.pyplot(fig)

# Line chart - Responses Over Time
st.subheader("Responses Over Time")
df['Date'] = pd.to_datetime(df['Timestamp']).dt.date
daily = df.groupby('Date').size()
st.line_chart(daily)

# Word Cloud - Feedback
# Word Cloud - Feedback
st.subheader("Feedback Word Cloud")
text = " ".join(filtered_df['Feedback'].dropna().astype(str))
if text:
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    fig_wc, ax_wc = plt.subplots()
    ax_wc.imshow(wordcloud, interpolation="bilinear")
    ax_wc.axis("off")
    st.pyplot(fig_wc)
else:
    st.write("No feedback available to generate word cloud.")
