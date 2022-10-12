
         # Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

   
with open('File1.txt', 'r') as file:
    my_text = file.readline()
    compression_text = my_text.split()

print(my_text)

def encode(text):
   encoding = ""
   i = 0
   while i < len(text):
      count = 1
      while i + 1 < len(text) and text[i] == text[i + 1]:
         count = count + 1
         i = i + 1
      encoding = encoding + str(count) + text[i]
      i = i + 1
   return encoding

def decode(data):
   decoding = ""
   count = ""
   for char in data:
      if char.isdigit():
         count = count + char

      else:
         decoding = decoding + char * int(count)
         count = count + 1
   return decoding

compression_text = encode(my_text)

with open('File2_Ex004.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{compression_text}')
print(compression_text)
