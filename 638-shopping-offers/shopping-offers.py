class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def _impl(current_needs, dp_table):
            if current_needs in dp_table:
                return dp_table[current_needs]
            length = len(price)
            min_price = float("inf")

            for spec in special:
                can_use = True
                for i in range(length):
                    if spec[i] > current_needs[i]:
                        can_use = False
                        break
                if can_use:
                    current_price = spec[-1] + _impl(
                        tuple([need - consume for consume, need in zip(spec, current_needs)]),
                        dp_table
                    )
                    if current_price < min_price:
                        min_price = current_price

            if not math.isinf(min_price):
                dp_table[current_needs] = min_price
                return min_price

            current_price = 0
            for i, n in enumerate(current_needs):
                current_price += n * price[i]

            dp_table[current_needs] = current_price
            return current_price

        length = len(price)
        useful_special = []
        for spec in special:
            current = 0
            for i in range(length):
                current += price[i] * spec[i]
            if current > spec[-1]:
                useful_special.append(spec)
        special = useful_special
        return _impl(tuple(needs), {})