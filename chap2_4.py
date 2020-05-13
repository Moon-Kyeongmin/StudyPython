format_a="{}".format(1000);
format_b="hello {} {}".format(10,20);
print(format_a)
print(format_b)

print(type(format_b))

output_a="{:010d}".format(30)

print(output_a)

input_s="Hello Python Programming"
input_t="""
    안녕하세요      
    테스트입니다.               
"""
input_r="배고프다 배부르다"

print(input_s.upper())
print(input_s.lower())

print(input_t.strip())

print("안뇽" in "안뇽하세요")
print("안뇽" in "안녕하세요")
print(input_r.find("아아아"))

a="10,20,30,40,50,60".split(",")
b="1|2|3|4|5|6".split("|")
print(a)
print(a[0])

print(b)