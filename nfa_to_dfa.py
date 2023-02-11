def delta(state, alphabet, rules, dfa):
    """
    Find result of state for every input
    """
    result = []
    i = 0
    for letter in alphabet:
        res = ''
        for a in state:
            for idx in rules:
                if idx[0] == str(a) and idx[1] == letter:
                    if idx[2] not in res:
                        res += idx[2]
        result.append(''.join(sorted(res)))
        i += 1
    dfa[state] = result


def set_final_states(final, dfa_dict):
    """
    Set final states of DFA
    """
    new_final_state = []

    for init_final_state in final:
        for state in dfa_dict.keys():
            if init_final_state in state:
                new_final_state.append(state)
    return new_final_state


def states_queue(dfa_dict):
    """
    Accessible states that have yet to be checked
    """
    temp = []
    for state in dfa_dict:
        for x in dfa_dict[state]:
            if (x not in dfa_dict.keys()) and x:
                temp.append(x)
    return temp


def export_file(dfa_dict, alphabet, initial, final):
    """
    Create and export to file
    """
    dfa_output = open("DFA.txt", "w")

    dfa_output.write(f"{len(dfa_dict)}\t\t//Number of states\n")

    for a in alphabet:
        dfa_output.write(a)
    dfa_output.write(f"\t\t// {len(alphabet)} symbols in the alphabet\n")

    dfa_output.write(f"{initial}\t\t// Initial state(s)\n")

    for f in final:
        dfa_output.write(f"{f} ")
    dfa_output.write(f"\t\t// Final state(s)\n")

    for state in dfa_dict:
        i = 0
        for result in dfa_dict[state]:
            if state == '':
                state = '_'
            if result == '':
                result = '_'
            dfa_output.write(f"{state} {alphabet[i]} {result}")
            dfa_output.write(f"\t\t// From state {state} with input {alphabet[i]} next state is {result}\n")
            i += 1
    dfa_output.close()


def main():
    dfa_result_dict = {}
    states_to_examine = []
    alphabet = []
    rules = []

    # Open and read from file
    nfa_input = open("NFA.txt", "r").readlines()

    count = 0
    states_num = 0
    initial_state = ''
    final_states = ''

    for line in nfa_input:
        line = line.split("//")
        if count == 0:
            states_num = int(line[0])
        elif count == 1:
            alphabet = list(line[0].strip())
        elif count == 2:
            initial_state = str(line[0]).strip()
        elif count == 3:
            final_states = (str(line[0]).strip())
        else:
            rules.append(line[0].strip())
        count += 1

    final_states = list(final_states)

    # Check if states (n) & inputs (m) < 10
    if len(alphabet) > 10:
        print("Error: Too many inputs.")
    if states_num > 10:
        print("Error: Too many states.")

    states_to_examine.append(initial_state)

    while True:
        for state in states_to_examine:
            delta(state, alphabet, rules, dfa_result_dict)
            states_to_examine = states_queue(dfa_result_dict).copy()

        if not states_to_examine:
            break

    final_states = (set_final_states(final_states, dfa_result_dict)).copy()

    export_file(dfa_result_dict, alphabet, initial_state, final_states)
    print(f"\n{dfa_result_dict}")


if __name__ == "__main__":
    main()
