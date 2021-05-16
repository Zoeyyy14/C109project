import csv
import random
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("StudentsPerformance.csv")
reading_score=df["reading score"].tolist()
reading_score_list_mean=statistics.mean(reading_score)
reading_score_list_median=statistics.median(reading_score)
reading_score_list_mode=statistics.mode(reading_score)
reading_score_list_sd=statistics.stdev(reading_score)
print("Mean, Median, Mode And Standared deviation of reading_score is {}, {}, {} and {}respectively".format(reading_score_list_mean, reading_score_list_median, reading_score_list_mode, reading_score_list_sd))

reading_score_first_sd_start, reading_score_first_sd_end=reading_score_list_mean-reading_score_list_sd, reading_score_list_mean+reading_score_list_sd
reading_score_second_sd_start, reading_score_second_sd_end=reading_score_list_mean-(2*reading_score_list_sd), reading_score_list_mean+(2*reading_score_list_sd)
reading_score_third_sd_start, reading_score_third_sd_end=reading_score_list_mean-(3*reading_score_list_sd), reading_score_list_mean+(3*reading_score_list_sd)

reading_score_list_of_data_within_1_sd=[result for result in reading_score if result>reading_score_first_sd_start and result<reading_score_first_sd_end]
reading_score_list_of_data_within_2_sd=[result for result in reading_score if result>reading_score_second_sd_start and result<reading_score_second_sd_end]
reading_score_list_of_data_within_3_sd=[result for result in reading_score if result>reading_score_third_sd_start and result<reading_score_third_sd_end]

print("{}% of data for reading_score lies within 1 standared deviation".format(len(reading_score_list_of_data_within_1_sd)*100.0/len(reading_score)))
print("{}% of data for reading_score lies within 2 standared deviation".format(len(reading_score_list_of_data_within_2_sd)*100.0/len(reading_score)))
print("{}% of data for reading_score lies within 3 standared deviation".format(len(reading_score_list_of_data_within_3_sd)*100.0/len(reading_score)))

fig=ff.create_distplot([reading_score],["reading score"], show_hist=True)
fig.add_trace(go.Scatter(x=[reading_score_list_mean,reading_score_list_mean],y=[0,0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[reading_score_first_sd_start,reading_score_first_sd_start],y=[0,0.17], mode="lines", name="STANDERED DEVIATION ONE"))
fig.add_trace(go.Scatter(x=[reading_score_first_sd_end,reading_score_first_sd_end],y=[0,0.17], mode="lines", name="STANDERED DEVIATION ONE"))
fig.add_trace(go.Scatter(x=[reading_score_second_sd_start,reading_score_second_sd_start],y=[0,0.17], mode="lines", name="STANDERED DEVIATION TWO"))
fig.add_trace(go.Scatter(x=[reading_score_third_sd_end,reading_score_third_sd_end],y=[0,0.17], mode="lines", name="STANDERED DEVIATION TWO"))
fig.show()