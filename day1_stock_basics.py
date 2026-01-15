stock_name = "Zomato"
today_price = 1669
yesterday_price = 1223

print("Stock:", stock_name)
print("Today's Price:", today_price)
print("Yesterday's Price:", yesterday_price)

if today_price < yesterday_price:
    print("Risk Alert: Price is failing")
else:
    print("No Risk: Price is stable or rising") 

    
