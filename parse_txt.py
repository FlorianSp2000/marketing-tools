with open('texting.txt', encoding='UTF-8') as file:
    lines = [line.rstrip() for line in file]
    new_file = open('test.txt', "w+", encoding='UTF-8')
    for line in lines:
        new_file.write(line+"\n")
    # print(lines[0])
    new_file.close()
file.close()