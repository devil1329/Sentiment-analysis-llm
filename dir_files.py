import os
import csv
import reader_writer as rw
import pandas as pd

output_file = "data/shanghai.csv"
fields = ["hotel name", "reviews"]
with open(output_file, 'w', encoding='utf-8') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(fields)

# get the files names 
path_dir = "Hotels_Data/shanghai"
list_of_files = os.listdir(path_dir)

# extract hotel name 
def extract_hotel_name(h_name):
        temp = list(h_name.replace("_"," ").split(" "))
        hotel = ""
        for i in range(2,len(temp)):
                hotel+=temp[i]+" "
        return hotel


# reading the reviews of hotels 
for l in list_of_files:
        hotel_name = extract_hotel_name(l)
        input_file = path_dir + "/" + l
        rw.creating_a_csv(output_file, input_file, hotel_name)


print("end")