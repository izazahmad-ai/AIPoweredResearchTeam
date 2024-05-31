import os
from dotenv import load_dotenv, find_dotenv

def load_env():
    _ = load_dotenv(find_dotenv())

def get_openai_api_key():
    load_env()
    return os.getenv("OPENAI_API_KEY")

def pretty_print_result(result):
    parsed_result = []
    for line in result.split('\n'):
        if len(line) > 80:
            words = line.split(' ')
            new_line = ''
            for word in words:
                if len(new_line) + len(word) + 1 > 80:
                    parsed_result.append(new_line)
                    new_line = word
                else:
                    if new_line == '':
                        new_line = word
                    else:
                        new_line += ' ' + word
            parsed_result.append(new_line)
        else:
            parsed_result.append(line)
    return "\n".join(parsed_result)
