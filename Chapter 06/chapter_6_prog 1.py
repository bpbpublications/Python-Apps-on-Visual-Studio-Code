total_chars = 256
#total 256 all possible characters

def smallestWindow(mainstr, pattern):
   n = len(mainstr)
   if n < len(pattern):
      return -1
   mp = [0]*total_chars

   # Starting index of ans
   start = 0

   # Length of ans
   ans = n + 1
   cnt = 0

   # creating map
   for i in pattern:
      mp[ord(i)] += 1
      if mp[ord(i)] == 1:
         cnt += 1

   # References of Window: j will move by each character
    #i will be used to remove the duplicate entry
   i,j = 0,0

   # Traversing the window
   while(j < n):

   # Calculating
      mp[ord(mainstr[j])] -= 1
      if mp[ord(mainstr[j])] == 0:
         cnt -= 1

         # Condition matching
         while cnt == 0:
            if ans > j - i + 1:

            # calculating answer.
               ans = j - i + 1
               start = i

            # Sliding I:removing from I
            mp[ord(mainstr[i])] += 1
            if mp[ord(mainstr[i])] > 0:
               cnt += 1
            i += 1
      j += 1
   if ans > n:
      return "-1"
   return mainstr[start:start+ans]
#Now writing the code to execute the above function:
# Driver code
s = 'i am on a seafood diet. i see food and i eat it.'
t = 'fast'
small_window = smallestWindow(s, t)
if small_window =="-1":
    print("No such window possible")
else:
    print(f'Window is "{small_window}" and Minimum length between'
          f'the substring is {len(small_window)}')