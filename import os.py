import os
import openai
from langchain import ChainedModel, CompletionType


api_key = 'YOUR_API_KEY'
openai.api_key = api_key


model = ChainedModel(api_key=api_key, engine='text-davinci-003')


def extract_file_content(file_path):
    
    
    pass


def generate_answer(question, file_content):
    
    prompt = f"User Question: {question}\nFile Content: {file_content}\n"

    
    response = openai.Completion.create(
        engine='text-davinci-003',  
        prompt=prompt,
        max_tokens=100,  
        n=1,  
        stop=None,  
        temperature=0.7,  
        top_p=1.0,  
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    
    answer = response.choices[0].text.strip()

    return answer


while True:
    try:
        
        print("==== Agent Script ====")
        print("Please follow the instructions to interact with the agent:")
        print("1. Enter your question (or type 'exit' to quit).")
        print("2. Provide the path to the file you want to upload.")
        question = input("Question: ")
        if question.lower() == 'exit':
            break
        file_path = input("File Path: ")

        
        if not os.path.exists(file_path):
            raise FileNotFoundError("File not found.")
        file_content = extract_file_content(file_path)
        if not file_content:
            raise Exception("Failed to extract content from the file.")

        
        answer = generate_answer(question, file_content)
        print("\nAgent's Answer:")
        print(answer)
        print("=====================")
        print()

    except FileNotFoundError:
        print("Error: File not found. Please provide a valid file path.")
        print()

    except Exception as e:
        print("An error occurred:", str(e))
        print()