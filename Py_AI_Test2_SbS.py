# make predictions
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)
# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
y = array[:,4]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)
# Make predictions on validation dataset
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)
# Evaluate predictions
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

exit(0)

'''
///*-==================================================================================================-*
/// Dateiname             : Py_AI_Test2_SbS.py (Artificial Intelligence by Python Step by Step)
/// Version               : 1.0.0.0
/// Beginn                : 2023-11-11 (1402/08/20)
/// Letzte Aktualisierung : 2023-11-11 (1402/08/20)
/// Autor                 : Ingenieur Behdad Pourtavakoli
/// Warenzeichen          : Behdad Software Developers Group™
/// ----------------------------------------------------------------------------------------------------
/// Copyright© 1380-1402,2001-2023 von B.S.D Group™
/// Alle Rechte vorbehalten.
/// ----------------------------------------------------------------------------------------------------
///
/// Beschreibung: Überprüfen und lernen Sie die Python-Programmierung auf den Websites 
///               https://machinelearningmastery.com/machine-learning-in-python-step-by-step, 
///               
///               
///               
///-===================================================================================================-*///
'''

# 2.1 Import libraries
import os
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#region Konstanten, Variablen und Deklarationen
'''
///*********************************************************************************************************
///* Konstanten, Variablen und Deklarationen                                                               *
///*********************************************************************************************************
'''
# 2.2 Load Dataset
dataset = []
X_train = 0
X_validation = 0
Y_train = 0
Y_validation = 0

#endregion

#region Handschriftliche Funktionen und Prozeduren
'''
/// *********************************************************************************************************
/// * Handschriftliche Funktionen und Prozeduren                                                            *
/// *********************************************************************************************************
'''

'''
/// step1() funktion zum Überprüfen der Versionen von Bibliotheken
/// + 1. Downloading, Installing and Starting Python SciPy
/// - 1.1 Install SciPy Libraries
/// - 1.2 Start Python and Check Versions
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/20
'''
def step1():
    print("Step1: ...")

    # Check the versions of libraries
    print("First Check Versions of libraries:\n")

    # Python version
    import sys
    print("Python: \t{}".format(sys.version))

    # scipy
    import scipy
    print("scipy: \t\t{}".format(scipy.__version__))

    # numpy
    import numpy
    print("numpy: \t\t{}".format(numpy.__version__))

    # matplotlib
    import matplotlib
    print("matplotlib: \t{}".format(matplotlib.__version__))

    # pandas
    import pandas
    print("pandas: \t{}".format(pandas.__version__))

    # scikit-learn
    import sklearn
    print("sklearn: \t{}".format(sklearn.__version__))

'''
/// step2() funktion zum 
/// + 2. Load The Data
/// - 2.2 Load Dataset
/// + 3. Summarize the Dataset
/// - 3.1 Dimensions of Dataset
/// - 3.2 Peek at the Data
/// - 3.3 Statistical Summary
/// - 3.4 Class Distribution
/// - 3.5 Complete Example
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/20
'''
def step2():
    print("\nStep2: ...")

    print("\nLoad data: ...")
    global dataset
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
    dnames = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]
    dataset = read_csv(url, names=dnames)

    # shape
    print("Dimensions of Dataset", dataset.shape)

    # head
    print("Peek at the Data: ", dataset.head(20))

    # descriptions
    print("Statistical Summary: ", dataset.describe())

    # class distribution
    print("Class Distribution: ", dataset.groupby("class").size())

'''
/// step3() funktion zum 
/// + 4. Data Visualization
/// - 4.1 Univariate Plots
/// - 4.2 Multivariate Plots
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/21
'''
def step3():
    print("\nStep3: ...")

    print("\nPlot box and whisker plots:")
    # box and whisker plots
    dataset.plot(kind="box", subplots=True, layout=(2, 2), sharex=False, sharey=False)
    plt.show()

    print("\nPlot histograms:")
    # histograms
    dataset.hist()
    plt.show()

    print("\nscatter plot matrix:")
    # scatter plot matrix
    scatter_matrix(dataset)
    plt.show()

'''
/// step4() funktion zum 
/// + 5. Evaluate Some Algorithms
/// - 5.1 Create a Validation Dataset
/// - 5.2 Test Harness
/// - 5.3 Build Models
/// - 5.4 Select Best Model
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/21
'''
def step4():
    print("\nStep4: ...")

    global X_train, X_validation, Y_train, Y_validation

    # Split-out validation dataset
    array = dataset.values
    X = array[:,0:4]
    y = array[:,4]
    X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

    # Spot Check Algorithms
    models = []
    models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
    models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('CART', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC(gamma='auto')))
    # evaluate each model in turn
    results = []
    names = []
    for name, model in models:
        kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
        cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
        results.append(cv_results)
        names.append(name)
        print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

    # Compare Algorithms
    plt.boxplot(results, labels=names)
    plt.title('Algorithm Comparison')
    plt.show()

'''
/// step5() funktion zum 
/// + 6. Make Predictions
/// - 6.1 Make Predictions
/// - 6.2 Evaluate Predictions
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/21
'''
def step5():
    print("\nStep5: ...")

    # Make predictions on validation dataset
    model = SVC(gamma="auto")
    model.fit(X_train, Y_train)
    predictions = model.predict(X_validation)

    # Evaluate predictions
    print(accuracy_score(Y_validation, predictions))
    print(confusion_matrix(Y_validation, predictions))
    print(classification_report(Y_validation, predictions))

    return()

#endregion

#region Standardfunktionen und -verfahren
'''
///*********************************************************************************************************
///* Standardfunktionen und -verfahren                                                                     *
///*********************************************************************************************************
'''

'''
/// mainWindow() funktion zur 
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/20
'''
def mainWindow():
    os.system('cls')
    print("Artificial Intelligence by Python Step by Step\n")
    
    step1() # Step1 - Check the versions of libraries
    step2() # Step2 - Load The Data and Summarize the Dataset
    step3() # Step3 - Data Visualization
    step4() # Step4 - Evaluate Some Algorithms
    step5() # Step5 - Make Predictions

    print("\nEnde des Programms...", end = "")

    exit(0)

#endregion

#region Hauptprogramm
'''
/// Hauptprogramm, enthält Hauptanweisungen und Aufruffunktionen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/20
/// 
'''

mainWindow()

#endregion
