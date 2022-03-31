import json
x={
    "Subscriptions": [
        {
            "name": "Three month subscription",
            "price": "39900",
            "discount": "50"
            },
            {
                "name": "One month subscription",
                "price": "19900",
                "discount": "30"
            },
            {
                "name": "Premium free trial",
                "price": "40000",
                "discount": "10"
                }
    ]
}
listi=x["Subscriptions"]
mini=1000000000000000
ans=""
for i in listi:
    price=int(i["price"])*((100-int(i["discount"]))/100)
    if p<mini:
        mini=price
        ans=i["name"]
print("Name: ", ans)
print("Price: ", int(mini))