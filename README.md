# GPT-3.5 Turbo Answer Resolver

This script uses OpenAI's GPT-3.5 Turbo API to generate and evaluate potential answers to a user's question. It first generates three answer options, then reflects on the flaws and faulty logic in each option, and finally, chooses the best answer and improves it.

![Image Description](https://i.imgur.com/utRBcbM.gif)


## What this script does:

1. Takes a user's question as input.
2. Generates three answer options by requesting 3 individual responses for your question.
3. Reflects on the flaws and faulty logic of each answer option.
4. Chooses the best answer and improves it.

1. "Question" + "Answer: Let's work this out in a step by step way to be sure we have the right answer."

2. You are a researcher tasked with investigating the X response options provided. List the flaws and faulty logic of each answer option. Let's work this out in a step by step way to be sure we have all the errors:

3. You are a resolver tasked with 1) finding which of the X answer options the researcher thought was best 2) improving that answer, and 3) Printing the improved answer in full. Let's work this out in a step by step way to be sure we have the right answer:


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

# Automatic running on Windows:
What you can do is run the powershell file I have provided by opening powershell and running it from the command line. This will install python if you don't already have it, insteall the openai library then execute the script. If the script doesn't already exist in the same folder, it will download it from this repository.


Project inspired by
- https://www.youtube.com/@ai-explained-
