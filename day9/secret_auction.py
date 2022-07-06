import auction_art
print(auction_art.logo)

bids = {}
continue_auction = True

while continue_auction:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n$"))
    bids[name] = bid
    add_bid = input("Are there any other users who would like to bid?\n").lower()
    if add_bid == "no":
        continue_auction = False

print(bids)
winning_bid = 0
winner = ""
for bidder in bids:
    amount_bid = bids[bidder]
    if amount_bid > winning_bid:
        winning_bid = amount_bid
        winner = bidder


print(f"The winner was {winner} with a bid of ${winning_bid}!")
