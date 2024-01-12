import re

def print_welcome_message():
    print("""
        Let's make a Madlib!
          
        I will be asking you for a few words to complete our story.
        Please type appropriate responses in your terminal.
        When you are done, I will read out your Madlib!
          """)

def print_user_prompst(parts_of_speech):
    user_inputs = []
    for part in parts_of_speech:
        response = input(f"Type a(n) {part} > ")
        user_inputs.append(response)
    return user_inputs

def read_template(text):
    with open(text) as file:
        content = file.read().strip()
        return content

def parse_template(template):
    parts_of_speech = re.findall(r"\{(.*?)\}", template)
    stripped_template = re.sub(r"\{.*?\}", "{}", template)
    return stripped_template, tuple(parts_of_speech)


def merge(stripped_template, parts):
    return stripped_template.format(*parts)


if __name__ == "__main__":
    print_welcome_message()
    template = read_template("./assets/video_game.txt")
    stripped_template, parts_of_speech = parse_template(template)
    user_inputs = print_user_prompst(parts_of_speech)
    completed_madlib = merge(stripped_template, user_inputs)
    print(completed_madlib)