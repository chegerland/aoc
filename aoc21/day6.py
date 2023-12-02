from collections import Counter

def read_input(filename):
    with open(filename) as file:
        line = file.readline().split(',')

    line = [int(num) for num in line] 
    return line

def evolve(state):
    append_fishes = 0
    for i, fish in enumerate(state):
        if fish != 0:
            state[i] -= 1
        else:
            state[i] = 6
            append_fishes += 1
    
    state.extend(append_fishes * [8])

    return state

def simulate(state, n):
    initial_state = state.copy()
    for i in range(n):
        evolve(state)
        print(i, state)

def state_to_dict(state):
    pop_dict = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for fish in state:
        pop_dict[fish] += 1
    
    return pop_dict

def get_population(day, initial_state):
    pop_dict = state_to_dict(initial_state)

    for i in range(day):
        zeros = pop_dict[0]
        for j in range(0, 8):
           pop_dict[j] = pop_dict[j + 1] 

        pop_dict[8] = zeros 
        pop_dict[6] += zeros
        
        #print(i, pop_dict)
    
    return pop_dict


def main():
    state = read_input("inputs/day6.txt")
    #state = [3,4,3,1,2]
    pop_dict = get_population(256, state)
    total_population = sum(pop_dict.values())
    print(total_population)
    #simulate(state, 25)
    #print(len(state))

if __name__ == "__main__":
    main()