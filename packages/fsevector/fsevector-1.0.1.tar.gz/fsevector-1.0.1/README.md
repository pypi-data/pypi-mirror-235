# a fse vecstore for langchain


## Installation

```console
pip install fsevector
```

## Documentation

More information can be found on the [examples](https://gitlab.deepglint.com/chenbo/fsevector/-/blob/main/examples/fsevector_fromtexts_test.py)

## Usage
使用例子
```python
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_base = os.environ["OPENAI_API_BASE"]
openai.api_version = os.environ["OPENAI_API_VERSION"]
openai.api_type = os.environ["OPENAI_API_TYPE"]

#初始化fseVector
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
fseVector = FseVector.from_texts(
    pg_connection_string="fsedoc://username:passwd@ip:port",
    fse_connection_string="fseaddr://ip:port",
    collection_name="knowledge_test",
    texts=["teststssss"], embedding= embeddings, metadatas=[{"source": "teststssss"}], ids=[str(11111)], pre_delete_collection=True)

#初始化chain
prompt_1 = prompt_qa()  # prompt要尽量简短和高效. law
DEPLOYMENT_NAME = "gpt-35-turbo"  # gpt-35-turbo gpt-35-turbo-16k
llm = AzureChatOpenAI(deployment_name=DEPLOYMENT_NAME)
chain = RetrievalQAWithSourcesChain.from_chain_type(llm=llm,
                                chain_type="stuff", verbose=False, memory=None,
                                retriever=fseVector.as_retriever(search_type='similarity_score_threshold',
                                                                search_kwargs={'score_threshold': 0.3, 'k': 3}),
                                return_source_documents=False,
                                chain_type_kwargs={'prompt': prompt_1})

#添加文档
fseVector.add_texts(texts=[full_text], metadatas=[{"source": filename, "key_list": key_phrases}], ids=[str(idx)])    

#搜索
result = chain({"question": key_phrases[0]})
output = f"Answer: {result['answer']}\nSources: {result['sources']}\nresult: {result}"
print(output)
        
```

## Development
- CI pipeline
