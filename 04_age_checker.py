# functions go here

# checks useres enter an integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer. ")

# main routine goes here
tickets_sold = 0

while True:

    name = input("Enter your name (or 'xxx' to quit) ")

    if name == "xxx":
        break

    age = num_check("Age: ")

    if 12 <= age <=120:
        pass
    elif age < 12:
        print("Sorry you are too young for this movie")
        continue
    else:
        print("?? That looks like a typo, please try again.")


    tickets_sold += 1

print("you have sold {} ticket/s" .format(tickets_sold))
