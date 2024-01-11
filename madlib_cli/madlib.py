import re

def print_welcome_message():
    print("""
        Let's make a Madlib!
          
        I will be asking you for a few words to complete our story.
        Please type appropriate responses in your terminal.
        When you are done, I will read out your Madlib!
          """)

def print_user_prompst():
    adj_one = input("Type an Adjective > ")
    adj_two= input("Type another Adjective > ")
    adj_three= input("Type a Noun > ")
    return adj_one,adj_two,adj_three

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
    user_inputs = print_user_prompst()
    template = read_template("./assets/dark_and_stormy_night_template.txt")
    stripped_template, parts_of_speech = parse_template(template)
    completed_madlib = merge(stripped_template, user_inputs)
    print(completed_madlib)