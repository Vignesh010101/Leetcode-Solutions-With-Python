class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9 + 7  # Define the modulo value for the final result
        res = 1  # Initialize the result variable to 1 (will be updated during iteration)
        prev_seat = 0  # Initialize the variable to track the index of the previous seat
        num_seats = 0  # Initialize the variable to count the number of seats encountered

        for i, c in enumerate(corridor):
            if c == 'S':
                num_seats += 1  # Increment the seat count when 'S' is encountered
                # Check if there are more than 2 consecutive seats and an odd number of seats
                if num_seats > 2 and num_seats % 2 == 1:
                    # Update the answer using the distance between the current seat and the previous seat
                    res *= i - prev_seat
                prev_seat = i  # Update the previous seat index to the current index

        # Return the answer only if there are more than 1 seat and an even number of seats
        return res % mod if num_seats > 1 and num_seats % 2 == 0 else 0