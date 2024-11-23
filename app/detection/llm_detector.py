from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

GOOGLE_API_KEY = "AIzaSyCCg21eLTOor53LJW3vAdoas3U9HbwfcQk"  # Replace with your actual Google API key

def detect_sensitive_data(file_content):
    prompt_template = """
    Analyze the following text and extract sensitive data. Categorize them into:
    - PII (Personally Identifiable Information)
    - PHI (Protected Health Information)
    - PCI (Payment Card Information)
    
    Text:
    {content}
    
    return this JSON schema:
    {{"PII": list[tuple(field_name, value)], "PHI": list[tuple(field_name, value)], "PCI": list[tuple(field_name, value)]}}
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3, google_api_key=GOOGLE_API_KEY)
    prompt = PromptTemplate(template=prompt_template, input_variables=["content"])
    chain = prompt | model

    response = chain.invoke({"content": file_content})
    raw_output = response.content  # Explicitly get the content of AIMessage

    cleaned_output = raw_output.strip("```").strip("json").strip()

    return cleaned_output


def process_file(file_path):
    with open(file_path, 'r') as f:
        file_content = f.read()
    return detect_sensitive_data(file_content)

def main():
    input_file = "demo.txt"
    try:
        results = process_file(input_file)
        print(f"Results for {input_file}:")
        print(results)
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    main()
