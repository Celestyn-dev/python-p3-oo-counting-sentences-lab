#!/usr/bin/env python3
class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value  # Use the setter here

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        temp = self.value.replace("!", ".").replace("?", ".")
        parts = temp.split(".")
        sentences = [part.strip() for part in parts if part.strip() != ""]
        return len(sentences)
