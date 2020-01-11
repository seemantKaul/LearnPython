def computeIntCode(arrCode):
    pointer = 0

    ###Configuration
    # instructionCount = 4
    inputParameter1 = 1
    inputParameter2 = 2
    outputParameter = 3
    ADD = '01'
    MUL = '02'
    SET = '03'
    GET = '04'
    JUMP_TRUE = '05'
    JUMP_FALSE = '06'
    LESS_THAN = '07'
    EQUALS = '08'
    HALT = '99'
    ###

    while int(arrCode[pointer]) != int(HALT):

        # print(pointer)

        instruction = str(arrCode[pointer]).zfill(
            5)  # converting every instruction to 4 digit
        opcode = str(instruction)[3:5]
        parameter_mode_1 = int(str(instruction[2]))
        parameter_mode_2 = int(str(instruction[1]))
        parameter_mode_3 = int(str(instruction[0]))

        para1 = 0  # initialize
        para2 = 0  # initialize
        para3 = 0  # initialize

        print(f"pointer:{pointer}")
        print("instruction:" + str(instruction))
        print("opcode:" + str(opcode))
        # print( type(opcode))
        print("parameter_mode_1:" + str(parameter_mode_1))
        print("parameter_mode_2:" + str(parameter_mode_2))
        # print("parameter_mode_3:" + str(parameter_mode_3))

        '''
        #Implementation of parameter mode
        if parameter_mode_1 == 0:
            #print(f"pointer:{pointer}, inputParameter1:{inputParameter1}")
            para1 = int(arrCode[int(arrCode[pointer + inputParameter1])])
            print(para1)
        elif parameter_mode_1 == 1:
            para1 = int(arrCode[pointer + inputParameter1])
        if parameter_mode_2 == 0:
            #print(f"pointer:{pointer}, inputParameter2:{inputParameter2}")
            para2 = int(arrCode[int(arrCode[pointer + inputParameter2])])
            #print(arrCode[pointer + inputParameter2])
            #print(para2)
        elif parameter_mode_2 == 1:
            para2 = int(arrCode[pointer + inputParameter2])
            #print(f"pointer:{pointer}, inputParameter2:{inputParameter2}")
        '''
        if int(opcode) == int(ADD):

            # print("Adding")
            instructionCount = 4
            inputParameter1 = 1
            inputParameter2 = 2
            outputParameter = 3
            # Implementation of parameter mode
            if parameter_mode_1 == 0:
                # print(f"pointer:{pointer}, inputParameter1:{inputParameter1}")
                para1 = int(arrCode[int(arrCode[pointer + inputParameter1])])
                # print(para1)
            elif parameter_mode_1 == 1:
                para1 = int(arrCode[pointer + inputParameter1])
            if parameter_mode_2 == 0:
                # print(f"pointer:{pointer}, inputParameter2:{inputParameter2}")
                para2 = int(arrCode[int(arrCode[pointer + inputParameter2])])
                # print(arrCode[pointer + inputParameter2])
                # print(para2)
            elif parameter_mode_2 == 1:
                para2 = int(arrCode[pointer + inputParameter2])
                # print(f"pointer:{pointer}, inputParameter2:{inputParameter2}")

            # print(arrCode[int(arrCode[pointer + outputParameter])])
            arrCode[int(
                arrCode[pointer + outputParameter])] = int(para1) + int(para2)
            pointer = pointer + instructionCount
            '''
            print(f"pointer:{pointer}, inputParameter2:{inputParameter2}")
            print(arrCode)
            print(int(arrCode[pointer]) == int(HALT)) 
            print(int(HALT))
            '''
            continue

        elif int(opcode) == int(MUL):
            # print("Multiplying")
            # Implementation of parameter mode
            if parameter_mode_1 == 0:
                # print(f"pointer:{pointer}, inputParameter1:{inputParameter1}")
                para1 = int(arrCode[int(arrCode[pointer + inputParameter1])])
                # print(para1)
            elif parameter_mode_1 == 1:
                para1 = int(arrCode[pointer + inputParameter1])
            if parameter_mode_2 == 0:
                # print(f"pointer:{pointer}, inputParameter2:{inputParameter2}")
                para2 = int(arrCode[int(arrCode[pointer + inputParameter2])])
                # print(arrCode[pointer + inputParameter2])
                # print(para2)
            elif parameter_mode_2 == 1:
                para2 = int(arrCode[pointer + inputParameter2])
                # print(f"pointer:{pointer}, inputParameter2:{inputParameter2}")
            instructionCount = 4
            inputParameter1 = 1
            inputParameter2 = 2
            outputParameter = 3
            arrCode[int(
                arrCode[pointer + outputParameter])] = int(para1) * int(para2)
            pointer = pointer + instructionCount
            continue

        elif int(opcode) == int(SET):
            # print("Setting")
            # Implementation of parameter mode
            if parameter_mode_1 == 0:
                # print(f"pointer:{pointer}, inputParameter1:{inputParameter1}")
                para1 = int(arrCode[int(arrCode[pointer + inputParameter1])])
                # print(para1)
            elif parameter_mode_1 == 1:
                para1 = int(arrCode[pointer + inputParameter1])
            instructionCount = 2
            outputParameter = 1
            getValue = input("GET VALUE")
            arrCode[int(arrCode[pointer + outputParameter])] = getValue
            pointer = pointer + instructionCount
            continue


        elif int(opcode) == int(GET):
            # print("Getting")
            # Implementation of parameter mode
            if parameter_mode_1 == 0:
                # print(f"pointer:{pointer}, inputParameter1:{inputParameter1}")
                para1 = int(arrCode[int(arrCode[pointer + inputParameter1])])
                # print(para1)
            elif parameter_mode_1 == 1:
                para1 = int(arrCode[pointer + inputParameter1])

            instructionCount = 2
            inputParameter1 = 1
            print("OUT:" + str(para1))
            pointer = pointer + instructionCount
            continue


        elif int(opcode) == int(JUMP_TRUE):
            instructionCount = 3
            inputParameter1 = 1
            inputParameter2 = 2

            # Implementation of parameter mode
            if parameter_mode_1 == 0:
                # print(f"pointer:{pointer}, inputParameter1:{inputParameter1}")
                para1 = int(arrCode[int(arrCode[pointer + inputParameter1])])
                # print(para1)
            elif parameter_mode_1 == 1:
                para1 = int(arrCode[pointer + inputParameter1])
            if parameter_mode_2 == 0:
                #   print(f"pointer:{pointer}, inputParameter2:{inputParameter2}")
                para2 = int(arrCode[int(arrCode[pointer + inputParameter2])])
                # print(arrCode[pointer + inputParameter2])
                # print(para2)
            elif parameter_mode_2 == 1:
                para2 = int(arrCode[pointer + inputParameter2])
            # print(f"pointer:{pointer}, inputParameter2:{inputParameter2}")

            # print(arrCode[int(arrCode[pointer + outputParameter])])
            if int(para1) == 0:
                pointer = pointer + instructionCount
            else:
                print(f"jumping to {para2}")
                pointer = para2
            print(f"pointer:{pointer}, inputParameter2:{inputParameter2}")
            input("See")
            continue


        elif int(opcode) == int(JUMP_FALSE):
            instructionCount = 3
            inputParameter1 = 1
            inputParameter2 = 2

            # Implementation of parameter mode
            if parameter_mode_1 == 0:
                # print(f"pointer:{pointer}, inputParameter1:{inputParameter1}")
                para1 = int(arrCode[int(arrCode[pointer + inputParameter1])])
                # print(para1)
            elif parameter_mode_1 == 1:
                para1 = int(arrCode[pointer + inputParameter1])
            if parameter_mode_2 == 0:
                # print(f"pointer:{pointer}, inputParameter2:{inputParameter2}")
                para2 = int(arrCode[int(arrCode[pointer + inputParameter2])])
                # print(arrCode[pointer + inputParameter2])
                # print(para2)
            elif parameter_mode_2 == 1:
                para2 = int(arrCode[pointer + inputParameter2])
            # print(f"pointer:{pointer}, inputParameter2:{inputParameter2}")

            # print(arrCode[int(arrCode[pointer + outputParameter])])
            if int(para1) == 0:
                print(f"jumping to {para2}")
                pointer = para2
                # print(f"pointer:{pointer}, inputParameter2:{inputParameter2}")

            else:
                pointer = pointer + instructionCount
            input("See")
            continue

        elif int(opcode) == int(LESS_THAN):
            instructionCount = 4
            inputParameter1 = 1
            inputParameter2 = 2
            inputParameter3 = 3

            # Implementation of parameter mode
            if parameter_mode_1 == 0:
                # print(f"pointer:{pointer}, inputParameter1:{inputParameter1}")
                para1 = int(arrCode[int(arrCode[pointer + inputParameter1])])
                # print(para1)
            elif parameter_mode_1 == 1:
                para1 = int(arrCode[pointer + inputParameter1])
            if parameter_mode_2 == 0:
                # print(f"pointer:{pointer}, inputParameter2:{inputParameter2}")
                para2 = int(arrCode[int(arrCode[pointer + inputParameter2])])
                # print(arrCode[pointer + inputParameter2])
                # print(para2)
            elif parameter_mode_2 == 1:
                para2 = int(arrCode[pointer + inputParameter2])

            para3 = int(arrCode[pointer + inputParameter3])
            # print(f"para1: {para1}, para2:{para2}, para3:{para3}, inputParameter3:{inputParameter3}" )
            if int(para1) < int(para2):
                # print(f"jumping to {para2}")
                arrCode[para3] = 1
            else:
                arrCode[para3] = 0
                # print(f"pointer:{pointer}, inputParameter2:{inputParameter2}")
            pointer = pointer + instructionCount
            continue


        elif int(opcode) == int(EQUALS):
            instructionCount = 4
            inputParameter1 = 1
            inputParameter2 = 2
            inputParameter3 = 3

            # Implementation of parameter mode
            if parameter_mode_1 == 0:
                # print("using position mode for para1")
                # print(f"pointer:{pointer}, inputParameter1:{inputParameter1}")
                para1 = int(arrCode[int(arrCode[pointer + inputParameter1])])
                # print(para1)
            elif parameter_mode_1 == 1:

                # print("using value mode for para1")
                para1 = int(arrCode[pointer + inputParameter1])
            if parameter_mode_2 == 0:
                # print("using position mode for para2")
                # print(f"pointer:{pointer}, inputParameter2:{inputParameter2}")
                para2 = int(arrCode[int(arrCode[pointer + inputParameter2])])
                # print(arrCode[pointer + inputParameter2])
                # print(para2)
            elif parameter_mode_2 == 1:
                # print("using value mode for para2")
                para2 = int(arrCode[pointer + inputParameter2])

            para3 = int(arrCode[pointer + inputParameter3])

            # print(f"para1: {para1}, para2:{para2}, para3:{para3}, inputParameter3:{inputParameter3}" )

            if int(para1) == int(para2):
                arrCode[para3] = 1
            else:
                arrCode[para3] = 0
                # print(f"pointer:{pointer}, inputParameter2:{inputParameter2}")
            pointer = pointer + instructionCount
            continue
        else:  # Opcode not found
            print(f"ERROR: Incorrect OpCode {opcode}")

    return (arrCode)


