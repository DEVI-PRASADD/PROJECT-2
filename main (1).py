def count_words(text):
  """Counts the number of words in the input text."""
  words = text.split()
  return len(words)

def main():
  """Main function to run the Word Counter program."""
  try:
      user_input = input("Enter a sentence or paragraph: ").strip()
      if not user_input:
          raise ValueError("Input cannot be empty. Please enter some text.")
      word_count = count_words(user_input)
      print(f"The number of words is: {word_count}")
  except ValueError as e:
      print(e)

if __name__ == "__main__":
  main()
