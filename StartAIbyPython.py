import pandas as pd  
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression  

# بارگذاری داده‌ها  
data = pd.read_csv('real_estate_data.csv')  
X = data[['size', 'bedrooms']]  # ویژگی‌ها  
y = data['price']  # برچسب‌ها  

# تقسیم داده‌ها به مجموعه‌های آموزشی و آزمایشی  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  

# آموزش مدل  
model = LinearRegression()  
model.fit(X_train, y_train)  

# پیش‌بینی  
predictions = model.predict(X_test)  
print(predictions)