def computeFuel(arrModules):
    pass


if __name__ == "__main__":
    inputCode = "3,225,1,225,6,6,1100,1,238,225,104,0,1102,35,92,225,1101,25,55,225,1102,47,36,225,1102,17,35,225,1,165,18,224,1001,224,-106,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,1101,68,23,224,101,-91,224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,2,217,13,224,1001,224,-1890,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,1102,69,77,224,1001,224,-5313,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,102,50,22,224,101,-1800,224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,1102,89,32,225,1001,26,60,224,1001,224,-95,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1102,51,79,225,1102,65,30,225,1002,170,86,224,101,-2580,224,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,101,39,139,224,1001,224,-128,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1102,54,93,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,677,224,1002,223,2,223,1005,224,329,101,1,223,223,7,677,677,224,102,2,223,223,1006,224,344,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,359,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,374,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,389,1001,223,1,223,107,226,677,224,102,2,223,223,1005,224,404,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,419,101,1,223,223,107,226,226,224,102,2,223,223,1005,224,434,1001,223,1,223,108,677,226,224,1002,223,2,223,1006,224,449,101,1,223,223,108,226,226,224,102,2,223,223,1006,224,464,1001,223,1,223,1007,226,226,224,1002,223,2,223,1005,224,479,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,494,101,1,223,223,1007,226,677,224,102,2,223,223,1006,224,509,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,524,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,539,101,1,223,223,1008,677,226,224,1002,223,2,223,1005,224,554,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,569,1001,223,1,223,1108,226,226,224,102,2,223,223,1005,224,584,101,1,223,223,1107,226,677,224,1002,223,2,223,1005,224,599,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,629,1001,223,1,223,8,226,226,224,1002,223,2,223,1005,224,644,1001,223,1,223,1107,677,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,1007,677,677,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226"

    # inputCode = "106,0,4,67,5,99"
    arrCode = inputCode.split(',')
    print(arrCode)
    arrCode = computeIntCode(arrCode)
    # print("Output=" + str(arrCode))

    # inputModule = input("Enter Modules")
