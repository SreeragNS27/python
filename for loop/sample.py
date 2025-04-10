# def add(a):
#     if a==0:
#         return 0
#     else:
#         return a+add(a-1)
# e=add(5)
# print(e)
# def add(a):
#     if a==:
#         return 1
#     else:
#         return a+add(a+1)
#     b=add(5)
#     print(b)

# sum of the digits by using Recursive function

# def sam(a):
#     b=0
#     c=0
    
#     if a==0:
#         return 0
#     else:
#         c=a%10
#         b=b*10+c
#         a//=10
        
#         return (c+sam(a))
# f=sam(347)
# print(f)
# anonymous function

# a=lambda b,c: b+c
# print(a(3,6))

# reverse a string

# def rev(a):
#     if len(a)==1:
#         return a
#     else:
#         return rev(a[1:])+a[0]
# f=rev("sree")
# print(f) 