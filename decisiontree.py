
from sklearn import tree
from sklearn.externals.six import StringIO
import pandas as pd
import pydot

tennis = pd.read_csv("/Users/darchcruise/code/Python/data_science/tennisplayer/DecisionTree.csv")


#select columns from pandas table
Y = tennis[["Play"]]
X = tennis[["Wind","Outlook","Humidity"]]

#removes the settingwithcopywarning
pd.options.mode.chained_assignment = None

#replace strings with indicator numbers, since scikit didn't like the strings.
# X["Wind"].replace(["Strong","Weak"],[1,0],inplace=True)
# X["Outlook"].replace(["Sunny","Overcast","Rain"],[0,1,2],inplace=True)
# X["Humidity"].replace(["Normal","High"],[0,1],inplace=True)
# Y["Play"].replace(["No","Yes"],[0,1],inplace=True)




X["Wind"].replace(["Strong","Weak"],[1,0],inplace=True)
X["Outlook"].replace(["Sunny","Overcast","Rain"],[2,1,0],inplace=True)
X["Humidity"].replace(["High", "Normal"],[1,0],inplace=True)
Y["Play"].replace(["No","Yes"],[0,1],inplace=True)


#fit with scikit
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

def choices(wind,outlook,humidity):
	if wind == 'strong':
		w = 1
	else:
		w = 0
	if outlook == 'sunny':
		o = 2
	elif outlook == 'overcast':
		o = 1
	else:
		o = 0
	if humidity == 'high':
		h = 1
	else:
		h = 0

#check how our model decides for Weak,Rain,High
	print clf.predict([w,o,h])

#Write the decision tree to a picture
# dot_data = StringIO()
# tree.export_graphviz(clf, out_file=dot_data)
# graph = pydot.graph_from_dot_data(dot_data.getvalue())
# graph.write_pdf("tennis.pdf")


# wind: strong 1, weak 0
# outlook: sunny 0, overcast 1, rain 2
# humidity: normal 0, high 1



#         wind, outlook, humidity
choices('strong','rain','normal')
