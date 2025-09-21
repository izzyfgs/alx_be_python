# Prompt user for weather input
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Dictionary of recommendations
advice = {
    "sunny": "Wear a t-shirt and sunglasses.",
    "rainy": "Don't forget your umbrella and a raincoat.",
    "cold": "Make sure to wear a warm coat and a scarf."
}

# Print advice, or default message if input not found
print(advice.get(weather, "Sorry, I don't have recommendations for this weather."))
