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
        return file.read()

def parse_template():
    pass

def merge():
    pass


if __name__ == "__main__":
    print_welcome_message()
    print_user_prompst()
    read_template("./assets/dark_and_stormy_night_template.txt")