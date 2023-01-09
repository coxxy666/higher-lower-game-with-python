import random
from artwork import logo,vs
from data import data


print(logo)

score = 0

game_should_contine = True

account_a = random.choice(data)
account_b = random.choice(data)

while game_should_contine :
    def data_collection(account) :
        account_name = account['name']
        account_desc = account['description']
        account_country = account['country']

        return(f"NAME : {account_name},  WORK {account_desc},from {account_country}")

    def check_answer(follower_ask, a_follower_count, b_follower_count):

        if a_follower_count > b_follower_count :
            return follower_ask == 'a'
        else :
            return follower_ask == 'b'

    account_a =  is_correct
    account_b = random.choice(data)
    
    while account_a == account_b :
        account_b = random.choice(data) 

    print(f"Compare A : {data_collection(account_a)}\n")

    print(vs)

    print(f"Compare B : {data_collection(account_b)}\n")

    follower_ask = input("Who has more followers ? type 'A' or 'B' :\n").lower()


    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']


    is_correct = check_answer(follower_ask, a_follower_count, b_follower_count)

    if is_correct :
        score += 1
        print(f"YOU ARE RIGHT  CURRENT SCORE : {score}")
    else :
        game_should_contine = False
        print(f"SORRY, THAT IS WRONG SCORE : {score}")
