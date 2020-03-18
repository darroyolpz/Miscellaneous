# Send emails up to 100

import pandas as pd

excel_file = 'Emails data.xlsx'
df = pd.read_excel(excel_file)

max_list = 10
email_list = ''

for row in df['Email']:
	list_len = email_list.count(';')
	if list_len < max_list:
		email_list = email_list + str(row) + '; '
	else:
		print(email_list)
		print('\n')
		email_list = str(row) + '; '

print('Last one:')
print('\n')
print(email_list)
print('\n')

