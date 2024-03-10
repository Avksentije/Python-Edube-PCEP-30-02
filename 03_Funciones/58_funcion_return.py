def is_year_leap(year):
    if year in test_years:
        return test_results[i]

def days_in_month(year, month):
    if month < 1 or month > 12 or year < 0:
        return None
    if month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
