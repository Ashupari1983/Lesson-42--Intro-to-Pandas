import pandas as pd
import numpy as np

exam_data = {"Name":["Belle", "Anne", "Arora", "Michael", "Kris"],
             "Score":[9, np.nan, 9.5, 10, np.nan],
             "Attempts":[1, 1, 2, 2, 1],
             "Grade":[10, 10, 10, 10, 10],
             "Qualify":["yes","yes","yes","yes","yes"]}

labels = ["a", "b", "c", "d", "e"]

df = pd.DataFrame(exam_data, index = labels)
print(df.head())
print(df.info())
