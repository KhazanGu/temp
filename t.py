import requests

def call_chatgpt_api(prompt):
    url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer sk-"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 150
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()["choices"][0]["text"].strip()
    else:
        print("Error:", response.status_code)
        return None

# Example usage
prompt = "Once upon a time"
response = call_chatgpt_api(prompt)
print(response)
