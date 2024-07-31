# To solve the problem of distributing apples among Ram, Sham, and Rahim in proportion to their contributions, I developed a Python program that ensures each person receives apples closest to their proportional share, without splitting any apples. Ram paid 50 rupees (50%), Sham paid 30 rupees (30%), and Rahim paid 20 rupees (20%). Based on these proportions, I calculated the target share of the total apple weight each person should receive.

# The program takes apple weights as input until the user signals the end of input with -1. I then sorted the apples in descending order of weight, which allows for more accurate allocation of heavier apples to match the larger proportional shares. The distribution logic allocates apples to the person whose current total weight is farthest from their target proportion, ensuring the distribution is as fair as possible.

# Finally, the program outputs the distribution, listing the weights of apples each person receives. This method ensures a fair and efficient distribution of whole apples according to their contributions, demonstrating an effective approach to solving proportional allocation problems.

def distribute_apples():
    total_amount = 100
    proportions = {
        'Ram': 50 / total_amount,
        'Sham': 30 / total_amount,
        'Rahim': 20 / total_amount
    }
    
    apple_weights = []
    while True:
        weight = int(input("Enter apple weight in grams (-1 to stop ): "))
        if weight == -1:
            break
        apple_weights.append(weight)
    
    apple_weights.sort(reverse=True)
    
    distribution = {'Ram': [], 'Sham': [], 'Rahim': []}
    total_weight = sum(apple_weights)
    allocated_weight = {'Ram': 0, 'Sham': 0, 'Rahim': 0}
    
    for weight in apple_weights:
        # Find the person who needs more weight in proportion
        min_person = min(allocated_weight, key=lambda person: allocated_weight[person] / (proportions[person] * total_weight))
        distribution[min_person].append(weight)
        allocated_weight[min_person] += weight
    
    
    print("Distribution Result :")
    for person in distribution:
        print(f"{person}: {', '.join(map(str, distribution[person]))}")

distribute_apples()
