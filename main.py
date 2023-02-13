from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader

# documents = SimpleDirectoryReader('index').load_data()
# index = GPTSimpleVectorIndex(documents)
index = GPTSimpleVectorIndex.load_from_disk('index.json')
response = index.query('What sins are forbidden in the first commandment?')
# index.save_to_disk('index.json')

print(response)