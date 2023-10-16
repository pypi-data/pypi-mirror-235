from promptmodel import Client, PromptModel
# from promptmodel.utils.prompt_util import set_inputs_to_prompts
import time
client = Client()

extract_keyword_prompt = PromptModel("extract_keyword").prompts()

@client.register
def test():
	response = PromptModel("test").generate({})
	print(response)

# print("hello")
# @promptmodel.with_llm
# def test():
# 	response = promptmodel.llm("extract_keyword").generate({})
# 	print(response)

# while True:
#     print("Awake")
#     time.sleep(3)