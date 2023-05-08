import openai

openai.api_key = "APIKEYHERE"
border = "=" * 50

def generate_gpt_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].message['content'].strip()

def main():
    user_question = input("Ask GPT a question to resolve: ")

    chain_of_thought_prompt = f"Question. {user_question} Answer: Let's work this out in a step by step way to be sure we have the right answer."
    chain_of_thought_responses = []
    print(border)
    for i in range(3):
        chain_of_thought_response = generate_gpt_response([
            {"role": "user", "content": chain_of_thought_prompt},
        ])
        chain_of_thought_responses.append(f"Answer Option {i + 1}: {chain_of_thought_response}")
        print(f"\033[31mAnswer Option\033[0m \033[31m{i + 1}\033[0m \033[31m{chain_of_thought_responses}\033[0m")  # Red color
        print()
    print(border)

    reflection_prompt = f'"{user_question}"\n\n' + "\n".join(chain_of_thought_responses)
    reflection_prompt += '\n\nYou are a researcher tasked with investigating the three answer options provided. List the flaws and faulty logic of each answer option. Let\'s think step by step:'
    reflection_response = generate_gpt_response([
        {"role": "user", "content": reflection_prompt},
    ])
    print(f"\033[33mReflection response:\033[0m \033[33m{reflection_response}\033[0m")  # Orange color
    print(border)

    resolver_prompt = f"You are a resolver tasked with 1) finding which of the answer options the researcher thought was best 2) improving that answer, and 3) Printing the improved answer in full. Let's work this out in a step by step way to be sure we have the right answer:\n\n{reflection_response}"
    self_dialogue = generate_gpt_response([
        {"role": "user", "content": resolver_prompt},
    ])
    print(f"\033[32mSelf Dialogue Response:\033[0m \033[32m{self_dialogue}\033[0m")  # Green color

if __name__ == "__main__":
    main()
