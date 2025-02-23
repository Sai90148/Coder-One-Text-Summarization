from transformers import pipeline

def summarize_text(text, max_length=200, min_length=50):
    """
    Summarizes the given text using the transformers pipeline.

    Args:
        text: The input text to be summarized.
        max_length: Maximum length of the summary.
        min_length: Minimum length of the summary.

    Returns:
        The summarized text.
        Returns None if there is an issue with summarization.
    """
    try:
        summarizer = pipeline("summarization")  # Uses a pre-trained summarization model

        summary = summarizer(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False  # For more deterministic output
        )[0]["summary_text"]
        return summary
    except Exception as e:
        print(f"An error occurred during summarization: {e}")
        return None



def main():
    while True:  # Loop to allow for multiple summarizations
        print("\nEnter your text below (or type 'exit' to quit):")
        text = ""
        while True:  # Allows multi-line input
            line = input()
            if line.lower() == "exit":
                return # Exits the entire program.
            if not line: # Empty line signals end of input
                break
            text += line + "\n"  # Add newline for preserving structure.

        if not text.strip(): # Check if the input is empty or just whitespace.
            print("No text entered. Please try again.")
            continue  # Go to next iteration of the loop

        try:
           max_len = int(input("Enter maximum summary length (words, optional, press Enter for default 200): ") or 200)
           min_len = int(input("Enter minimum summary length (words, optional, press Enter for default 50): ") or 50)
           if max_len < min_len:
               print("Max length should be greater than or equal to min length.")
               continue

        except ValueError:
            print("Invalid input for length. Using default values.")
            max_len = 200
            min_len = 50

        summary = summarize_text(text, max_length=max_len, min_length=min_len)

        if summary:
            print("\nSummarized Text:")
            print(summary)

        print("-" * 50)  # Separator between summaries



if __name__ == "__main__":
    main()