# Mad Lib template
madlib_template = "I’ve had a very {adjective} day.\n"
madlib_template += "This morning, I dropped a box of {large_objects} on my {body_part}.\n"
madlib_template += "Then, at lunch, I went to {restaurant} for their delicious {first_food},\n"
madlib_template += "But the waiter brought me {second_food}, which I was not hungry for.\n"
madlib_template += "Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof."

# Get user input
adjective = input("Enter an adjective: ")
large_objects = input("Enter large objects (plural): ")
body_part = input("Enter a body part: ")
restaurant = input("Enter a restaurant: ")
first_food = input("Enter a first food: ")
second_food = input("Enter a second food: ")
large_object = input("Enter a large object: ")

# Fill in the Mad Lib template with user input
madlib_story = madlib_template.format(
    adjective=adjective,
    large_objects=large_objects,
    body_part=body_part,
    restaurant=restaurant,
    first_food=first_food,
    second_food=second_food,
    large_object=large_object
)

# Display the completed Mad Lib
print("\nYour Mad Lib Story:\n")
print(madlib_story)
