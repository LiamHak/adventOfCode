input_object = open("input.txt", "r")
input_data = input_object.readlines()
input_object.close()
cleaned_data = []

for line in input_data:
    cleaned_data.append(int(line.strip()))
input_size = len(cleaned_data)


for i in range(0, input_size):
    for j in range(i, input_size):
        if cleaned_data[i] + cleaned_data[j] == 2020:
            ans = cleaned_data[i]*cleaned_data[j]
            print(ans)
            break
