# Documentation
**Goal and Basic Structure**

For this project, I was tasked with the objective of coding a program that extracts different features from a document of potential allosteric sites of a specific protein. The goal was to convert a .txt file of a list of pockets and their attributes into a 2D array. This allows for easier access of the protein data later in the project. My script reads in the .txt file and then splits the data using the delimiter ":". Each value is then added into the 2D array. The data in the array is then cleaned up, with formatting elements such as "\t" and "\n" being removed, resulting in the finalized array.

**Accomplishments**

Over the course of this project, I have created:
* Code to extract features from a .txt file into a usable array of data
* Testing code to raise warnings when expected values do not match
* Documentation of the code

**How to Run**

* The code can be tested through the test.py folder
* This tests the beginning and end of the resultant array against the expected values :)
