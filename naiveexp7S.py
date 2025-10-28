from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = [[180, 75, 43], [165, 55, 38], [175, 70, 42],
        [160, 50, 37], [185, 80, 44], [170, 60, 39]]
y = ["M", "F", "M", "F", "M", "F"]

X_train ,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model =GaussianNB()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print("y_pred:",y_pred)
print("y_test:",y_test)
print(accuracy_score(y_test, y_pred)*100)

new_data = [[170, 65, 40]]
print(f"\nNew prediction [170cm, 65kg, size 40]: {model.predict(new_data)}")