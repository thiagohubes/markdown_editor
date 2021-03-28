list_of_commands = "Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line\nSpecial commands: !help !done"
final = []


def get_format():
    return input("- Choose a formatter: ")


def get_text():
    return input("- Text: ")


def bold(txt):
    return f"**{txt}**"


def italic(txt):
    return f"*{txt}*"


def inline_code(txt):
    return f"`{txt}`"


def link(name, website):
    return f"[{name}]({website})"


def header(txt, lvl):
    tag = []
    for i in range(lvl):
        tag += "#"
    return f"{''.join(tag)} {txt}\n"


def ordered_list(row):
    a = []
    for i in range(row):
        b = input(f"Row #{i+1}: ")
        a.append((f"{i+1}. " + b + "\n"))

    return "".join(a)


def unordered_list(row):
    a = []
    for i in range(row):
        b = input(f"Row #{i+1}: ")
        a.append((f"* " + b + "\n"))

    return "".join(a)


user = get_format()

while user != "!done":
    if user == "!help":
        print(list_of_commands)
        user = get_format()
        continue

    elif user == "plain":
        markdown = get_text()

    elif user == "bold":
        text = get_text()
        markdown = bold(text)

    elif user == "italic":
        text = get_text()
        markdown = italic(text)

    elif user == "inline-code":
        text = get_text()
        markdown = inline_code(text)

    elif user == "link":
        label = input("Label: ")
        url = input("URL: ")
        markdown = link(label, url)

    elif user == "new-line":
        markdown = "\n"

    elif user == "header":
        level = int(input("- Level: "))
        if 1 <= level <= 6:
            text = get_text()
            markdown = header(text, level)
        else:
            print("The level should be within the range of 1 to 6")
            continue
    elif user == "ordered-list":
        rows = int(input("- Number of rows: "))
        if rows <= 0:
            print("The number of rows should be greater than zero")
            continue
        markdown = ordered_list(rows)
    elif user == "unordered-list":
        rows = int(input("- Number of rows: "))
        if rows <= 0:
            print("The number of rows should be greater than zero")
            continue
        markdown = unordered_list(rows)
    else:
        print("Unknown formatting type or command. Please try again.")
        user = get_format()
        continue

    final.append(markdown)
    text = "".join(final)
    print(text)
    with open("output.md", 'w') as f:
        f.write(text)
    user = get_format()
