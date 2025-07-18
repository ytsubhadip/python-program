import random
def encode(user_msg):
    encode=[]
   
    words = list(user_msg.split(" "))
    for word in words:
        first_random=""
        last_random =""

        if len(word) <3:
            a = word[::-1]
        elif len(word) > 3:
            a = word[1:] + word[0]
        
        for _ in range(3):
            r = random.randrange(97,122+1)
            first_random += chr(r)

        for _ in range(3):
            r = random.randrange(97,122+1)
            last_random +=chr(r)

        new_word = first_random + a + last_random

        encode.append(new_word)
    word = ' '.join(encode)
    print(word)

def decode(msg):
    words = list(msg.split(" "))
    decode =[]
    for word in words:
        new_word = word[3:-3]

        if len(word) < 3:
            decode.append(new_word[::-1])
        elif len(word) > 3:
            decode.append(new_word[-1]+new_word[:-1])
    new = ' '.join(decode)
    print(new)    



user_msg = input("Enter your message: ")
print("1. Encode Message")
print("2. Decode Message")
z = int(input("Enter: "))
if(z == 1):
    encode(user_msg)
elif(z == 2):
    decode(user_msg)


