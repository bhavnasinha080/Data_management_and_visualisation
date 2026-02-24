from datetime import datetime
sales={"laptop":200, "camera": 300, "desk":400, "mouse":500}
totalrev=sum(sales.values)
maxprod=max(sales.items(), keys=lambda x: x[1])
print("Total= ", totalrev)
print("Maximum sale product= ", maxprod[3])