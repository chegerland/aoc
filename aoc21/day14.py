from collections import Counter, defaultdict

def read_input(filename):
    lines = []
    with open(filename) as file:

        template = file.readline().replace('\n', '')
        _ = file.readline()
        rules = {}
        for line in file:
            split = line.split()
            rules[split[0]] = split[2]

    return template, rules

def get_pairs(template):
    pairs = []
    for i in range(0, len(template)-1):
        pairs.append(template[i:i+2])
    return pairs

def apply_rules_to_pairs(rules, pairs):
    triplets = []
    for pair in pairs:
        template = pair
        if pair in rules.keys():
            template = pair[0] + rules[pair] + pair[1]

        triplets.append(template)
    
    return triplets

def stitch_together_triplets(triplets):
    result_template = ""
    for i in range(0, len(triplets)-1):
        result_template += triplets[i][:-1]

    result_template += triplets[-1]
    return result_template


def apply_rules(rules, template):

    # get pairs from the template
    pairs = get_pairs(template)

    # apply rules to pairs
    triplets = apply_rules_to_pairs(rules, pairs)

    ## stitch pairs together
    result_template = stitch_together_triplets(triplets)

    return result_template

def apply_rules_steps(rules, template, steps):
    old_template = template

    for i in range(0, steps):
        new_template = apply_rules(rules, old_template)
        old_template = new_template

    return old_template

def get_puzzle_result(template):
    # get character count
    counts = Counter(list(template)).values()

    return max(counts) - min(counts)

def solve_puzzle_2(template, rules, steps):

    # create a dict character -> count
    char2count = Counter(list(template))
    
    # create a dict pair -> count
    pair2count = defaultdict(int)
    for i in range(0, len(template)-1):
        pair2count[template[i:i+2]] += 1

    print(pair2count, char2count)

    for i in range(0, steps):
        # create new pairs
        new_pairs = defaultdict(int)
        for pair, count in pair2count.items():

            # create new pair
            character = rules[pair]
            new_pair_1 = pair[0] + character
            new_pair_2 = character + pair[1]

            # update the pair dict
            new_pairs[new_pair_1] += count
            new_pairs[new_pair_2] += count

            # update the char dict
            char2count[character] += count

        pair2count = new_pairs

        #print(pair2count, char2count) 
    
    return max(char2count.values()) - min(char2count.values())
        






def main():
    template, rules = read_input("inputs/day14.txt")
    #puzzle_result = get_puzzle_result(apply_rules_steps(rules, template, 10))
    #print(puzzle_result)
    print(solve_puzzle_2(template, rules, 40))


if __name__ == "__main__":
    main()