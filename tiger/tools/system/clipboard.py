import pyperclip


def copy(text):
    pyperclip.copy(text)



tool_name = "system.clipboard.copy"
tool_obj = copy
tool_requirements = ["pyperclip==1.8.2"]
