import random
# write your code here
friends = []


def lucky_one(friends):
    lucky_one = random.choice(friends)
    return lucky_one

# function to clac the split value then assign it to friends


def split_bill(friends):
    bill = int(input("Enter the total bill value:"))
    print()
    split_value = round(bill / len(friends), 2)
    lucky_or_not = input(
        'Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    print()
    if lucky_or_not == 'Yes':
        lucky_friend = lucky_one(friends)
        split_value = round(bill / (len(friends) - 1), 2)
        friends = dict.fromkeys(friends, split_value)
        friends[lucky_friend] = 0
        print(f"{lucky_friend} is the lucky one!")
    else:
        friends = dict.fromkeys(friends, split_value)
        print("No one is going to be lucky")
    print()
    print(friends)

# function to invite friends and save names in list then
# use split_bill function to assign split value to friends


def invite_friends(friends):
    friends_count = int(
        input("Enter the number of friends joining (including you):"))
    print()
    if friends_count > 0:
        print("Enter the name of every friend (including you), each on a new line:")
        # taking friends names and save it in list
        for i in range(friends_count):
            friends.append(input())
        print()
        split_bill(friends)

    else:
        print("No one is joining for the party")


invite_friends(friends)
