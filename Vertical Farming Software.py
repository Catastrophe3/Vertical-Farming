# Determine name of plant
plant1 = input("Enter type of plant: ")

# Convert input to lowercase
plant1_lower = plant1.lower()

# Define the plant requirements dictionary
all_plants = {
    "lettuce": {"moisture": "moderate", "sunlight": "full sun to partial shade", "nutrients": "low to moderate"},
    "kale": {"moisture": "moderate", "sunlight": "full sun", "nutrients": "moderate"},
    "spinach": {"moisture": "moderate", "sunlight": "full sun to partial shade", "nutrients": "moderate"},
    "basil": {"moisture": "moderate", "sunlight": "full sun", "nutrients": "moderate"},
    "mint": {"moisture": "high", "sunlight": "partial shade to full sun", "nutrients": "low"},
    "cilantro": {"moisture": "moderate", "sunlight": "full sun", "nutrients": "low to moderate"},
    "strawberries": {"moisture": "moderate", "sunlight": "full sun", "nutrients": "moderate"},
    "tomatoes": {"moisture": "moderate to high", "sunlight": "full sun", "nutrients": "high"},
    "peppers": {"moisture": "moderate", "sunlight": "full sun", "nutrients": "moderate to high"},
    "cucumbers": {"moisture": "high", "sunlight": "full sun", "nutrients": "moderate"},
    "chard": {"moisture": "moderate", "sunlight": "full sun to partial shade", "nutrients": "moderate"},
    "arugula": {"moisture": "moderate", "sunlight": "full sun to partial shade", "nutrients": "low to moderate"},
    "mustard greens": {"moisture": "moderate", "sunlight": "full sun to partial shade", "nutrients": "moderate"},
    "pak choi": {"moisture": "high", "sunlight": "full sun to partial shade", "nutrients": "moderate"},
    "radishes": {"moisture": "moderate", "sunlight": "full sun", "nutrients": "low"},
    "microgreens": {"moisture": "high", "sunlight": "indirect light to partial shade", "nutrients": "moderate"},
    "collard greens": {"moisture": "moderate", "sunlight": "full sun to partial shade", "nutrients": "moderate"},
    "rocket": {"moisture": "moderate", "sunlight": "full sun to partial shade", "nutrients": "low to moderate"},
    "mizuna": {"moisture": "moderate", "sunlight": "full sun to partial shade", "nutrients": "low to moderate"},
    "swiss chard": {"moisture": "moderate", "sunlight": "full sun to partial shade", "nutrients": "moderate"},
    "baby kale": {"moisture": "moderate", "sunlight": "full sun", "nutrients": "moderate"},
    "oregano": {"moisture": "low to moderate", "sunlight": "full sun", "nutrients": "low"},
    "lemon balm": {"moisture": "moderate", "sunlight": "partial shade to full sun", "nutrients": "low to moderate"},
    "zinnia flowers": {"moisture": "moderate", "sunlight": "full sun", "nutrients": "low to moderate"},
}



# Check if the plant is in the dictionary and output the requirements
if plant1_lower in all_plants:
    requirements = all_plants[plant1_lower]
    print(f"\n{plant1_lower.capitalize()} Requirements:")
    print("Moisture:", requirements["moisture"])
    print("Sunlight:", requirements["sunlight"])
    print("Nutrients:", requirements["nutrients"])
else:
    print(f"Sorry, {plant1} is not in our plant database.")
