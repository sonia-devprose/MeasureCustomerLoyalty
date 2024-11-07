# Customer loyalty program attributes
# Initial reward points that the customer currently owns
customer_reward = 50
# Total purchases done by the customer till now
customer_purchases = 5
# No.of Discounted coupons currently available to the customer
discounted_coupons = 2


# Criteria for loyalty calculation
# Bonus points awarded to the customer for completing a specific milestone
bonus_points = 20
# No.of coupons required to receive a special reward
coupon_threshold = 5

# Example of compound assignment operators
# Modifying loyalty program attributes
# Add 30 reward points
customer_reward += 30
# Increment by 1
customer_purchases += 1
# Redeem one discounted coupon
discounted_coupons -= 1
# Double the reward points
customer_reward *= 2
# Limit reward points to not exceed beyond 100
customer_reward %= 100

# Calculate a basic customer loyalty score
# score = (purchases_made * 10) + reward_points - (discounted_coupons * 5)
score = (customer_purchases * 10) + customer_reward - (discounted_coupons * 5)
# Display loyalty score
print ("The customer loyalty score is:  ", score)

# Use relational and logical operators to determine customer status
is_eligible_for_reward = (customer_purchases > 2) and (customer_reward > 50)
is_coupon_low = discounted_coupons <= 1

# Final assesment for deciding loyalty programs
if not is_eligible_for_reward:
	print("Not eligible for loyalty")
elif is_coupon_low:
 print("Eligible for rewards, but low on coupons")
else:
     print("Eligible for special loyalty")
     









