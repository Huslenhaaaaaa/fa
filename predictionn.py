import os
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model

class train_model:
    def train(self):
        data = pd.read_csv(r'C:\\Users\\user\\PycharmProjects\\dataset\\train_dataset.csv')
        array = data.values

        for i in range(len(array)):
            if array[i][0] == "Male":
                array[i][0] = 1
            else:
                array[i][0] = 0

        df = pd.DataFrame(array)

        maindf = df[[0, 1, 2, 3, 4, 5, 6]]
        mainarray = maindf.values

        temp = df[7]
        train_y = temp.values

        self.mul_lr = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg', max_iter=1000)
        self.mul_lr.fit(mainarray, train_y)

    def test(self, test_data):
        try:
            test_predict = list()
            for i in test_data:
                test_predict.append(int(i))
            y_pred = self.mul_lr.predict([test_predict])
            return y_pred
        except:
            print("All Factors For Finding Personality Not Entered!")


def check_type(data):
    if type(data) == str or type(data) == str:
        return str(data).title()
    if type(data) == list or type(data) == tuple:
        str_list = ""
        for i, item in enumerate(data):
            str_list += item + ", "
        return str_list
    else:
        return str(data)


def prediction_result(personality_values):
    personality = model.test(personality_values)
    print("\n############# Predicted Personality #############\n")
    print(personality)
    return personality


# model = train_model()
# model.train()
# prediction_result(('1', '23', '7', '4', '7', '3', '2','2'))
