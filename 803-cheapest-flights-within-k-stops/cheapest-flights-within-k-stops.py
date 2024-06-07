class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices: List[int] = [float('inf')] * n
        prices[src] = 0
        for stopI in range(k + 1):
            curr_prices: List[int] = prices.copy()
            for flight_from, flight_to, flight_price in flights:
                new_price: int = prices[flight_from] + flight_price
                if new_price < curr_prices[flight_to]:
                    curr_prices[flight_to] = new_price
            prices = curr_prices
        return -1 if prices[dst] == float('inf') else prices[dst]