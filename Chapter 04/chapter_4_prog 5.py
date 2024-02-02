from scipy.special import comb

sum=0
#find combinations of 5, 2 values using comb(N, k)
#selecting 4 boys: 6C4
com = comb(6, 4, exact = False, repetition=False)
sum+=com
#selecting 3 boys and 1 girl: 6C3 × 4C1
com = comb(6, 3) * comb(4, 1)
sum+=com
#selecting 2 boys and 2 girls: 6C2 × 4C2
com = comb(6, 2) * comb(4,2)
sum+=com
#selecting 1 boy and 3 girls: 6C1 × 4C3
com = comb(6, 1) * comb(4, 3)
sum+=com
print("Total combination possible: ",sum)