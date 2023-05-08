# GPT-3.5 Turbo Answer Resolver

This script uses OpenAI's GPT-3.5 Turbo API to generate and evaluate potential answers to a user's question. It first generates three answer options, then reflects on the flaws and faulty logic in each option, and finally, chooses the best answer and improves it.

## What this script does:

1. Takes a user's question as input.
2. Generates three answer options.
3. Reflects on the flaws and faulty logic of each answer option.
4. Chooses the best answer and improves it.

## How to comment out print lines for Answer Option and Reflection Response:

To comment out the print lines for the answer options and reflection response, simply add a `#` at the beginning of the corresponding lines in the `main` function:

```python
# print(f"\033[31mAnswer Option\033[0m \033[31m{i + 1}\033[0m \033[31m{chain_of_thought_responses}\033[0m")  # Red color
# print()
# ...
# print(f"\033[33mReflection response:\033[0m \033[33m{reflection_response}\033[0m")  # Orange color
```

### How to get an API key:
- Sign up for an OpenAI account at https://beta.openai.com/signup/
- After logging in, go to the API Keys page: https://beta.openai.com/account/api-keys
- Click "Create API Key" to generate a new API key.
- Copy the key (it should start with sk-).

## How to use the API key in this script:
Replace the existing API key in the script with your own:
```
openai.api_key = "your_api_key_here"
```

Using an API key allows you to interact with OpenAI's API to generate more accurate and relevant responses based on your input.

#### Dependencies:
To run the script, you need to have the openai Python library installed. You can install it using pip:
```
pip install openai
```
## Running the Script

To run the script, follow these steps:

1. Ensure that you have Python installed on your system. You can download Python from https://www.python.org/downloads/
2. Install the `openai` library, if you haven't already, using the command: `pip install openai`
3. Save the script to a file named `gpt_answer_resolver.py`.
4. Replace the placeholder API key with your own OpenAI API key in the script.
5. Open a terminal or command prompt, navigate to the directory containing the `gpt_answer_resolver.py` file, and run the following command: `python gpt_answer_resolver.py`
6. When prompted, enter your question and press Enter. The script will generate answer options, reflect on their flaws, and provide an improved answer.

If you have any issues or need further assistance, consult the [OpenAI API documentation](https://beta.openai.com/docs/).

#### To run nicely on windows:
What you can do is download python and install it automatically 
