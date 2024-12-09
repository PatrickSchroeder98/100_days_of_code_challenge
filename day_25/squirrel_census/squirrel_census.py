import pandas as pnd

data = pnd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241201.csv')

grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
      "Fur Color": ["Gray", "Cinnamon", "Black"],
      "Count": [grey_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

df = pnd.DataFrame(data_dict)
df.to_csv("squirrels_count.csv")
