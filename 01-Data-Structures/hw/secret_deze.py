pizza = {"dough", "tomatoes", "pepperoni", "ground pepper", "sweet basil",
         "a lot of cheeeese", "onion", "garlic", "salt", "oregano"}
shaverma = {"lavash", "cucumbers", "tomatoes", "sauce", "fried chicken", "onion", "cabbage"}

print("Union of pizza and shaverma: ", pizza | shaverma)
print("Symmetric difference of pizza and shaverma: ", pizza ^ shaverma)
print("Pizza is subset of shaverma: ", pizza.issubset(shaverma))
print("Shaverma is subset of pizza: ", shaverma.issubset(pizza))
print("Pizza is subset of shaverma: ", pizza.issuperset(shaverma))
print("Shaverma is subset of pizza: ", shaverma.issuperset(pizza))
print("Difference between pizza and shaverma: ", pizza.difference(shaverma))
print("Difference between shaverma and pizza: ", shaverma.difference(pizza))
print("Intersection: ", pizza.intersection(shaverma))
