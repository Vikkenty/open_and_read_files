file_names = ['1.txt', '2.txt', '3.txt']
line_counts = []
for file_name in file_names:
    with open (file_name, encoding = 'utf-8') as file:
        lines = file.readlines()
        line_count = len(lines)
        line_counts.append(line_count)
# print(line_counts)

data = []
for file_name, line_count in zip(file_names, line_counts):
    with open(file_name, encoding='utf-8') as file:
        content = file.read()
        # print(content)
        data.append({'file_name': file_name, 'line_count': line_count, 'content': content})
# print(data)

sorted_data = sorted(data, key=lambda x: x['line_count'])
# print(sorted_data)

with open('result.txt', 'w', encoding='utf-8') as result_file:
    for file_data in sorted_data:
        file_name = file_data['file_name']
        line_count = file_data['line_count']
        content = file_data['content']
        result_file.write(f'Имя файла: {file_name}\n')
        result_file.write(f'Количество строк: {line_count}\n')
        result_file.write(content)