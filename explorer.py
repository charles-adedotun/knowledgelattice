# explorer.py
import streamlit as st


def view_document(supabase):
    # Get the document from the database
    response = supabase.table("documents").select("content").execute()
    st.write("**Explore your data**")
    # Display a list of elements from the documents
    # If the user clicks on an element, display the content of the document
    for index, document in enumerate(response.data):
        if st.button(document['content'][:50].replace("\n", " "), key=f"doc_button_{index}"):
            continue
