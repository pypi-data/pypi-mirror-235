def p1():
    a = """
    import pandas as pd
    from sklearn.preprocessing import LabelEncoder
    from sklearn.preprocessing import MinMaxScaler
    diamond_data = pd.read_csv("C:\\MS214419\\diamonds.csv")
    print("\n Before Preprocessing")
    print("-----------------------")
    print(diamond_data.head(50))
    diamond_data['price'] = diamond_data['price'].fillna(diamond_data['price'].mean())
    l = LabelEncoder()
    diamond_data['cut'] = l.fit_transform(diamond_data['cut'])
    n = MinMaxScaler(feature_range=(0, 1))
    diamond_data['depth'] = n.fit_transform(diamond_data[['depth']])
    print("\n After preprocessing data")
    print("---------------------------")
    print("\n 1. Replacing null values in the price column with the mean")
    print("\n 2. Changing categorical data in the Cut column to numerical data")
    print("\n 3. Normalizing the Depth column to fit in the range [0, 1]\n\n")
    print(diamond_data.head(50))
    print("--------------------------")
    """
    print(a)


def p2():
    b = """
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    sd = pd.read_csv("C:\\MS214419\\Salary_Data.csv")
    x = sd[['Years']]
    y = sd['Salary']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    print(df.to_string())
    """
    print(b)


def p3():
    c = """
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    import warnings
    warnings.filterwarnings("ignore")
    sd = pd.read_csv("C:\\MS214419\\Startups.csv")
    features = sd[['R&DSpend', 'Administration', 'MarketingSpend']]
    x = features
    y = sd['Profit']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    print(df)
    print("For new test data")
    rd = float(input("Enter the value for R&D "))
    ad = float(input("Enter the value for Administration: "))
    m = float(input("Enter the value for marketing: "))
    test_data = [[rd, ad, m]]
    pred = model.predict(test_data)
    print("Profit predicted for the test data: ", pred)
    """
    print(c)


def p4():
    d = """
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import PolynomialFeatures
    measles_data = pd.read_csv("C:\\MS214419\\MeaslesVaccine.csv")
    x = measles_data[['Year']]
    y = measles_data['Rate']
    polyregs = PolynomialFeatures(degree=3)
    xpoly = polyregs.fit_transform(x)
    model = LinearRegression()
    model.fit(xpoly, y)
    plt.scatter(x, y, color='blue')
    plt.plot(x, model.predict(xpoly), color='purple')
    plt.xlabel('Year')
    plt.ylabel('Vaccination Rate')
    plt.show()
    print("Predicted Vaccination rate for any year")
    years = int(input("Enter the Year: "))
    pred = model.predict(polyregs.fit_transform([[years]])
    print("The predicted vaccination rate for the year", years, "is:", pred)
    """
    print(d)


def p5():
    e = """
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn import metrics
    import warnings
    warnings.filterwarnings("ignore")
    diabetes_data = pd.read_csv("C:\\MS214419\\diabetes.csv")
    features_cols = diabetes_data[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI',' Age']]
    x = features_cols
    y = diabetes_data['Outcome']
    print("Logistic Regression")
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    model = LogisticRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    df = pd.DataFrame({'Actual value': y_test, 'Predicted ': y_pred})
    print(df.to_string())
    cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
    accuracy = metrics.accuracy_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)
    recall = metrics.recall_score(y_test, y_pred)
    print("Confusion Matrix: -")
    print(cnf_matrix)
    print("Accuracy: ", accuracy)
    print("Precision: ", precision)
    print("Recall : ", recall)
    print("For new test data")
    p = float(input("Enter the value for Pregnancies: "))
    g = float(input("Enter the value for Glucose: "))
    bp = float(input("Enter the value for BloodPressure: "))
    st = float(input("Enter the value for SkinThickness: "))
    i = float(input("Enter the value for Insulin: "))
    bmi = float(input("Enter the value for BMI: "))
    age = float(input("Enter the value for Age: "))
    test_data = [[p, g, bp, st, i, bmi, age]]
    pred = model.predict(test_data)
    if pred == 1:
        print("The person is diabetic")
    else:
        print("The person is not diabetic")
    """
    print(e)


def p6():
    f = """
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import GaussianNB
    from sklearn import metrics
    diabetes_data = pd.read_csv("C:\\MS214419\\diabetes.csv")
    Featurecol = diabetes_data[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','Age ']]
    x = Featurecol
    y = diabetes_data['Outcome']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    model = GaussianNB()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    print(df.to_string())
    cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
    accuracy = metrics.accuracy_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)
    recall = metrics.recall_score(y_test, y_pred)
    print("Confusion Matrix")
    print(cnf_matrix)
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    """
    print(f)


