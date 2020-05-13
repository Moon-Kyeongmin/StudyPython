for i in range(0,10,2):
    print(i,"=반복변수")

array=[11,22,33,44,55,66]

for i in range(len(array)):
    print(i+1,array[i])

# while True:
#     print(".",end="")

i=0
while True:
    print("{}번째 반복".format(i+1))
    i+=1

    input_text=input("> 종료합니까?(y)")
    if input_text in ["y","Y"]:
        print("반복 종료")
        break