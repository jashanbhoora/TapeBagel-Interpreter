import os
import argparse

def interpret(input):
    code = input.split(" ")

    state = [0,0,0]
    idx = 0

    output = ""
    
    for instructionIndex, instruction in enumerate(code):
        if len(instruction) > 0:
            print "Instruction " + str(instructionIndex) + ": " + str(instruction)

            ##commands
            if(instruction == "%#"):
                idx += 1
                print "    idx = " + str(idx)

            elif(instruction == "%%"):
                idx = 0
                print "    idx = " + str(idx)

            elif(instruction == "%&"):
                raise NotImplementedException("%&")

            elif(instruction == "#%"):
                state = [1,1,1]
                print "    state = " + str(state)

            elif(instruction == "##"):
                state = [0,0,0]
                print "    state = " + str(state)

            elif(instruction == "&&"):
                raise NotImplementedException("&&")

            elif(instruction == "&@"):
                os.system('cls' if os.name == 'nt' else 'clear')

            elif(instruction == "%++"):
                state[idx] += 1
                print "    state = " + str(state)



            ##operations
            elif("&" in instruction):
                leftOperand, rightOperand = instruction.split("&")
                state[idx] = state[len(leftOperand)-1] * state[len(rightOperand)-1]
                print "    state = " + str(state)

            elif("+" in instruction):
                leftOperand, rightOperand = instruction.split("+")
                state[idx] = state[len(leftOperand)-1] + state[len(rightOperand)-1]
                print "    state = " + str(state)

            elif("$" in instruction):
                leftOperand, rightOperand = instruction.split("$")
                state[idx] = state[len(leftOperand)-1] / state[len(rightOperand)-1]
                print "    state = " + str(state)

            elif("-" in instruction):
                leftOperand, rightOperand = instruction.split("-")
                state[idx] = state[len(leftOperand)-1] - state[len(rightOperand)-1]
                print "    state = " + str(state)

            elif("@" in instruction):
                c = instruction.count("@")
                if c == 1:
                    _, rightOperand = instruction.split("@")
                    char = state[len(rightOperand)-1]
                    o = chr(64 + char if char > 0 else char)
                    print "    output += " + o
                    output += o

                elif c == 2:
                    _,_, rightOperand = instruction.split("@")
                    o = str(state[len(rightOperand)-1])
                    print "    output += " + o
                    output += o

                else:
                    raise Exception("Unknown @ operation " + str(instruction))

            else:
                raise Exception("Unknown operation " + str(instruction))

            print ""

    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="An extremely simple interpreter for TapeBagel. (https://github.com/jashanbhoora/TapeBagel-Interpreter)")
    parser.add_argument("tbFile", type=str, help="Path to the file to interpret")
    args = parser.parse_args()
    with open(args.tbFile, 'r') as file:
        print "output: " + interpret(file.read())
