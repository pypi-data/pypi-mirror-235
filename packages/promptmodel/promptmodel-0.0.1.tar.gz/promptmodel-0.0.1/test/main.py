from promptmodel import FastLLM
from promptmodel.utils.prompt_util import set_inputs_to_prompts
import time
promptmodel = FastLLM()

extract_keyword_prompt = promptmodel.get_prompts("extract_keyword")

@promptmodel.register
def test():
	response = promptmodel.fastmodel("test").generate({})
	print(response)

# print("hello")
# @promptmodel.with_llm
# def test():
# 	response = promptmodel.llm("extract_keyword").generate({})
# 	print(response)

while True:
    print("Awake")
    time.sleep(3)