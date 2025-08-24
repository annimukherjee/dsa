## DSA

I will be documenting my learning journey in Data Structures and Algorithms here. I will be using C++ / Python / Java for this purpose.

I am trying to follow [Striver's A2Z DSA Course/Sheet](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2). It's extremely organised, starts from the fundamentals and goes on to advanced topics. I will be following this course and also supplementing it with other resources like [GeeksforGeeks](https://www.geeksforgeeks.org/) and [LeetCode](https://leetcode.com/).

I hope to make a commit everyday as I learn one new thing everyday. I will be taking notes in Markdown and also include C++ files where necessary.

I hope that this *public contract* will keep me accountable and help me stay consistent in my learning.

[![LeetCode](https://img.shields.io/badge/LeetCode-orange?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/u/annimukh/)
[![HackerRank](https://img.shields.io/badge/HackerRank-2EC866?style=for-the-badge&logo=hackerrank&logoColor=white)](https://www.hackerrank.com/profile/mukh_aniruddha)
[![Codolio](https://img.shields.io/badge/Codolio-blueviolet?style=for-the-badge)](https://codolio.com/profile/annimukh)


<summary>Problems I've solved</summary>


### HackerRank:
1. https://www.hackerrank.com/challenges/solve-me-first/problem (5 Feb 2025)
2. https://www.hackerrank.com/challenges/cpp-hello-world/problem?isFullScreen=true (5 Feb 2025)
3. https://www.hackerrank.com/challenges/c-tutorial-basic-data-types/problem?isFullScreen=true (5 Feb 2025)
4. https://www.hackerrank.com/challenges/cpp-input-and-output/problem?isFullScreen=true (9 Feb 2025)
5. https://www.hackerrank.com/challenges/c-tutorial-for-loop/problem?isFullScreen=true (12 Feb 2025)
6. https://www.hackerrank.com/challenges/c-tutorial-conditional-if-else/problem?isFullScreen=true (12 Feb 2025)
7. https://www.hackerrank.com/challenges/c-tutorial-functions/problem?isFullScreen=true (12 Feb 2025)
8. https://www.hackerrank.com/challenges/c-tutorial-pointer/problem?isFullScreen=true
9. https://www.hackerrank.com/challenges/arrays-introduction/problem?isFullScreen=true
10. https://www.hackerrank.com/challenges/python-division/problem?isFullScreen=true [Python] (23 Mar 2025)
11. https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true [Python] (23 Mar 2025)
12. https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true [Python] (24 Mar 2025)
13. https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true [Python] (24 Mar 2025)
14. https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem?isFullScreen=true [Python] (24 Mar 2025)
15. https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true [Python] (24 March 2025)
16. https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true [Python] (24 March 2025)
17. https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true [Python, Numpy] (25 March 2025)
18. https://www.hackerrank.com/challenges/bash-tutorials---the-world-of-numbers/problem?isFullScreen=true [Bash] (28th March 2025)
19. https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true [Python, sWAP cASE] (2nd April 2025)
20. https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true [Python, Basic Printing] (4th April 2025)
21. https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true [Array Sum] (9th Apr 2025)
22. https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true [Python, Sets] (10th Apr 2025)
23. https://www.hackerrank.com/challenges/conditional-statements-in-c/problem?isFullScreen=true [If-Else in C] (12th Apr 2025)
24. https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true [Sliding Window Substring Matching] (13th Apr 2025)
    1.  Learnt how to slide a window over a string to find a substring. Created https://claude.site/artifacts/d26622f9-69ef-4dfa-90da-303be1cea047 to visualize it.
    2.  Trying to setup `commitizen`
25. https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true (15 Apr 2025)
    1.  Learnt `s.add()` method in set for Python.
26. https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
    1.  Learnt about `split()` and `join()`. I knew split which splits a string into a list (`" "` is the default delimiter). However `join()` I didn't know too well. `"-".join(a)` where `a` is a list returns `"a[0]-a[1]-a[2]...a[len(a)-1]"`
27. https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true [Python Lists]
    1.  Slew of List functions like `pop`, `append`, `l[::-1]`, `.remove`, `.sort`.
    2.  `sort` sorts the list in-place.
28. https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true
    1.  Use `zip` which iterates over tuples.
    2.  Basic `if`, `elif` and `else` logic.
29. https://www.hackerrank.com/challenges/bash-tutorials---a-personalized-echo/problem
    1.  To get input in `bash` use the read command. Nice [Bash Tutorial for beginners here](https://www.panix.com/~elflord/unix/bash-tute.html).
30. https://www.hackerrank.com/challenges/text-processing-cut-1/problem
    1.  `cut -b <num>` gets the `<num>` byte from a string.
31. https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
    1.  Sort the list, record the highest score. Keep on looping through the list from the end and check if the current value is equal to the highest score or not, if it is then that score is not the runner up. So continue. Else the current value is not equal to the highest score, then it must be the runner up as the list has already been sorted with the `.sort()` command which sorts a list in place in Python.


### Leetcode:
1. https://leetcode.com/problems/concatenation-of-array/description/ (18 Mar 2025)
2. https://leetcode.com/problems/return-length-of-arguments-passed/description/ (18 Mar 2025)
3. Height Checker: https://leetcode.com/problems/height-checker/description/?envType=problem-list-v2&envId=array (18 Mar 2025)
4. https://leetcode.com/problems/display-the-first-three-rows/description/ [Pandas] (18 Mar 2025)
5. https://leetcode.com/problems/modify-columns/description/ (20th Mar 2025)
6. https://leetcode.com/problems/rename-columns/description/ [Pandas] (20th Mar 2025)
7. https://leetcode.com/problems/change-data-type/description/ [Pandas] (20th Mar 2025)
8. https://leetcode.com/problems/select-data/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata [Pandas] (22nd Mar 2025)
9. https://leetcode.com/problems/recyclable-and-low-fat-products/description/?envType=study-plan-v2&envId=top-sql-50 [SQL] (27th Mar 2025)
10. https://leetcode.com/problems/find-customer-referee/description/?envType=study-plan-v2&envId=top-sql-50 [SQL] (27th Mar 2025)
11. https://leetcode.com/problems/big-countries/?envType=study-plan-v2&envId=top-sql-50 [SQL] (27th Mar 2025)
12. https://leetcode.com/problems/article-views-i/description/?envType=study-plan-v2&envId=top-sql-50 [SQL] (27th Mar 2025)
13. https://leetcode.com/problems/create-a-dataframe-from-list/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata [Pandas] (29th Mar 2025)
14. https://leetcode.com/problems/get-the-size-of-a-dataframe/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata [Pandas] (29th Mar 2025)
15. https://leetcode.com/problems/create-a-new-column/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata [Pandas] (29th March 2025)
16. https://leetcode.com/problems/drop-duplicate-rows/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata [Pandas] (29th March 2025)
17. https://leetcode.com/problems/drop-missing-data/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata [Pandas] (30th March) (nice [editorial](https://leetcode.com/problems/drop-missing-data/editorial/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata))
18. https://leetcode.com/problems/check-if-the-number-is-fascinating/description/ [Hash Table, Math] (30th March 2025)
19. https://leetcode.com/problems/number-of-good-pairs/ [DSA] (31st March 2025)
20. https://leetcode.com/problems/add-two-integers/description/ [Add 2 Numbers xD] (7 Apr 2025)
21. https://leetcode.com/problems/valid-palindrome/description/ [Palindrome] (7 Apr 2025)
22. https://leetcode.com/problems/intersection-of-two-arrays/description/ [Intersection of Two Arrays] (8 Apr 2025)
23. https://leetcode.com/problems/plus-one/ [Plus One] (9 Apr 2025)
24. https://leetcode.com/problems/shuffle-the-array/description/ [Shuffle an Array] (9 Apr 2025)
25. https://leetcode.com/problems/fill-missing-data/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata [Pandas] (11 Apr 2025)
26. https://leetcode.com/problems/running-sum-of-1d-array/description/ [Running Sum of 1D Array] (15 Apr 2025)
    1. Did a running sum of the array.
 27. https://leetcode.com/problems/sqrtx/ (15 Apr 2025)
     1.  Did this in O(n) time. Problem is to find the square root of a number without using built in functions. Can do this with binary search and thus reduce the problem into `O(log(n))`
 28. https://leetcode.com/problems/reshape-data-concatenate/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata (16 April)
     1.  Essentially teaches you how to use the `pd.concat()` function. `concat()` allows you to glue dataframes together. If `axis=0` it does a row wise concatenation (increase the height of the dataframe) and if `axis=1`, it does a column wise concatenation (increase the width of the dataframe). Also supports `join` etc. i.e. `inner` and `outer`. [Great short medium article here](https://medium.com/@connor.m.killion/joins-concat-vs-merge-inner-vs-outer-with-pandas-b27d36b63752).
 29. https://leetcode.com/problems/method-chaining/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
     1.  Method Chaining. Filter, sort the df by weight using `sort_values(by='col_name')` and then get the necessary column.
 30. https://leetcode.com/problems/add-digits/description/?envType=problem-list-v2&envId=prshgx6i
     1.  Take an integer, add all the digits of that integer to get a number. If that number has more than one digit, repeat.
     2.  I created a modular solution whereby I created a function whose purpose was to input a number and output the sum of the digits of that number. Then I ran a while loop until the num//10 == 0 as that would mean that `num` is a number with one digit.
 31. https://leetcode.com/problems/score-of-a-string/submissions/1643047539/
     1.  Given a string, calculate the difference of the ASCII values of adjacent characters
     2.  Use `ord` to get the ASCII value of a character in Python
     3.  To get the absolute value of any number, use `abs()` instead of `math.abs()`.
 32. https://leetcode.com/problems/richest-customer-wealth/description/
     1.  Return the max of the row wise sum of a mxn matrix
 33. https://leetcode.com/problems/merge-strings-alternately/description/
     1.  Given two strings `s1 = "abc"` and `s2 = "pqr"`, merge them alternatively i.e. `"apbqcr"`
        - To solve:
          - Check which word has the least length
          - Run a for loop and add the characters till that least length i.e. do `merged_str = merged_str + word1[i] + word2[i]`
          - Then for the string that's longer (if that's even a case), add all the characters from len(shorter_str) to len(longer_word). Checkout my solution here for better context.
34. https://leetcode.com/problems/fizz-buzz/description/
    1.  Classic FizzBuzz. Need I say more?
35. https://leetcode.com/problems/convert-the-temperature/description/
    1.  Really basic temperature conversion problem. Kind of shocked how LeetCode has this up on their website.
36. https://leetcode.com/problems/first-unique-character-in-a-string/description/
    1.  I iterate over the string. I push each character into a list. If a character is already in the list, I set it to False in a corresponding dictionary.
    2.  Then I iterate over the string again and return the index of the first character that is True in the dictionary.
    3.  It's a bit slow. I'm sure there's a better way to do this.
37. https://leetcode.com/problems/sum-multiples/description/
    1.  Variant of FizzBuzz. First check if a number is divisible by 3, 5 or 7. If it is, add it to the sum. Then check if its divisible by both (3 and 5) or (3 and 7 [i didn't do this]) or (5 and 7). If it is, add it to the sum. Then check if its divisible each of the three. If it is, add it to the sum.
    2.  Prevents overcounting i.e. Whereby you'd count a number twice if it's divisible by both 3 and 5.
38. https://leetcode.com/problems/find-closest-person/description/
    1.  Really simple problem. 3 people. X, Y and Z. X and Y move towards Z at the same speed. It is our job to find out who will reach Z first. This can be simply solved by taking the difference.
39. https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/
    1.  Loop over each sentence in the list sentences. use `.split()` to get all the words and `len()` to get the number of words and then do a simple max_words `if` statement. Really easy problem.
    
40. [STRING] https://leetcode.com/problems/student-attendance-record-i/description/
    1.  Loop over the string. 
        1.  First count the number of `A`s using a dictionary. If this count is ever `>=2` directly return `False` within the loop itself. 
        2.  Now we need to find a way to track if the string has 3 or more consecutive `L`. To do this, I use a variable called `late_consec`. Whenever the loop encounters a `L` this is incremented by 1. However, if the loop encounters a different letter i.e. a `P` or a `A`, then `late_consec` is reset to zero. This ensures that the only way `late_consec` can be more than 3 is if the loop encounters 3 or more `L`s consecutively thereby making it impossible for the counter to be rest by any other the other if conditions.
        3. Within the if condition for the character `L` check if the counter is `>=3` or not. If it is, then return `False` immediately, else keep on going.

I've solved 40 problems (atleast) that's how many I've recorded in this repository. I will now transition to doing more structured practice. So I asked `o3` to give me a plan and it gave me this link: https://dev.to/dfs_with_memo/leetcode-warmup-problems-13o7. I will now use this list and try to solve problems using it. I will also try to tag my problems from now on.

41. [LINKED LIST] https://leetcode.com/problems/middle-of-the-linked-list/
    1.  First get the length of the Linked List.
    2.  Then calculate the middle index based on whether the length of the list is positive or negative.
    3.  Then, traverse through the LL and keep a track of the number of the nodes you're visiting. The moment you hit the middle node (based on the index that was calculated earlier) save the reference of that node and break the loop.
    4.  Return this reference. ([code](./leetcode-problems/lc_876_Middle_Of_LL.py))
42. [ARRAY] https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
    1.  Longest Continuous Increasing Sub Sequence
    2.  For each element of the array, I go forward as long as the previous element (prev) is lesser than the next one. If it isn't then, I append the length of the increasing sequence to a list.
    3.  Sometimes, the list is already sorted in ascending order, so prev is never more than the next. And hence, no value is appended to my list. That's why, I use a flag variable to check if a length was ever appended to my list. If it wasn't then when I come out of the `j` or nested loop, I append the length anyways. Each time the length is reset.
    4.  This is O(n^2) and pretty slow, but it gets the job done!
43. [STRINGS] https://leetcode.com/problems/find-the-difference/?envType=study-plan-v2&envId=programming-skills
    1.  two strings, `s` and `t`. `t` has one extra character that `s` does not have.
    2.  Goal: Print out this extra character.
    3.  Solution: Loop through `t`. Check if that character exists in `s`. If it does, remove it from `s`. The first character you find that does not exists in s, is your correct answer.
        1.  Note: removal from s is important due to the case of `s='a'` and `t='aa'`


### LeetCode (Neetcode.io):

1. [ARRAY] https://leetcode.com/problems/contains-duplicate/description/
    1.  This is the first problem on [Neetcode's roadmap](https://neetcode.io/roadmap).
    2. Return `True` if the Array has duplicate elements, else return `False`.
    3. Initially I tried to keep a list called `app`. As I iterated through the array I checked if that particular element was already in `app` or not. If it was already present in `app` I returned `True` as that meant I'd seen the number before and the array did indeed contain duplicate elements. If the number wasn't present in `app` I appended it to `app` and continued with life.
    4. However doing the above led to a `Timeout` error. So I asked GPT to guide me to the right solution using the [Socratic Method](https://en.wikipedia.org/wiki/Socratic_method) and it asked me to find a more efficient data structure for the `app` list which is a Set. So I changed `app = []` to `app = set()` and found that I solved the problem!
    5. Solution [here](leetcode-problems/lc_217_contains_duplicates.py)
    6. NeetCode's solution: [YouTube](https://www.youtube.com/watch?v=3OamzN90kPg&ab_channel=NeetCode), [Text](https://neetcode.io/solutions/contains-duplicate)
 2. [ARRAY] https://leetcode.com/problems/valid-anagram/
    1. Given two strings `s` and `t` check if they are [anagrams](https://en.wikipedia.org/wiki/Anagram).
    2. I created a list of all the letters in `t`.
    3. For each character of `s` if it was present in `t_chars` I removed that from the `t_chars` list.
    4. At the end of the loop, if `len(t_chars)==0` I returned `True`, else I returned `False`.





### CodeForces:
1. https://codeforces.com/problemset/problem/4/A [Watermelon] (15 Apr 2025)
   1. Essentially check if a number is even and greater than 2 so that it can be split into two even numbers. 
2. https://codeforces.com/problemset/problem/71/A [Way Too Long Words]
   1. Essentially get the length of a string and if the length of the string is more than 10 then replace it with 
3. https://codeforces.com/problemset/problem/231/A [Team]
   1. Count the number of 1's in a bit string. Count if it's more than 2.
4. https://codeforces.com/problemset/problem/282/A [Bit++]
   1. See if the string '++' is in the string and update a variable accordingly.






## Things I've Learnt:

1. In Pandas, to modify the columns `.astype('int')` or something is used in general.
2. In Pandas, to rename a column, you have to pass a dictionary of the `{'old_col_name': 'new_col_name'}` to the `.rename()` function.
3. In SQL, to use the WHERE clause these two links might be helpful to refresh your memory of the Syntax ([here](https://five.co/blog/sql-multiple-where-clauses/#:~:text=%27New%20York%27%3B-,Combining%20Multiple%20WHERE%20Clauses,Using%20OR%20operator), [here](https://www.w3schools.com/sql/sql_where.asp))
4. If you want to get the unique values from a column in SQL use the `DISTINCT` keyword. For example, `SELECT DISTINCT column_name FROM table_name;` ([here](https://www.w3schools.com/sql/sql_distinct.asp))
5. To read numbers in Bash you use `read` command. For example, `read a` will read a number and store it in the variable `a`.
6. To do arithmetic expressions in Bash using the values of variables use the `$(())` sign. For example, `echo $((a+b))` will print the sum of `a` and `b`.
7. In Pandas if you have a column say `email` in a DataFrame, say, `customers` and you want to get the drop the rows where a duplicate value occurs then use `customers.drop_duplicates(subset=['email'])`. This will drop the rows where the `email` column has duplicate values. ([Nice article](https://medium.com/@robertsevan/leetcode-problem-2882-drop-duplicate-rows-leetcode-introduction-to-pandas-70e8a5298e40))
8. `sorted()` in Python returns a list whereas `.sort()` just does the sort inplace on the list. So, `a=sorted(list)` makes sense but `b=l.sort()` will yield `None` for `b`.
   





Starting to maintain a table from now on.

| SNo | Date | Day | Name of Problem | Platform | Description for how I solved it | What I learnt | Code |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2025-06-18 (18th June 2025) | Wednesday | Find the Index of the First Occurrence in a String | Leetcode #28 | I slid a window across the haystack. I check character wise if the needle is equal to the haystack or not. If it is, I continue to increment a counter. The moment the counter == length of the needle that means I’ve found len(needle) number of characters in the haystack that exactly equal the characters in the haystack. To calculate the first index, I reasoned, I am starting from some index i of the haystack and I checking in front of index i by len(needle). So to get the first index, it is natural to subtract i+j (the last index where I got the total equality from len(needle)-1. | How do do this sliding window thing | [Link](./leetcode-problems/lc_28_idx_first_occuring_string.py) |
| 2 | 2025-06-19 (19th June 2025) | Thursday | Minimum Number Game | Leetcode #2974 | Really simple problem. Until the given array is empty, let alice remove the min element from the list and then let bob remove the next min element etc. and append bob’s min element to the new list `arr` and then append alice’s min element to the aforementioned array `arr`. | How to loop over a list and do “append” | [Link](./leetcode-problems/lc_2974_min_num_game.py) |
| 3 | 2025-06-22 (22nd June 2025) | Sunday | Check if the Sentence Is Pangram | LeetCode       #1832 | Check if a string contains all the letters of the English alphabet. How? Create a str called “alphabet_str” with all the alphabet. Loop over that string. Now for each letter of the alphabet check if the “input_str” contains that character or not. If not, immediately return False (no point searching anymore). Else, continue onwards. | How to loop and define a string (basic). Really basic stuff which I knew already but Oh well… | [Link](./leetcode-problems/lc_1832_Check__Sentence_Is_Pangram.py) |
| 4 | 2025-06-23 (23rd June 2025) | Monday | Count the Digits That Divide a Number | LeetCode #2520 | Extract the digits in a number and then check if those digits actually divide the number fully. If the number is `121` the extracted digits are `[1,2,1]` and `1` divides `121` hence we return `2` as two of the digits in `121` divide the number 121 perfectly | How to do basic looping stuff | [Link](./leetcode-problems/lc_2520_Count_Digits_that_Divide_a_Number.py) |
|  |  |  |  |  |  |  |  |