import random, string
import pandas as pd

# Randomize the entries
def randomString(stringLength=10):
    letter_type = string.ascii_lowercase + string.digits
    new_string = ''.join(random.choice(letter_type) for i in range(stringLength))
    return new_string

def randomField(df, field):
	unique_fields = df[field].unique()
	for value in unique_fields:
		df.loc[df[field] == value, field] = randomString()

excel_file = 'Sales.xlsx'
df = pd.read_excel(excel_file)

randomField(df, 'Customer')
print(df.head())