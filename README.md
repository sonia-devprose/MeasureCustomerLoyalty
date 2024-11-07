# Customer Loyalty Program: Python Model

## Overview

This Python model simulates a basic **customer loyalty program** used in e-commerce platforms to manage customer engagement, retention, and rewards. The program uses various Python operators, including arithmetic, relational, logical, and compound assignment operators, to calculate a loyalty score for the customer based on their activity (e.g., number of purchases, reward points, coupon usage). It also evaluates whether the customer is eligible for rewards and determines the customer's status in the loyalty program.

## Features

- **Customer Attributes**: Tracks key customer data, such as reward points, purchases made, and available coupons.
- **Loyalty Score Calculation**: Uses customer activity to calculate a loyalty score based on purchases and reward points.
- **Eligibility Assessment**: Determines if a customer is eligible for special rewards or needs further monitoring.
- **Discounts and Coupons**: Updates the available coupons and applies rules like limited rewards points or coupon redemption.
- **Conditions**: Uses relational, logical, and compound assignment operators to update customer attributes and evaluate their status.

## Components

1. **Customer Attributes**: 
   - **reward_points**: The total number of reward points a customer has.
   - **purchases_made**: The number of purchases made by the customer.
   - **discounted_coupons**: The number of available discounted coupons.
   
2. **Loyalty Calculation Parameters**: 
   - **bonus_points**: Bonus points added for completing a milestone (e.g., making 5 purchases).
   - **coupon_threshold**: The number of coupons required to receive special rewards or status.
   
3. **Loyalty Score Formula**:
   - The formula calculates a score based on:
     - Number of purchases (`purchases_made` * 10)
     - Reward points (`reward_points`)
     - Discounted coupons used (`discounted_coupons` * 5)

4. **Eligibility Assessment**:
   - A customer is considered **eligible for rewards** if:
     - They have made more than 2 purchases
     - They have more than 50 reward points.
   - If the customer has fewer than 2 coupons remaining, they are marked as **eligible for a reward but low on coupons**.
   - If none of the conditions are met, the customer is considered **not yet eligible for special rewards**.

## Code Walkthrough

```python
# Customer loyalty program attributes
reward_points = 50          # Initial reward points that the customer has
purchases_made = 3          # Total purchases made by the customer
discounted_coupons = 2      # Number of discounted coupons currently available to the customer

# Parameters for loyalty calculations
bonus_points = 20           # Bonus points given as a reward for completing a specific milestone (e.g., making a certain number of purchases)
coupon_threshold = 5        # Number of coupons required to receive a special reward or status

# Example of compound assignment operators with clarified comments
# Modifying loyalty program attributes
reward_points += 30         # Add 30 points as a special bonus (e.g., customer reached a milestone such as their 10th purchase)
purchases_made += 1         # Increment the total purchases made by 1 (e.g., the customer makes another purchase)
discounted_coupons -= 1     # Redeem 1 discounted coupon (e.g., used for a recent purchase)
reward_points *= 2          # Double the reward points as part of a promotional offer
reward_points %= 100        # Limit reward points to remain under 100 to prevent exceeding a maximum cap

# Calculate a basic customer loyalty score
score = (purchases_made * 10) + reward_points - (discounted_coupons * 5)

# Display calculated score
print("Customer Loyalty Score:", score)

# Use relational and logical operators to determine customer status
is_eligible_for_reward = (purchases_made > 2) and (reward_points > 50)  # Customer is eligible if they have made more than 2 purchases and have more than 50 reward points
is_coupon_low = discounted_coupons <= 1  # Check if the customer has 1 or fewer coupons remaining

# Final assessment based on conditions using logical "not"
if not is_eligible_for_reward:
    print("\nCustomer Status: Not yet eligible for special rewards.")
elif is_coupon_low:
    print("\nCustomer Status: Eligible for a reward but low on coupons.")
else:
    print("\nCustomer Status: Eligible for a special reward!")
```

## Operators Used

- **Arithmetic Operators**:
  - `+=`, `-=`: Increment and decrement customer data attributes (e.g., reward points, purchases made).
  - `*=`: Used to apply promotional offers or bonuses (doubling points).
  - `%=`: Limits reward points to stay under a specified cap.

- **Relational Operators**:
  - `>`: Checks if a customer has made more than 2 purchases or has more than 50 reward points.
  - `<=`: Determines if a customer has fewer than or equal to 1 coupon remaining.

- **Logical Operators**:
  - `and`: Ensures that both conditions (more than 2 purchases and over 50 points) are true for the reward eligibility.
  - `or`: Checks if a customer has fewer coupons or is not eligible for rewards.
  - `not`: Used to negate a condition, making sure that the status of the customer is updated correctly when they are not eligible for rewards.

