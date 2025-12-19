with open('sample.txt', 'r+') as file:
    
    file.write("how things without trusting in God")
    file.seek(0) 
    content = file.readlines()

print(content)