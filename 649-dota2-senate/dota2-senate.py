class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        num_r = 0
        num_d = 0

        # Count the number of D and Rs
        for mem in senate:
            if mem == "R":
                num_r += 1
            else:
                num_d += 1
        ban_r = 0
        ban_d = 0
        senate = list(senate)
        floating_d_bans = 0
        floating_r_bans = 0
        # Loop until all D's are banned or all Rs are banned
        while ban_d!=num_d and ban_r!=num_r:
            for i,mem in enumerate(senate):

                # Member is R
                if mem == 'R':
                    # There is a ban on R that isn't enforced yet
                    if floating_r_bans > 0:
                        floating_r_bans -= 1
                        senate[i] = 'X'
                        ban_r += 1
                    else:
                        floating_d_bans += 1
                if mem == 'D':
                    if floating_d_bans > 0:
                        floating_d_bans -= 1
                        senate[i] = 'X'
                        ban_d += 1
                    else:
                        floating_r_bans += 1
        if ban_r == num_r:
            return "Dire"
        return "Radiant"