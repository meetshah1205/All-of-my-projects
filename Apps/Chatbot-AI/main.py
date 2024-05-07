import json
from difflib import get_close_matches

def load_knowledge(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def answer_question(question: str, knowledge: dict) -> str | None:
    for q in knowledge['questions']:
        if q['question'].lower() == question.lower():  
            return q['answer']

def chat_bot():
    knowledge_base: dict = load_knowledge('knowledge.json')
    while True:
        user_input: str = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break 
        best_match: str | None = find_best_match(user_input, [q['question'] for q in knowledge_base['questions']]) 
        if best_match:
            answer: str | None = answer_question(best_match, knowledge_base)
            print(f"Bot: {answer}")
        else:
            print("Bot: I'm sorry, I don't have an answer for that question. Can you please teach me?")
            new_input: str = input("Type the answer or 'skip' to skip: ")
            if new_input.lower() != 'skip':
                knowledge_base['questions'].append({'question': user_input, 'answer': new_input})
            elif new_input.lower() == 'skip':
                print("Bot: No problems :)")
                continue
            save_knowledge("knowledge.json", knowledge_base)
            print("Bot: Thank you for teaching me!")

if __name__ == '__main__':
    chat_bot()
