""" WRITE A FUNCTION THAT WRITES AND READS ITEMS INTO A FILE"""

def write_read_new_file(file_content, file_name):
    try:
        with open(file_name, 'w') as file:
            file.writelines(file_content)
        
        # open the file again to read from it
        with open(file_name, 'r') as file:
           content = file.read()
        return content
    except Exception as e:
        print(e)
            
            


write_read_new_file("money \n food \n house \n cars", 'new.txt')