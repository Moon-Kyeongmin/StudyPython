# numbers=[1,2,3,4,5,6,7,11]

# for i in reversed(numbers):
#     print("첫번째 반복문 {}".format(i))

# for i in reversed(numbers):
#     print("두번째 반복문 {}".format(i))

example_list=["itemA","itemB","itemC","itemD"]

print(example_list)
print(list(enumerate(example_list)))

for i, value in enumerate(example_list):
    print("{}번째 요소는 {}".format(i,value))

example_dict={
    "키A":"값A",
    "키B":"값B",
    "키C":"값C",
    "키D":"값D",
}

print(example_dict.items())

for key,element in example_dict.items():
    print("dictionary[{}]={}".format(key,element))

