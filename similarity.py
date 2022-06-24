import numpy as np
def getsimilarity(dictl, dict2) :
    all_words_list= []
    for  key in dictl:
        all_words_list.append(key)
    for key in dict2:
           all_words_list.append(key)
    all_words_list_size = len(all_words_list)

    v1 = np.zeros(all_words_list_size, dtype=np.int)
    v2 = np.zeros(all_words_list_size, dtype=np.int)
    i = 0
    for (key) in all_words_list:
        v1[i] = dictl.get(key, 0)
        v2[i] = dict2.get(key, 0)
        i = i+1
    return cos_sim(v1, v2)



def cos_sim(a, b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a  * norm_b)

X=[]
y=[]
lis0=['average', 'middle', 'low']
lis1=['science', 'commerce', 'humanities']
lis2=['building', 'technology', 'healthcare', 'volunteering', 'coding', 'business', 'management', 'law', 'arts']

lis14=['Engineering', 'Medical', 'CA_and_IT', 'Enterpricing_and_management', 'Law', 'Entertainment']

def traing(yy):
    training_data = np.loadtxt(r"C:\Users\HP\Downloads\career_prediction\career_prediction\train.txt", dtype=str, delimiter=" ")
    X = []
    y = []
    for record in training_data:

        if record[0] != '':
            if lis14.index(record[14]) != yy :
                lis={}
                lis["0"] = lis0.index(record[0])
                lis["1"] = lis1.index(record[1])
                lis["2"] = lis2.index(record[2])
                lis["3"] = int(record[3])
                lis["4"] = int(record[4])
                lis["5"] = int(record[5])
                lis["6"] = int(record[6])
                lis["7"] = int(record[7])
                lis["8"] = int(record[8])
                lis["9"] = int(record[9])
                lis["10"] = int(record[10])
                lis["11"] = int(record[11])
                lis["12"] =int(record[12])
                lis["13"] = int(record[13])

                X.append(lis)
                y.append(lis14.index(record[14]))
    return X,y

def similaritycheck(out,d1):
    X,y=traing(out)
    print(X,y)
    outlist = []
    simlist = []
    for i in range(0,len(y)):
        sim = getsimilarity(X[i],d1)
        print(sim,y[i])
        if y[i] in outlist :
            ind = outlist.index(y[i])
            if sim > simlist[ind] :
                simlist[ind] = sim
        else :
            outlist.append(y[i])
            simlist.append(sim)
    return outlist,simlist

