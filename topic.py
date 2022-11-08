




import random
topics = []
TOTAL_TOPICS = 5 #test this program with 5 topics

def main():
    num_used_topics = 0
    for i in range(TOTAL_TOPICS): #fill the list with items with an "A" in each one
        topics.append("A")

    generate_another_randnunber = True #boolean variable to control the outer loop
    continue_search = True #boolean to control the inner loop

    while continue_search: #OUTER LOOP
        continue_search=True

        while continue_search: #INNERLOOP
            randnumber = random.randint(0, TOTAL_TOPICS-1) #items in list start with 0, not 1
            if topics[randnumber]== "A":
                topics[randnumber]= "U"
                num_used_topics += 1
                continue_search= False
        print("\nRandom Topic Number: " + str(randnumber+1)) #items in list start with 0, so add 1
        print("List of topic avalibility by number:")
        for i in range (TOTAL_TOPICS):
            print("\t"+ str(i+1) + ". " + topics[i])
        
        if num_used_topics == TOTAL_TOPICS:
            print("There are no more topics avaliable at this time.")
            return() #quite the main() function
        else:
            answer = input("Would you like another random number Y/N: ")
            if answer.upper() == "n" or answer.upper() == "N":
                generate_another_randnunber= False

main()