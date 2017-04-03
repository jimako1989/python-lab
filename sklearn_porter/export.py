from sklearn.datasets import load_iris
from sklearn.tree import tree
from sklearn_porter import Porter

# Load data and train the classifier:
iris_data = load_iris()
X, y = iris_data.data, iris_data.target
clf = tree.DecisionTreeClassifier()
clf.fit(X, y)

# Export:
porter = Porter(clf, language='java')
output = porter.export()
with open(file="import.java", mode='w') as f:
	f.write(output)