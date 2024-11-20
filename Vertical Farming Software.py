all_plants =  {"lettuce": {"moisture": "moderate", "sunlight": "full sun to partial shade", "nutrients": "low to moderate"},
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

new_plant_database = {}  # Separate database for newly added plants

while True:
    question = input("Do you want to search info on a plant or add a new plant? (search|add|exit): ").lower()
    if question == "exit":
        break

    if question == "search":
        plant1 = input("\nEnter type of plant: ").lower()
        
        # Search in both databases
        if plant1 in all_plants:
            requirements = all_plants[plant1]
        elif plant1 in new_plant_database:
            requirements = new_plant_database[plant1]
        else:
            print("Plant not found.")
            continue

        print(f"\n{plant1.capitalize()} Requirements:")
        print("Moisture:", requirements["moisture"])
        print("Sunlight:", requirements["sunlight"])
        print("Nutrients:", requirements["nutrients"])

    elif question == "add":
        new_plant_name = input("Enter name of plant: ").lower()
        moisture = input("Enter moisture level (low, moderate, high): ").lower()
        sunlight = input("Enter sunlight level (full sun, partial shade, indirect light): ").lower()
        nutrients = input("Enter nutrient level (low, moderate, high): ").lower()

        # Validate and add to the new plant database
        new_plant_database[new_plant_name] = {"moisture": moisture, "sunlight": sunlight, "nutrients": nutrients}
        print(f"\n{new_plant_name.capitalize()} has been added to the database.\n")

