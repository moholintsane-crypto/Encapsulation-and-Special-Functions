class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        # [::-1] creates a slice reversed copy of the string 
        # that moves backwards from the end to the start
        return self.text[::-1]

# Example usage:
if __name__ == "__main__":
    my_string = input("Enter a string to reverse: ")
    reverser = StringReverser(my_string)
    print(f"Original: {my_string}")
    print(f"Reversed: {reverser.reverse()}")
