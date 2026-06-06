class StringReverse:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)


# Example usage
s = StringReverse("Python is easy to learn")
print("Original String:", s.text)
print("Reversed String:", s.reverse_words())
