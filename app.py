import streamlit as st
import pandas as pd
import json

# Load data
with open('data/books.json') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Streamlit UI
st.title("📚 Book Search - Books to Scrape")

search_term = st.text_input("🔎 Search Book Title")

if search_term:
    filtered_df = df[df['title'].str.contains(search_term, case=False, na=False)]
    st.write(f"Found {len(filtered_df)} results:")
    st.table(filtered_df[['title', 'price', 'availability', 'link']])
else:
    st.write("Enter a keyword to search for books.")

st.write("---")
st.write("Created for **UAS Information Retrieval** Universitas Abulyatama.")
