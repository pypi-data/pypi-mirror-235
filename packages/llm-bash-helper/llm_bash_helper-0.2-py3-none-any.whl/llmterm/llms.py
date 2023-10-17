import os
from llama_cpp import Llama
from langchain.llms import OpenAI
from rich.prompt import Prompt
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain





def getOpenAIKey():
    if os.environ.get("OPENAI_API_KEY") is None:
        key = Prompt.ask("""Enter your OpenAI API key. 
It will be stored as `OPENAI_API_KEY` environment variable. 
To make this persistent, add it to your .bashrc file (or your shell's equivalent)""")
        os.environ["OPENAI_API_KEY"] = key
    else:
        return os.environ.get("OPENAI_API_KEY")


def translateLlama(description, previous=[]):
    llm = Llama(model_path="./.models/llama-2-7b.Q5_K_S.gguf", verbose=False)
    output = llm(f"Q: What is '{description}' as a bash oneliner? A: The exact command is '", max_tokens=64, stop=["Q:", "\n"], echo=False)
    command = output['choices'][0]['text']
    command = command[:-1]
    return command
    

def translateGPT4(description, previous=[]):
    getOpenAIKey()
    llm = OpenAI(model_name="text-davinci-003", verbose=False)

    template = """Rewrite '{description}' as a bash oneliner.
Only include the exact command(s) in your output without quotes or backticks.
"""

    prompt = PromptTemplate(template=template, input_variables=["description"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    command = llm_chain.run(description)

    return command
