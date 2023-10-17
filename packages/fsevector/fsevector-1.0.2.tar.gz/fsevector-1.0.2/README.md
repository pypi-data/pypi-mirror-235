# A fse vectorstore for langchain
fsevector is a vectorstore python library for langchain based on fse and postgres. it provides vector storage function, vector retrieval.

## Installation
Deploy postgres and fse
```
Before using fsevector, you need to deploy postgres and fse services (it is recommended to install the DeepEngine of deepglint).
```

Install fsevector
```console
pip install fsevector
```

## Documentation

More information can be found on the [examples](https://gitlab.deepglint.com/chenbo/fsevector/-/blob/main/examples/fsevector_fromtexts_test.py)
[Example](https://gitlab.deepglint.com/chenbo/fsevector/-/blob/main/examples/fsevector_streamlit_test.py) based on streamlit

## Usage
Instructions for use
```
When using fsevector, you need the following steps:
1. Enter pg_connection_string and fse_connection_string in the following call example.
2. Add OpenAI-related environment variables.
```

Example
```python
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_base = os.environ["OPENAI_API_BASE"]
openai.api_version = os.environ["OPENAI_API_VERSION"]
openai.api_type = os.environ["OPENAI_API_TYPE"]

#init fseVector
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
fseVector = FseVector(pg_connection_string="fsedoc://username:passwd@ip:port",
                      fse_connection_string="fseaddr://ip:port",
                      embedding_function=embeddings,
                      collection_name="knowledge_test")

#init chain
DEPLOYMENT_NAME = "gpt-35-turbo"  # gpt-35-turbo gpt-35-turbo-16k
llm = AzureChatOpenAI(deployment_name=DEPLOYMENT_NAME)
chain = RetrievalQAWithSourcesChain.from_chain_type(llm=llm,
                                chain_type="stuff", verbose=False, memory=None,
                                retriever=fseVector.as_retriever(search_type='similarity_score_threshold',
                                                                search_kwargs={'score_threshold': 0.3, 'k': 3}),
                                return_source_documents=False)

#add doc or texts
fseVector.add_texts(texts=[full_text], metadatas=[{"source": filename, "key_list": key_phrases}], ids=[str(idx)])    

#retrieval
result = chain({"question": key_phrases[0]})
output = f"Answer: {result['answer']}\nSources: {result['sources']}\nresult: {result}"
print(output)        
```

Other init fsevector methods
```
#from_texts
embeddings = OpenAIEmbeddings()
fseVector = FseVector.from_texts(
    pg_connection_string="fsedoc://username:passwd@ip:port",
    fse_connection_string="fseaddr://ip:port",
    collection_name="knowledge_test",
    texts=["teststssss"], embedding= embeddings, metadatas=[{"source": "teststssss"}], ids=[str(11111)], pre_delete_collection=True)

#from_documents
ids=[11]
embeddings = OpenAIEmbeddings()
doc=[Document(page_content="xxxx", metadata={"source": "teststssss","key_list":["emails", "get emails"]})]
fseVector = FseVector.from_documents(
    pg_connection_string="fsedoc://username:passwd@ip:port",
    fse_connection_string="fseaddr://ip:port",
    collection_name="knowledge_test",
    documents=doc,
    embedding= embeddings, ids=ids)

#from_embeddings
embeddings = OpenAIEmbeddings()
text_embeddings = embeddings.embed_documents(texts)
text_embedding_pairs = list(zip(texts, text_embeddings))
fseVector = FseVector.from_embeddings(
    pg_connection_string="fsedoc://username:passwd@ip:port",
    fse_connection_string="fseaddr://ip:port",
    collection_name="knowledge_test",
    text_embeddings=text_embedding_pairs,
    embedding= embeddings)
```

Supported interface
```
from_documents
from_texts
from_embeddings
from_existing_index
add_embeddings
add_texts
similarity_search
similarity_search_with_score
similarity_search_with_score_by_vector
similarity_search_by_vector
```

## Development
- CI pipeline
