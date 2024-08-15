"""2.  Imagine  you  are  doing  a  workout  routine,  and  you  have  to  complete  100jumping jacks. Write a program that: Asks you to perform 10 jumping jacks at a time. After each set, it asks, "Are you tired?" If you reply "yes" or "y," it should ask if you want to skip the remaining sets. If  you  reply  "yes"  or  "y,"  it  should  break  and  print,  "You  completed  a  total  ofjumping jacks." """

target = int(100)
complete_set = int(target / 10)

for set in range(1, complete_set + 1):
    
    print(f"Set {set} of {complete_set}:")

    for j in range(1, 11):
        jump = input(f"Jump {j} completed. Press ENTER")
    
    if set == complete_set:
        print(f"Congratulations..!! You completed all {set} sets.")
        break

    tired = input("Are you tired? Press (y or n): ").lower()
    
    if tired == "y":
        
        skip = input("Do you want to skip the Remaining sets? (y or n): ").lower()

        if skip == "y":
            print(f"You completed a total of {set*10} jumping jacks out of {target}")
            break
        
        elif skip == "n":
            print("Continue Jumping Jacks...")
            continue
    
    elif tired == "n":
        print("Let's Continue our Sets...")
        continue


# ----- Exit Program ----- #
exit()