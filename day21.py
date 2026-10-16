# # for i in range(12):
# #     print(i+1)
# #     if i==9:
# #         print("The value of i is",i)
# #         break

# # print("loop ko chodkar nikal gaya")

# for i in range(12):
#     if i==9:
#         print("Skipped the iteration")
#         continue
#     print(i+1)
#     print(i+1)
#     print(i+1)
#     print(i+1)
#     print(i+1)
#     print(i+1)
#     print(i+1)
    
# # print("loop ko chodkar nikal gaya")

# Keep asking until the user enters 0; break then exits the loop.
while True:
    i=int(input("Enter a number(0 to exit): "))
    print("You entered",i)
    if i==0:
        break
