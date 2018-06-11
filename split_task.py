"""Napisać program, który odczyta informacje z łańcucah znaków i wyświetli:
- dla każdego typu testu: ilość jego wywołań zakończonych sukcesem i ilość
wykonań zakończonych porażką
- nazwę testu, który wykonywał się najdłużej, biorąc pod uwagę jedynie testy,
które zakończyły się powodzeniem"""


RECORDS = "test_user_login,2.0,success\n test_display_devices,1.3,failure\n test_display_devices,1.2,success\n " \
          "test_user_logout,1.2,success\n test_show_alerts,10.0,failure"

temp = RECORDS.replace('\n', ',')
table = temp.split(',')


parts = {}
for i in range (0, len(table), 3):
    if table[i] in parts:
        parts[table[i]].append(table[i+1])
        parts[table[i]].append(table[i+2])
    else:
        parts[table[i]] = [table[i+1], table[i+2]]

print(parts)

for key, value in parts.items():
    for idx, record in enumerate(value):
        if record == 'success':
            max_time = str(float(max(value[idx-1])))

for key in parts:
    for part in parts[key]:
        if part == max_time:
            print (key)





