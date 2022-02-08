def solution(order, shoppers):
    should_take = []
    for shopper in shoppers:
        # Get ime to fill the order
        order_time = (order[0] + shopper[0]) / shopper[1] + shopper[2]
        # Determine if there's idle time. If there is shopper shouldn't take order.
        if order[1] > order_time or order[1] + order[2] < order_time:
            should_take.append(False)
        else:
            should_take.append(True)
    return should_take

order = [200, 20 , 15]
shoppers = [[300, 40, 5], [600, 40, 10]]
for i, result in enumerate(solution(order, shoppers)):
    print("SHOPPER", i, "--> Result:", result)
