import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_train = pd.read_csv("titanic.csv")

sample3=data_train.sample(100)
print(sample3)
sns.barplot(x="Embarked", y="Survived", hue="Sex", data=data_train)
#sns.pointplot(x="Pclass", y="Survived", hue="Sex", data=data_train,palette={"male": "blue", "female": "pink"},markers=["*", "o"], linestyles=["-", "--"])
plt.show()
