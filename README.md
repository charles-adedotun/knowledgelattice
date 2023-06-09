# KnowledgeLattice

KnowledgeLattice is your second brain in the cloud, designed to easily store and retrieve unstructured information. It's like Obsidian but powered by generative AI.

## Features

- **Store Anything**: KnowledgeLattice can handle almost any type of data you throw at it. Text, images, code snippets, you name it.
- **Generative AI**: KnowledgeLattice uses advanced AI to help you generate and retrieve information.
- **Fast and Efficient**: Designed with speed and efficiency in mind. KnowledgeLattice makes sure you can access your data as quickly as possible.
- **Secure**: Your data is stored securely in the cloud and is always under your control.
- **Compatible Files**: 
  - **Text**
  - **Markdown**
  - **PDF**
  - **CSV**
  - **PowerPoint**
  - **Docx**
  - **HTML**
  - **Audio**
  - **Video**
- **Open Source**: KnowledgeLattice is open source and free to use.

## Demo

### Demo with GPT3.5

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed before continuing:

- Python 3.10 or higher
- Pip
- Virtualenv

You'll also need a [Supabase](https://supabase.com/) account for:

- A new Supabase project
- Supabase Project API key
- Supabase Project URL

### Installing

- Clone the repository

```bash
git clone  && cd chat-all-files
```

- Create a virtual environment

```bash
virtualenv venv
```

- Activate the virtual environment

```bash
source venv/bin/activate
```

- Install the dependencies

```bash
pip install -r requirements.txt
```

- Copy the streamlit secrets.toml example file

```bash
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

- Add your credentials to .streamlit/secrets.toml file

```toml
supabase_url = "SUPABASE_URL"
supabase_service_key = "SUPABASE_SERVICE_KEY"
openai_api_key = "OPENAI_API_KEY"
anthropic_api_key = "ANTHROPIC_API_KEY" # Optional
```

_Note that the `supabase_service_key` is found in your Supabase dashboard under Project Settings -> API. Use the `anon` `public` key found in the `Project API keys` section._

- Run the following migration scripts on the Supabase database via the web interface (SQL Editor -> `New query`)

```sql
-- Enable the pgvector extension to work with embedding vectors
create extension vector;

-- Create a table to store your documents
create table documents (
  id bigserial primary key,
  content text, -- corresponds to Document.pageContent
  metadata jsonb, -- corresponds to Document.metadata
  embedding vector(1536) -- 1536 works for OpenAI embeddings, change if needed
);

CREATE FUNCTION match_documents(query_embedding vector(1536), match_count int)
    RETURNS TABLE(
        id bigint,
        content text,
        metadata jsonb,
        -- we return matched vectors to enable maximal marginal relevance searches
        embedding vector(1536),
        similarity float)
    LANGUAGE plpgsql
    AS $$
# variable_conflict use_column
BEGIN
    RETURN query
    SELECT
        id,
        content,
        metadata,
        embedding,
        1 -(documents.embedding <=> query_embedding) AS similarity
    FROM
        documents
    ORDER BY
        documents.embedding <=> query_embedding
    LIMIT match_count;
END;
$$;
```

and 

```sql


create table
stats (
  -- A column called "time" with data type "timestamp"
  time timestamp,
  -- A column called "details" with data type "text"
  chat boolean,
  embedding boolean,
  details text,
  metadata jsonb,
  -- An "integer" primary key column called "id" that is generated always as identity
  id integer primary key generated always as identity
);
```

- Run the app

```bash
streamlit run main.py
```

## Built With

* [Streamlit](https://streamlit.io/) - The web framework used.
* [LangChain](https://python.langchain.com/en/latest/) - The LLM framework used.
* [Supabase](https://supabase.io/) - The open source Firebase alternative.

## Authors

* **Adedotun Charles** - *Initial work* - [AdedotunCharles](https://github.com/AdedotunCharles)

Inspired by the work of Quivr - [Quivr](https://github.com/StanGirard/quivr)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* A big thank you to the open-source community for making this project possible.
* Special thanks to [Quivr](https://github.com/StanGirard/quivr) for inspiring the creation of KnowledgeLattice.
