def test(n):
    if n == 50:
        print("hampir tidak lulus")
        # print(n)
        print(50-n)
    elif n > 50:
        print("lulus", n)
    else:
        # print("lanjut dulu")
        # print(n)
        return test(n+5)

test(30)

# def faktorial1(n):
#     if n == 0 or n == 1:
#         print("pertama:", n)
#         return 1
#     else:
#         print("kedua:", n)
#         return n*faktorial1(n-1)

# print(faktorial1(3))

# def faktorial2(n,i,result=1):
#     if i>n:
#         print("n:", n)
#         print("i:", i)
#         print("result:",result)
#         return result
#     else:
#         print("n2:", n)
#         print("i2:", i)
#         print("result2:",result)
#         return faktorial2(n,i+1,result*i)

# print(faktorial2(3,1,result=1))