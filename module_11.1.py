import requests
import pandas as pd
import matplotlib.pyplot as plt

# Пример использования requests
response = requests.get('https://api.github.com')
print(f"Status Code: {response.status_code}")
print(f"JSON Response: {response.json()}")

# Пример использования pandas
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Gender': ['Female', 'Male', 'Male', 'Male']
}
df = pd.DataFrame(data)
print(df.head())
average_age = df['Age'].mean()
print(f"Average Age: {average_age}")
gender_counts = df['Gender'].value_counts()
print(f"Gender Counts:\n{gender_counts}")

# Пример использования matplotlib
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]
plt.plot(x, y)
plt.title('Sample Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
