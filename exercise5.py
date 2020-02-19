profit = float(input("Please enter your profit: "))
loss = float(input("Please enter your loss: "))
if profit < loss:
    print("your company is unprofitable")
else:
    print("your company is profitable")
    print("your profitability is: {:.2f}".format((profit-loss)/profit) )
