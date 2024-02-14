import random,time,sys,os

print('''
    Vroom...vroom
      
                                 .-=--.                
                         .' .--. '.              
                        :  : .-.'. :    _ _         
                        :  : : .': :   (o)o)     
                        :  '. '-' .'   ////      
                         _'.__'--=' '-.//>'       
                     .-'               /         
                     '---..____...---''          



      ''')

MAX_NUM_SNAILS = 10
finish_line = 10
boost_speed = 5

while(True):
    print("How many snails are here , Max:",MAX_NUM_SNAILS)
    response = int(input(">"))
    if(1 < response < MAX_NUM_SNAILS):
        break
    print("Snails can be between 2 and 10")

snail_names =[]


for i  in range(1,response+1):
    while(True):
        print("Enter snail #",str(i),"name")
        name = input(">")
        if(len(name) == 0):
            print("please enter a name")
        elif name in snail_names:
            print("Name already taken")
        else:
            break
    snail_names.append(name)


print("\n" * 8)
print("START"+(' ' * (finish_line)) + "FINISH")
print("|"+(' ' * (finish_line)) + (' ' * 5) + "|")

# Display snail at the start of the line

snail_progress ={}

for snail in snail_names:
    print(snail[:MAX_NUM_SNAILS])
    print(".")
    snail_progress[snail] = 0

time.sleep(2) # calm before the storm

while(True):
    
    for _ in range(random.randint(1,response//2)):
        chosen_one = random.choice(snail_names)
        snail_progress[chosen_one] += 1

        if(snail_progress[chosen_one] == finish_line):
            print(f"looks like {chosen_one} won the.....Zzzzz")
            sys.exit()
    # time.sleep(2)
    # print("\n" * 10)

    print('START' + (' ' * finish_line) + "FINISH")
    print("|"+(' ' * (finish_line)) + (' ' * 5) + "|")

    for snail in snail_names:
        spaces =snail_progress[snail]
        print((' ' * spaces) + snail)
        print(('.' * spaces + "@>"))

    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
        # print((' ' * spaces) + ('.' * spaces) + '''
        #   .--.  oo
        # _(____)\\
        # `~~~~~~~'
        #   ''' * spaces)
       
           


       




