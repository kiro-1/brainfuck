import sys

#globals
position = 0 #tracks the position of the memory head
memory_tape = [0] #holds the data in the memoryb tape
instruction_tape = [] # a complete list of all the instructions
matching_pos = {} # a dictionary for finding matching brackets
reverse_matching_pos = {} # a dictionary for finding brackets the other way around
instruction_tape_counter = 0 # counts the position on the instruction tape
brackets_positions = []# temp variable for constructing dictionaries

#populates the instruction tape
with open(sys.argv[1],"r") as f: instruction_tape = list(f.read())

#generate a list with all the positions of starting brackets
for j in range(len(instruction_tape)):
    if instruction_tape[j] == "[":
        brackets_positions.append(j)

# a function that finds the position of the closing bracket for the position of the bracket you enter
def find_bracket(b_pos):
    global matching_pos
    level = 0
    Temp_counter = b_pos+1
    while True:
        if instruction_tape[Temp_counter] == "]":
            if level > 0 :
                level -= 1
            else:
                matching_pos[b_pos] = Temp_counter
                break
        elif instruction_tape[Temp_counter] == "[":
            level += 1
        Temp_counter += 1

#populate the first dictionary
for pos in brackets_positions:
    find_bracket(pos)

#populate the second dictionary by reversing the first, finds all closing brackets and their opening brackets
for x,y in matching_pos.items():
    reverse_matching_pos[y] = x

#function the performs the action associated with the command
def interp(pos_cmd):
    global position, memory_tape, instruction_tape, matching_pos, reverse_matching_pos, instruction_tape_counter

    if pos_cmd == ">":#if you skip ahead multiple positions make sure you make the memory
        position += 1
        while True:
            try:
                h = memory_tape[position]
                break
            except:
                memory_tape.append(0)

    if pos_cmd == "<": position -= 1

    if pos_cmd == "+":
        try:
            memory_tape[position] += 1
            if memory_tape[position] > 255: memory_tape[position] = 0
        except:
            memory_tape.append(0)
            memory_tape[position] += 1
            if memory_tape[position] > 255: memory_tape[position] = 0

    if pos_cmd == "-":
        try:
            memory_tape[position] -= 1
            if memory_tape[position] < 0: memory_tape[position] = 255
        except:
            memory_tape.append(0)
            memory_tape[position] -= 1
            if memory_tape[position] < 0: memory_tape[position] = 255
    if pos_cmd == ".":
        print(chr(memory_tape[position]),end="")

    if pos_cmd == ",":
        while True:
            u = input("imput: ")
            if len(u) > 1:
                continue
            elif len(u) == 1:
                break

        memory_tape[position] = ord(u)

    if pos_cmd == "[":
        if memory_tape[position] == 0:
            instruction_tape_counter = matching_pos[instruction_tape_counter]


    if pos_cmd == "]":
        if memory_tape[position] != 0:
            instruction_tape_counter = reverse_matching_pos[instruction_tape_counter]

    else:
        pass
#main loop
while True:


    if instruction_tape_counter > len(instruction_tape)-1: break
    interp(instruction_tape[instruction_tape_counter])
    instruction_tape_counter += 1