def p7():
    g = """
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn import metrics
    diabetes_data = pd.read_csv("C:\\MS214419\\diabetes.csv")
    features_cols = diabetes_data[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI',' Age']]
    x = features_cols
    y = diabetes_data['Outcome']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    model = DecisionTreeClassifier()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    df = pd.DataFrame({'Actual value': y_test, 'Predicted ': y_pred})
    print(df.to_string())
    cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
    accuracy = metrics.accuracy_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)
    recall = metrics.recall_score(y_test, y_pred)
    print("Confusion Matrix: -")
    print(cnf_matrix)
    print("Accuracy: ", accuracy)
    print("Precision: ", precision)
    print("Recall : ", recall)
    """
    print(g)


def p8():
    h = """
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn import metrics
    diabetes_data = pd.read_csv("C:\\MS214419\\diabetes.csv")
    features_cols = diabetes_data[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI',' Age']]
    x = features_cols
    y = diabetes_data['Outcome']
    print("K Nearest Neighbors Classification")
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    df = pd.DataFrame({'Actual value': y_test, 'Predicted ': y_pred})
    print(df.to_string())
    cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
    accuracy = metrics.accuracy_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)
    recall = metrics.recall_score(y_test, y_pred)
    print("Confusion Matrix: -")
    print(cnf_matrix)
    print("Accuracy: ", accuracy)
    print("Precision: ", precision)
    print("Recall : ", recall)
    """
    print(h)


def p9():
    i = """
    import pandas as pd
    from sklearn.cluster import KMeans
    import matplotlib.pyplot as plt
    iris = pd.read_csv("C:\\MS214419\\iris.csv")
    x = iris[['PetalLengthCm','PetalWidthCm']]
    y = iris['Species']
    model = KMeans(n_clusters=3)
    y_pred = model.fit_predict(x)
    df = pd.DataFrame({'Petal Length in Cm': x['PetalLengthCm'], 'Petal Width in Cm': x['PetalWidthCm'], 'Actual ': y, 'Predicted ': y_pred})
    print(df.to_string())
    plt.scatter(x['PetalLengthCm'], x['PetalWidthCm'], c=y_pred, cmap="rainbow")
    plt.xlabel("Petal Length in Cm")
    plt.ylabel("Petal Width in Cm")
    plt.show()
    """
    print(i)


def p10():
    j = """
    import pandas as pd
    from sklearn.cluster import AgglomerativeClustering
    from scipy.cluster.hierarchy import dendrogram, linkage
    from scipy.spatial.distance import pdist
    import matplotlib.pyplot as plt
    iris = pd.read_csv("C:\\MS214419\\Iris.csv")
    x = iris[['PetalLengthCm','PetalWidthCm']]
    y = iris['Species']
    model = AgglomerativeClustering(n_clusters=3)
    y_pred = model.fit_predict(x)
    df = pd.DataFrame({'Petal Length in Cm': x['PetalLengthCm'], 'Petal Width in Cm': x['PetalWidthCm'], 'Actual ': y, 'Predicted ': y_pred})
    print(df.to_string())
    clusters = linkage(pdist(x, metric='euclidean'), method='complete')
    dend = dendrogram(clusters)
    plt.xlabel("Data Points")
    plt.ylabel("Euclidean Distance")
    plt.show()
    """
    print(j)


def p11():
    k = """
    import pandas as pd
    from sklearn.cluster import DBSCAN
    import matplotlib.pyplot as plt
    iris = pd.read_csv("C:\\MS214419\\iris.csv")
    x = iris[['PetalLengthCm','PetalWidthCm']]
    y = iris['Species']
    model = DBSCAN(eps=0.3, metric="euclidean")
    y_pred = model.fit_predict(x)
    df = pd.DataFrame({'Petal Length in Cm': x['PetalLengthCm'], 'Petal Width in Cm': x['PetalWidthCm'], 'Actual ': y, 'Predicted ': y_pred})
    print(df.to_string())
    plt.scatter(x['PetalLengthCm'], x['PetalWidthCm'], c=y_pred, cmap="rainbow")
    plt.xlabel("Petal Length in Cm")
    plt.ylabel("Petal Width in Cm")
    plt.show()
    """
    print(k)


def p12():
    l = """
    # Empty function
    """
    print(l)
