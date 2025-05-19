import chardet

with open('dict.txt', 'rb') as f:
    result = chardet.detect(f.read(10000))  # анализируем первые 10Кб
print(result['encoding'])  # выведет предполагаемую кодировку