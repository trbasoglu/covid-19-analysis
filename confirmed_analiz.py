import csv
import matplotlib.pyplot as plt

def sumCasesInStates(_countries, _dict, _day_number):
    for _country in _countries:
        cases = _dict[_country]
        actual_cases = []
        for i, case in enumerate(cases):
            if i < _day_number:
                actual_cases.append(case)
            else:
                actual_cases[i%_day_number]+=case
        _dict[_country]= actual_cases
    return _dict

def numbersFromFirstCase(_dict,_days):
    for _country in _dict.keys():
        cases = _dict[_country]
        casesFromFirst = []
        isFirstCaseFound = False
        for case in cases:
            if case > 0:
                isFirstCaseFound = True
            if isFirstCaseFound:
                casesFromFirst.append(case)
        _dict[_country] = {"cases":casesFromFirst, "firstDay":_days[-len(casesFromFirst)], "Total":casesFromFirst[-1]}
    return _dict


COVID19_confirmed_csv = open("time_series_covid_19_confirmed.csv", encoding="utf-8-sig")
csv_reader = csv.reader(COVID19_confirmed_csv)
line_count = 0
countryDict={}
# {'id': 0, 'case_in_country': 1, 'reporting date': 2, '': 26, 'summary': 4, 'location': 5, 'country': 6, 'gender': 7, 'age': 8, 'symptom_onset': 9, 'If_onset_approximated': 10, 'hosp_visit_date': 11, 'exposure_start': 12, 'exposure_end': 13, 'visiting Wuhan': 14, 'from Wuhan': 15, 'death': 16, 'recovered': 17, 'symptom': 18, 'source': 19, 'link': 20}
tags=dict()
countriesHasState = []
days=[]
for row in csv_reader:
    if line_count == 0:
        for i, tag in enumerate(row):
            tags[tag]=i
            if i > 3:
                days.append(tag)
        line_count += 1
    else:
        # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
        state = row[tags['Province/State']]
        country = row[tags['Country/Region']]
        if not country in countryDict.keys():
            countryDict[country]=[]
        elif not country in countriesHasState:
            countriesHasState.append(country)
        for dailyNumber in row[4:]:
                countryDict[country].append(int(dailyNumber))
       
        line_count += 1
print(tags)

first20Countries = []
day_number = len(tags)-4
countryDict = sumCasesInStates(countriesHasState, countryDict, day_number)
countryDict_fromFirst = numbersFromFirstCase(countryDict, days)


Italy = countryDict_fromFirst['Italy']["cases"][:10]
Spain = countryDict_fromFirst['Spain']["cases"][:10]
US = countryDict_fromFirst['US']["cases"][:10]
Germany = countryDict_fromFirst['Germany']["cases"][:10]
Iran = countryDict_fromFirst['Iran']["cases"][:10]
France = countryDict_fromFirst['France']["cases"][:10]
KoreaSouth = countryDict_fromFirst['Korea, South']["cases"][:10]
Switzerland = countryDict_fromFirst['Switzerland']["cases"][:10]
UnitedKingdom = countryDict_fromFirst['United Kingdom']["cases"][:10]
Netherlands = countryDict_fromFirst['Netherlands']["cases"][:10]
Turkey = countryDict_fromFirst['Turkey']["cases"][:10]

days = [1,2,3,4,5,6,7,8,9,10]

plt.xlabel('Days')
plt.ylabel('Cases')
plt.plot(days, Italy,  label="Italy")
plt.plot(days, Spain,  label="Spain")
plt.plot(days, US,  label="US")
plt.plot(days, Germany,  label="Germany")
plt.plot(days, Iran,  label="Iran")
plt.plot(days, France,  label="France")
plt.plot(days, KoreaSouth,  label="Korea")
plt.plot(days, Switzerland,  label="Switzerland")
plt.plot(days, Netherlands,  label="Netherlands")
plt.plot(days, Turkey,  label="Turkey")
plt.legend()
plt.show()