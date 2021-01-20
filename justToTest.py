import logging
import csv

dic = {"Lama":12 , "dana": 13}
logging.basicConfig(level=logging.DEBUG, filename='sample.log')

for item in dic:
    string = "Command: "+ str(item) + "\nOutput: "+ str(dic[item])
    logging.info(string)



with open('sample.log') as file:
    lines = file.read().splitlines()
    lines = [lines[x:x+2] for x in range(0, len(lines), 2)]

    with open('yourcsv.csv', 'w+') as csvfile:
        w = csv.writer(csvfile)
        w.writerows(lines)
# logging.basicConfig(level=logging.DEBUG, filename='hi.log')
#
# for item in dic:
#     string = "Command: "+ str(item) + "\n          Output: "+ str(dic[item])
#     logging.info(string)

#
# a_file = open("sample.csv", "w")
# a_dict = {"a": 1, "b": 2}
#
# writer = csv.writer(a_file)
# for key, value in a_dict.items():
#     writer.writerow([key, value])
#
# a_file.close()