from textblob import TextBlob

movie = input("🎬 Enter a movie description: ")

score = TextBlob(movie).sentiment.polarity

print("\n🤖 AI Analysis")

if score > 0:
    print("😊 This movie sounds positive!")
elif score < 0:
    print("😢 This movie sounds emotional!")
else:
    print("😐 This movie sounds neutral!")

print("Score:", round(score, 2))