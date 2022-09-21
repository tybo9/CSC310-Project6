# CSC310-Project6
Assignment 6 
 
 
When to Submit 
Due: 11:59pm, 12/21/2020 
 
What to Submit 
   Please prepare a PDF file to include your answers to each question. Please also prepare 
ONE ha6.py file to include all your codes (if applicable) – clearly comment the corresponding 
questions.  
 
How to Submit 
  Submit your PDF file and ha6.py file using the Canvas.  
 
The goal of this collection of assignment is to help you review (i)  maps; (ii) search tree; (iii) 
sorting.  
 
*The first two questions require you to provide drawings. You might manually draw and upload 
a photograph of your drawings; or directly draw your answers using PowerPoint. Either way, 
include pictures of your drawings in your PDF file.  
 
 
1. Draw the 9-entry hash table that results from using the hash function, h(i) = (i+1) mod 10, to 
hash the keys 2, 3, 24, 12, 13, 23, 11, 20, and 5, assuming collisions are handled by chaining.  A 
sample drawing can be found in the page 30 of Lecture 9, e.g., 
  
  
2.  The data structure for Binary search tree includes three major operations: search, insert, and 
delete. With an empty binary search tree, insert entries with keys 30, 35, 29, 60, 44, 22 (in this 
order). Draw the binary search tree after each insertion.  
 
 
3. Suppose a n-element sequence S is used to store votes for president candidates.  Each element 
of S is an integer (ID) representing a particular candidate. E.g., S=[10, 874, 10, 874, 92, 384, 
92, ...]. Every candidate has a UNIQUE ID. The number of candidates is UNKNOWN and thus 
each ID might be arbitrarily large. The number of votes n is also not given and the sequence 
could be arbitrarily large. Please Design and Develop a Python function of time-complexity 
O(nLogn) that takes S as its argument and return the candidate’s ID who won the election.  
(Tips: you might sort the sequence first using an O(nlogn) sorting method and then cast the 
votes). 
