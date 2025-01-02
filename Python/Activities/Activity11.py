fruits_Availability = {
        "apple": 2,
        "Cherry" :10,
        "banana": 5,
        "orange": 80,
        "grapes" :20    
}

customer_Requirement = input("which fruit you are looking for sir!! ").lower()
if(customer_Requirement in fruits_Availability):
    print("Yes, its available")
else:
    print("No, this fruits is unavaibale now")