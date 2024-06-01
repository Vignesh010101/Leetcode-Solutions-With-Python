from heapq import heappush, heappop
class Solution:
    def longestRepeating(self, A: str, C: str, I: List[int]) -> List[int]:
        ii = [[0, 0, 1, A[0]]]
        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                ii[-1][1] = i
                ii[-1][2] += 1
            else:
                ii.append([i, i, 1, A[i]])

        hh = [-(ln) for _, _, ln, _ in ii]
        cc = defaultdict(int)
        for _, _, ln, _ in ii: cc[ln] += 1
        heapq.heapify(hh)

        rr = []
        for i in range(len(C)):
            idx = bisect_left(ii, I[i], key=lambda x: x[1])
            if ii[idx][3] == C[i]: 
                rr.append(-hh[0])
                continue
            if ii[idx][0] == ii[idx][1]:
                ii[idx][3] = C[i]
            elif ii[idx][0] == I[i]:
                ii[idx][0] = I[i] + 1
                cc[ii[idx][2]] -= 1
                ii[idx][2] -= 1
                cc[ii[idx][2]] += 1
                cc[1] += 1
                heappush(hh, -ii[idx][2])
                heappush(hh, -1)
                ii[idx:idx + 1] = [[I[i], I[i], 1, C[i]], ii[idx]]
            elif ii[idx][1] == I[i]:
                cc[ii[idx][2]] -= 1
                ii[idx][2] -= 1
                cc[ii[idx][2]] += 1
                cc[1] += 1
                heappush(hh, -ii[idx][2])
                heappush(hh, -1)
                ii[idx][1] = I[i] - 1
                ii[idx:idx + 1] = [ii[idx], [I[i], I[i], 1, C[i]]]
                idx += 1
            else:
                cc[ii[idx][2]] -= 1
                ii[idx:idx + 1] = [
                    [ii[idx][0], I[i] - 1, I[i] - ii[idx][0], ii[idx][3]],
                    [I[i], I[i], 1, C[i]], 
                    [I[i] + 1, ii[idx][1], ii[idx][1] - I[i], ii[idx][3]],
                ]
                cc[ii[idx][2]] += 1
                cc[ii[idx + 2][2]] += 1
                cc[1] += 1
                heappush(hh, -ii[idx][2])
                heappush(hh, -ii[idx + 2][2])
                heappush(hh, -1)
                idx += 1
            
            if idx + 1 < len(ii) and ii[idx + 1][3] == C[i]:
                cc[ii[idx][2]] -= 1
                cc[ii[idx + 1][2]] -= 1
                ii[idx + 1][0] = ii[idx][0]
                ii[idx + 1][2] += ii[idx][2]
                ii[idx:idx + 2] = ii[idx + 1:idx + 2]
                cc[ii[idx][2]] += 1
                heappush(hh, -ii[idx][2])
            if idx > 0 and ii[idx - 1][3] == C[i]:
                cc[ii[idx][2]] -= 1
                cc[ii[idx - 1][2]] -= 1
                ii[idx - 1][1] = ii[idx][1]
                ii[idx - 1][2] += ii[idx][2]
                ii[idx - 1:idx + 1] = ii[idx - 1:idx]
                cc[ii[idx - 1][2]] += 1
                heappush(hh, -ii[idx - 1][2])
            
            while hh and not cc[-hh[0]]:
                heappop(hh)
            rr.append(-hh[0])
        return rr