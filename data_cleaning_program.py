import pandas as pd

list_words = []

with open("data/toefl_must_known_words.txt", mode='r') as file:
    for line in file.readlines():
        if "@" in line:
            tmp = line[:-2].split("@")
            list_words.append({"Word": tmp[0].strip(), "Explanation": tmp[1]})

dataset = pd.DataFrame(list_words, columns=["Word", "Explanation"])
dataset.to_csv("data/toefl_must_known_words.csv", index=False)
