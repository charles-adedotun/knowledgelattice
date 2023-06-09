## 1. **sidebar.py**

**Description:**

This file is responsible for generating the sidebar information in the application. It displays the total number of documents in the database. The sidebar information is important to give an overview of the data contained in the database.

**Functions:**

- `sidebar(supabase)`: This function generates the title of the sidebar and calls the function `number_of_documents` to calculate and display the total number of documents present in the database.

- `number_of_documents(supabase)`: This function queries the 'documents' table in the Supabase database and returns the count of the documents.

---

## 2. **question.py**

**Description:**

This file manages the question-asking functionality of the app. It uses OpenAI and Anthropics models to generate responses to user queries. This script also includes the functions to count the number of tokens in the question and manage the chat history.

**Objects and Functions:**

- `memory`: This is an instance of the `ConversationBufferMemory` class which stores the chat history.

- `openai_api_key`, `anthropic_api_key`: These are keys used for accessing the OpenAI and Anthropics APIs.

- `count_tokens(question, model)`: This function counts the number of words and tokens in the question.

- `chat_with_doc(model, vector_store: SupabaseVectorStore, stats_db)`: This function manages the chat interaction with the user. It includes buttons for asking a question, counting tokens, and clearing history. It also handles the interaction with the OpenAI and Anthropics models to generate responses.

---

## 3. **files.py**

**Description:**

This file manages the uploading and processing of files to the application. It supports various file types and handles each file differently based on its extension. 

**Functions:**

- `file_uploader(supabase, vector_store)`: This function handles the uploading of files. It supports single file upload and multiple files upload if self-hosted. It calls `filter_file` function for each uploaded file.

- `file_already_exists(supabase, file)`: This function checks if a file already exists in the database.

- `file_to_uploaded_file(file)`: This function converts a file to a streamlit `UploadedFile` object.

- `filter_zip_file(file, supabase, vector_store)`: This function unzips a zip file and filters each unzipped file.

- `filter_file(file, supabase, vector_store)`: This function filters a file based on its type and existence in the database. It calls the respective file processor function based on the file extension.

- `url_uploader(supabase, vector_store)`: This function allows uploading files from a URL.

---

## 4. **explorer.py**

**Description:**

This script manages the display of documents in the application. It retrieves all documents from the database and provides an interactive list to the user. When a user selects a document, it continues to the next document.

**Functions:**

- `view_document(supabase)`: This function retrieves all documents from the database and displays a button for each document. Clicking a button associated with a document will continue to the next document.

---

## 5. **components_keys.py**

**Description:**

This module contains a Python class `ComponentsKeys` that provides a centralized place for defining and maintaining component keys used in the Streamlit app. It currently contains one attribute `FILE_UPLOADER`.

**Classes:**

- `ComponentsKeys`: This class contains the keys for different components of the Streamlit app.

---

## 6. **brain.py**

**Description:**

This script provides data analysis and management features for

 the documents in the Supabase database. It fetches all documents, computes some statistics (total number and total size of documents), and displays these in the app. 

**Functions:**

- `brain(supabase)`: This function fetches all documents, computes some statistics, and displays these in the app. It also lists all documents along with a delete button for each one.

- `delete_document(supabase, document_name)`: This function deletes a document from the database.

---

## 7. **stats.py**

**Description:**

This file is responsible for tracking usage statistics of the application. It creates a table "stats" and includes functions for tracking usage and adding usage entries.

**Database Table:**

- `stats`: This table stores the timestamp of the action, details about the action, whether the action involved chat or embedding, and metadata. The primary key is an auto-generated integer ID.

**Functions:**

- `get_usage_today(supabase)`: This function returns the number of rows in the stats table for the last 24 hours. It is used for usage tracking.

- `add_usage(supabase, type, details, metadata)`: This function adds a new row to the stats table with the current timestamp and details about the action.

---

## 8. **utils.py**

**Description:**

This file includes utility functions for handling files, specifically calculating SHA1 hashes for file content.

**Functions:**

- `compute_sha1_from_file(file_path)`: This function reads a file and computes its SHA1 hash.

- `compute_sha1_from_content(content)`: This function computes the SHA1 hash of the given content.

---

## 9. **main.py**

**Description:**

This is the main entry point of the application. It initializes the necessary API keys, creates an instance of `Client` for interacting with Supabase, and calls the main functions to display the application's interface.

**Initialization:**

- Supabase client, OpenAI embeddings, and Supabase vector store are initialized.

- The models supported by the application are defined.

- The Streamlit page configuration is set, including the page title, layout, and initial sidebar state.

**Main Interface:**

- Displays the application title and a radio button for users to choose between adding knowledge, chatting with the AI, forgetting (deleting knowledge), or exploring the knowledge base.

- Depending on the user's choice, the appropriate function (`file_uploader`, `url_uploader`, `chat_with_doc`, `brain`, or `view_document`) is called.

- Usage statistics are tracked and displayed to the user.

---

## General Application Description

This application serves as a comprehensive knowledge management system, with document storage, interactive Q&A, and usage tracking functionalities. It allows users to upload documents, ask AI-based questions about document content, view and delete documents, and explore the entire knowledge base. Usage stats are tracked for better resource management. It uses the Streamlit library for an interactive interface and leverages Supabase for its database and storage needs. The application integrates with AI models from OpenAI and Anthropics to generate responses to user queries about the documents.

### Main Functionalities:

- Document upload: Supports both direct file upload and URL upload. Uploaded files are filtered based on type and existence in the database.

- Document management: Allows users to view and delete documents. Users can also explore the entire knowledge base.

- Question-asking: Leverages AI models to generate responses to user queries. Configuration options for model, temperature, chunk size, and overlap are provided.

- Usage tracking: Tracks and displays the number of tokens used daily.

### Things to Note for Maintainers:

1. API keys for OpenAI, Anthropics, and Supabase are critical. Ensure they are available and updated.

2. The document storage size in the Supabase database should be regularly checked to ensure it doesn't exceed the limit.

3. The file type filtering and processing rules may need to be updated based on the evolving needs of the application.

4. When adding new functionalities, ensure they are modular and fit well with the existing application structure. 

5. Usage stats tracking helps in managing resources and understanding user behavior.