# Exercise Grading Program
    # student_scores = {
    #     "Harry" : 81,
    #     "Ron" : 78,
    #     "Med Ali" : 99,
    #     "Draco" : 74,
    #     "Neville" : 62,
    # }
    # student_grades = {}
    # for student in student_scores :
    #     if student_scores[student] > 90 :
    #         student_grades[student] = "Outstanding"
    #     elif student_scores[student] > 80 :
    #         student_grades[student] = "Exceeds Expectations"
    #     elif student_scores[student] > 70 :
    #         student_grades[student] = "Acceptable" 
    #     else :  
    #         student_grades[student] = "Fail"   
    # print(student_grades) 
     
 # Dictionary in List
# travel_log = [
#      {
#          "country" : "France",
#          "visits" : 12,
#          "cities" : ["Paris", "Lille", "Dijon"]
#      },
#      {
#       "country" : "Germany",
#          "visits" : 5,
#          "cities" : ["Berlin", "Hamburg", "Stuttgart"]   
#      }
#  ]
# def add_new_country (country_visited, visits_number, cities_visited ):
#     new_country = {}
#     new_country ["country"] = country_visited
#     new_country["visits"] = visits_number
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)
    
# add_new_country ("Russia", 2, ["Moscow", "Saint Petersburg"])  
# print(travel_log)  

# Project Auction
import os

def clear():
    # Clear the console based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
from Art import logo 
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bids_record):
    highest = 0
    winner = ""
    for bidder in bids_record :
        bidder_amount = int(bids_record[bidder])
        if bidder_amount > highest:
            highest = bidder_amount
            winner = bidder
    print(f"the winner is {winner} with a bid {highest}")      

while not bidding_finished :
    name = input("what is your name :")
    price = input("what is your bid :$ ")
    bids[name] = price
    should_continue = input("are there any other bidders ? Type 'yes' or 'no :")
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)    
    elif should_continue == 'yes':
        clear()
            

print(bids)
                     