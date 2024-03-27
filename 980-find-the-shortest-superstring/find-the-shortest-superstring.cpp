 class Solution {
 public:
 	string shortestSuperstring(vector<string>& A) {
 		const int n = A.size();
 		vector<vector<int>> g(n, vector<int>(n));
 		for(int f = 0; f < n; ++f){
 			int flen = A[f].length();
 			for(int s = 0; s < n; ++s){
 				if(s == f) continue;
 				int slen = A[s].length();
 				g[f][s] = slen;
 				for(int i = 1; i <= min(flen, slen); ++i){
 					if(A[f].substr(flen - i) == A[s].substr(0, i))
 						g[f][s] = slen - i;
 				}
 			}
 		}
 		vector<vector<int>> dp(1 << n, vector<int>(n, INT_MAX >> 1));
 		vector<vector<int>> parent(1 << n, vector<int>(n, -1));			
 		for(int i = 0; i < n; ++i) dp[1 << i][i] = A[i].length();			
 		for(int s = 1; s < (1 << n); ++s){ // 访问的集合
 			for(int j = 0; j < n; ++j){ // 最后的出口结点
 				if(!(s & (1 << j))) continue;
 				int ps = s & ~(1 << j);
 				for(int i = 0; i < n; ++i){
 					if(!(ps & (1 << i))) continue;
 					if(dp[ps][i] + g[i][j] < dp[s][j]){
 						dp[s][j] = dp[ps][i] + g[i][j];
 						parent[s][j] = i;
 					}
 				}
 			}
 		}
 		
 		auto it = min_element(begin(dp.back()), end(dp.back()));
 		int j = it - begin(dp.back());
 		int s = (1 << n) - 1;
 		string res;
 		while(s){
 			int i = parent[s][j];
 			if(i < 0) res = A[j] + res;
 			else    res = A[j].substr(A[j].length() - g[i][j]) + res;
 			s &= ~(1 << j);
 			j = i;
 		}
 		return res;
 	}
 };