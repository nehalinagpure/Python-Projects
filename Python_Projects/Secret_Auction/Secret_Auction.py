import logo
print(logo.logo_auction)


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amout = bidding_dictionary[bidder]
        if bid_amout > highest_bid:
            highest_bid = bid_amout
            winner = bidder
    print(f"The winner is {winner} with the bid amount ${highest_bid}.")


bids = {}

continue_bidding = True
while continue_bidding:
    name = input("what is your name? ")
    price = int(input("What is your bid? $"))   
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no' ").lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 50)
