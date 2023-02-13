from gpt_index import GPTTreeIndex, MockLLMPredictor, SimpleDirectoryReader

# the "mock" llm predictor is our token counter
llm_predictor = MockLLMPredictor(max_tokens=256)

from gpt_index import GPTTreeIndex, MockLLMPredictor, SimpleDirectoryReader

documents = SimpleDirectoryReader('./index').load_data()
# the "mock" llm predictor is our token counter
llm_predictor = MockLLMPredictor(max_tokens=256)
# pass the "mock" llm_predictor into GPTTreeIndex during index construction
index = GPTTreeIndex(documents, llm_predictor=llm_predictor)

# get number of tokens used
print(llm_predictor.last_token_usage)