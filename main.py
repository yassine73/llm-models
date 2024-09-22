import subprocess, time, os

## Get ids of running processes
def get_process_ids(process_name):
    try:
        result = subprocess.run(['pgrep', process_name], capture_output=True, text=True, check=True)
        process_ids = result.stdout.strip().split('\n')
        return process_ids
    except subprocess.CalledProcessError:
        print(f"No process named {process_name} found.")
        return []


## Ollama Model
def ollama_model():
    ## pip install langchain-ollama
    from langchain_ollama import ChatOllama
    
    ## Start ollama
    subprocess.Popen(["ollama", "serve"])
    time.sleep(2)
    
    ## Initialize Ollama & invoke
    llm = ChatOllama(model="llama2", temperature=0.7)
    print(llm.invoke("hi").content)
    
    ## Stop ollama
    for id_ in get_process_ids("ollama"):
        subprocess.check_call(["kill", id_])


## OpenAI Model
def openai_model():
    ## pip install langchain-openai
    from langchain_openai import ChatOpenAI
    
    ## OpenAI api key
    os.environ["OPENAI_API_KEY"] = "sk-..."
    
    ## Initialize OpenAI & invoke
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    print(llm.invoke("hi").content)
    


if __name__=="__main__":
    ollama_model()