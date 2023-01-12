from instagrapi import Client

user = input('What is your username?')
password = input('What is your password?')
api = Client()
api.login(user, password)

user_id = api.user_id_from_username(user)

following = api.user_followers(user_id, 0)
followers = api.user_following(user_id, 0)



with open('following.txt','w') as f:
    for i in following.values():
        username = i.username
        f.write(username + '\n')

with open('followers.txt','w') as f:
    for i in followers.values():
        username = i.username
        f.write(username + '\n')



with open('followers.txt') as file:
    followers_list = file.read().splitlines()

with open('following.txt') as file:
    following_list = file.read().splitlines()

good_accs = [user for user in followers_list if user not in following_list]

for user in good_accs:
    print(user)
