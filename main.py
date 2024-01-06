import g4f
import logging
import traceback
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(BASE_DIR)

try:
    logging.basicConfig(filename=os.path.join(BASE_DIR, 'logs.log'),
                    format='[%(asctime)s | %(levelname)s]: %(message)s',
                    datefmt='%m.%d.%Y %H:%M:%S',
                    level=logging.CRITICAL,
                    encoding='utf-8')
except:
    try:
        logging.basicConfig(filename=os.path.join(BASE_DIR, 'logs.log'),
                    format='[%(asctime)s | %(levelname)s]: %(message)s',
                    datefmt='%m.%d.%Y %H:%M:%S',
                    level=logging.CRITICAL)
    except:
        print(traceback.format_exc())

CHAT_MODEL = 'gpt-3.5-turbo'

g4f.logging = True
g4f.check_version = False

def ask(prompt: str) -> str:
    messages = [{"role": "user","content": prompt}]

    response = g4f.ChatCompletion.create(
        model=CHAT_MODEL,
        messages=messages,
        stream=True,
    )

    ans_message = ''
    for message in response:
        ans_message += message

    return ans_message

def main() -> None:
    print("Free ChatGPT by JuiceFW\n")

    while True:
        prompt = input()
        
        if not prompt:
            continue

        answer = ask(prompt)
        
        print("\n")
        print(answer)
        print("\n")

if __name__ == "__main__":
    main()