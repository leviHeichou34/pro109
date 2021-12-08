import csv
from os import stat 
import pandas as pd
import statistics 

df = pd.read_csv("data.csv")
mathScore_list = df["math score"].to_list()
readingScore_list = df["reading score"].to_list()

mathScore_mean = statistics.mean(mathScore_list)
readingScore_mean = statistics.mean(readingScore_list)


mathScore_median = statistics.median(mathScore_list)
readingScore_median = statistics.median(readingScore_list)


mathScore_mode = statistics.mode(mathScore_list)
readingScore_mode = statistics.mode(readingScore_list)

print("mean, median and mode of mathScore is {}, {}, {} respectively".format(mathScore_mean, mathScore_median, mathScore_mode))
print("mean, median and mode of readingScore is {}, {}, {} respectively".format(readingScore_mean, readingScore_median, readingScore_mode))

mathScore_stdev = statistics.stdev(mathScore_list)
readingScore_stdev = statistics.stdev(readingScore_list)

mathScore_first_stdev_start, mathScore_first_stdev_end = mathScore_mean-mathScore_stdev, mathScore_mean+mathScore_stdev
mathScore_second_stdev_start, mathScore_second_stdev_end = mathScore_mean-(2*mathScore_stdev), mathScore_mean+(2*mathScore_stdev)
mathScore_third_stdev_start, mathScore_third_stdev_end = mathScore_mean-(3*mathScore_stdev), mathScore_mean+(3*mathScore_stdev)


readingScore_first_stdev_start, readingScore_first_stdev_end = readingScore_mean-readingScore_stdev, readingScore_mean+readingScore_stdev
readingScore_second_stdev_start, readingScore_second_stdev_end = readingScore_mean-(2*readingScore_stdev), readingScore_mean+(2*readingScore_stdev)
readingScore_third_stdev_start, readingScore_third_stdev_end = readingScore_mean-(3*readingScore_stdev), readingScore_mean+(3*readingScore_stdev)

mathScore_list_of_data_within_1_stdev= [result for result in mathScore_list if result > mathScore_first_stdev_start and result < mathScore_first_stdev_end ]
mathScore_list_of_data_within_2_stdev= [result for result in mathScore_list if result > mathScore_second_stdev_start and result < mathScore_second_stdev_end ]
mathScore_list_of_data_within_3_stdev= [result for result in mathScore_list if result > mathScore_third_stdev_start and result < mathScore_third_stdev_end ]

readingScore_list_of_data_within_1_stdev= [result for result in readingScore_list if result > readingScore_first_stdev_start and result < readingScore_first_stdev_end ]
readingScore_list_of_data_within_2_stdev= [result for result in readingScore_list if result > readingScore_second_stdev_start and result < readingScore_second_stdev_end ]
readingScore_list_of_data_within_3_stdev= [result for result in readingScore_list if result > readingScore_third_stdev_start and result < readingScore_third_stdev_end ]

print("{}% of data for mathScore lies within 1 stdev".format(len(mathScore_list_of_data_within_1_stdev)*100.0/ len(mathScore_list)))
print("{}% of data for mathScore lies within 2 stdev".format(len(mathScore_list_of_data_within_2_stdev)*100.0/ len(mathScore_list)))
print("{}% of data for mathScore lies within 3 stdev".format(len(mathScore_list_of_data_within_3_stdev)*100.0/ len(mathScore_list)))

print("{}% of data for readingScore lies within 1 stdev".format(len(readingScore_list_of_data_within_1_stdev)*100.0/ len(readingScore_list)))
print("{}% of data for readingScore lies within 2 stdev".format(len(readingScore_list_of_data_within_2_stdev)*100.0/ len(readingScore_list)))
print("{}% of data for readingScore lies within 3 stdev".format(len(readingScore_list_of_data_within_3_stdev)*100.0/ len(readingScore_list)))