"""WRITE A FUNCTION THAT READS THE TOTAL LINES AND WORD OF A FILE """

def file_details(file_name):
    line_count = 0
    word_count = 0
    try:
        with open(file_name) as file:
            for line in file:
                line_count += 1
                words = line.split()
            for w in  words:
                word_count +=1
    
        return {
            "file_name": file_name,
            "word_count": word_count,
            "line_count": line_count
        }
    except Exception as e:
        print(e)
        
         
         
print(file_details('sample.txt'))