
import numpy as np




from collections import Counter


X=[]
y=[]
lis0=['average', 'middle', 'low']
lis1=['science', 'commerce', 'humanities']
lis2=['building', 'technology', 'healthcare', 'volunteering', 'coding', 'business', 'management', 'law', 'arts']

lis14=['Engineering', 'Medical', 'CA_and_IT', 'Enterpricing_and_management', 'Law', 'Entertainment']

def traing():
    training_data = np.loadtxt(r"C:\Users\HP\Downloads\career_prediction\career_prediction\train.txt", dtype=str, delimiter=" ")
    for record in training_data:

        if record[0] != '':
            lis=[]
            lis.append(lis0.index(record[0]))
            lis.append(lis1.index(record[1]))
            lis.append(lis2.index(record[2]))
            lis.append(int(record[3]))
            lis.append(int(record[4]))
            lis.append(int(record[5]))
            lis.append(int(record[6]))
            lis.append(int(record[7]))
            lis.append(int(record[8]))
            lis.append(int(record[9]))
            lis.append(int(record[10]))
            lis.append(int(record[11]))
            lis.append(int(record[12]))
            lis.append(int(record[13]))

            X.append(lis)
            y.append(lis14.index(record[14]))
traing()

# print(lis0)
# print(lis1)
# print(lis2)
# print(lis14)

print(X[0],y[0])


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred  =  classifier.predict(X_test)

print(y_pred)

from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(y_test, y_pred)
ac = accuracy_score(y_test,y_pred)

print(ac)
print(cm)

def predict_fun(features):
    f = sc.transform(features)
    res = classifier.predict(f)
    return res[0]