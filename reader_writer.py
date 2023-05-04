import re 
import csv

# this is to clear reviews 
def clear_text(text):
        pat = '(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{1,2}\s+\d{4}'
        text = re.sub(pat,'', text)
        text = re.sub('\s+',' ',text)
        text = text[1:]
        return text

def creating_a_csv(output_file, input_file, hotel_name):
        # contain reviews and hotel name 
        rows = []
        
        # reading the file and appending reviews into a list 
        f = open(input_file, 'r')
        Lines = f.readlines()
        f.close()

        for line in Lines:
                text = clear_text(line)
                l = [hotel_name, text]
                rows.append(l)

        # writing into csv file 
        with open(output_file, 'a', encoding='utf-8') as csvfile: 
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(rows)
        