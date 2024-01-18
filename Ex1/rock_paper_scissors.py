import random
player1=''
player2=''

def win_rule(user_input, machine_input):   
    user_count=0
    machine_count=0
    
    while True:
        track_dict={"user_count": user_count, "machine_count": machine_count}
        input_list=['rock', 'paper','scissors']
        machine_input=random.choice(input_list)
        print("machine input", machine_input)
        user_input=input('Please type in rock/ paper/ scissors:')
        if machine_input=='rock':
            if user_input!='rock':
                if user_input=='scissors':
                    machine_count+=1
                if user_input=='paper':
                    user_count+=1
            print(track_dict)
        elif machine_input=='paper':
            if user_input!='paper':
                if user_input=='rock':
                    machine_count+=1
                if user_input=='scissors':
                    user_count+=1
            print(track_dict)
    
        elif machine_input=='scissors':
            if user_input!='scissors':
                if user_input=='rock':
                    user_count+=1
                if user_input=='paper':
                    machine_count+=1
            print(track_dict)
        if user_count==3:
            print('The user wins')
            break
           
        if machine_count==3:
            print('The user loses')
            break
    return track_dict


win_rule(player1, player2)