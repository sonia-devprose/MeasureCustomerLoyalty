Customer Loyalty Program: Python Model
Overview
This Python model simulates a basic customer loyalty program used in e-commerce platforms to manage customer engagement, retention, and rewards. The program uses various Python operators, including arithmetic, relational, logical, and compound assignment operators, to calculate a loyalty score for the customer based on their activity (e.g., number of purchases, reward points, coupon usage). It also evaluates whether the customer is eligible for rewards and determines the customer's status in the loyalty program.

Features
Customer Attributes: Tracks key customer data, such as reward points, purchases made, and available coupons.
Loyalty Score Calculation: Uses customer activity to calculate a loyalty score based on purchases and reward points.
Eligibility Assessment: Determines if a customer is eligible for special rewards or needs further monitoring.
Discounts and Coupons: Updates the available coupons and applies rules like limited rewards points or coupon redemption.
Conditions: Uses relational, logical, and compound assignment operators to update customer attributes and evaluate their status.
Components
Customer Attributes:

reward_points: The total number of reward points a customer has.
purchases_made: The number of purchases made by the customer.
discounted_coupons: The number of available discounted coupons.
Loyalty Calculation Parameters:

bonus_points: Bonus points added for completing a milestone (e.g., making 5 purchases).
coupon_threshold: The number of coupons required to receive special rewards or status.
Loyalty Score Formula:

The formula calculates a score based on:
Number of purchases (purchases_made * 10)
Reward points (reward_points)
Discounted coupons used (discounted_coupons * 5)
Eligibility Assessment:

A customer is considered eligible for rewards if:
They have made more than 2 purchases
They have more than 50 reward points.
If the customer has fewer than 2 coupons remaining, they are marked as eligible for a reward but low on coupons.
If none of the conditions are met, the customer is considered not yet eligible for special rewards.
