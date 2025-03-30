## DSA

I will be documenting my learning journey in Data Structures and Algorithms here. I will be using C++ / Python / Java for this purpose.

I am trying to follow [Striver's A2Z DSA Course/Sheet](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2). It's extremely organised, starts from the fundamentals and goes on to advanced topics. I will be following this course and also supplementing it with other resources like [GeeksforGeeks](https://www.geeksforgeeks.org/) and [LeetCode](https://leetcode.com/).

I hope to make a commit everyday as I learn one new thing everyday. I will be taking notes in Markdown and also include C++ files where necessary.

I hope that this *public contract* will keep me accountable and help me stay consistent in my learning.




<summary>Problems I've solved</summary>


Hackerrank:
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


Leetcode:
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




## Things I've Learnt:

1. In Pandas, to modify the columns `.astype('int')` or something is used in general.
2. In Pandas, to rename a column, you have to pass a dictionary of the `{'old_col_name': 'new_col_name'}` to the `.rename()` function.
3. In SQL, to use the WHERE clause these two links might be helpful to refresh your memory of the Syntax ([here](https://five.co/blog/sql-multiple-where-clauses/#:~:text=%27New%20York%27%3B-,Combining%20Multiple%20WHERE%20Clauses,Using%20OR%20operator), [here](https://www.w3schools.com/sql/sql_where.asp))
4. If you want to get the unique values from a column in SQL use the `DISTINCT` keyword. For example, `SELECT DISTINCT column_name FROM table_name;` ([here](https://www.w3schools.com/sql/sql_distinct.asp))
5. To read numbers in Bash you use `read` command. For example, `read a` will read a number and store it in the variable `a`.
6. To do arithmetic expressions in Bash using the values of variables use the `$(())` sign. For example, `echo $((a+b))` will print the sum of `a` and `b`.
7. In Pandas if you have a column say `email` in a DataFrame, say, `customers` and you want to get the drop the rows where a duplicate value occurs then use `customers.drop_duplicates(subset=['email'])`. This will drop the rows where the `email` column has duplicate values. ([here](https://medium.com/@robertsevan/leetcode-problem-2882-drop-duplicate-rows-leetcode-introduction-to-pandas-70e8a5298e40))
   



