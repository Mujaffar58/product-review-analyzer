from textblob import TextBlob

def analyze_review_sentiment(review):
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity  # Range: -1 to +1

    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

def main():
    print("=== Product Review Sentiment Analyzer ===")
    while True:
        try:
            review = raw_input("Enter a product review (or type 'exit' to quit): ")
        except NameError:
            review = input("Enter a product review (or type 'exit' to quit): ")
        if review.lower() == 'exit':
            break
        result = analyze_review_sentiment(review)
        print("Sentiment:", result)
        print("------")

if __name__ == "__main__":
    main()
    