Problem_1  ->
In this problem i used a doubly linked list with a dictionary as a hash map to get the element present in it in O(1) time complexity.
Time complexity-
In this problem overall time complexity is O(1) as all the function used for adding , removing and getting the element are having worst time complexity of O(1)
# here I am only considering the cases of functions that are used.
space complexity-
In this problem the space complexity is O(capacity) as we are having the total number of nodes in liked list one more than the capacity and after that we remove that too, but we are also using the dictionary but the overall space complexity is O(n) where n is n is the capacity.capacity


Problem_2  ->
In this problem I used recursion to iterate in the directory.
space complexity-
In this problem we are storing all the files in the directory in a list so the space complexity to store it in worst case is O(n) where n is the total number of files and subfolder in the whole folder and subfolder and this the case of having a empty string as a suffix
and we also need some auxillary space for stack to store the recursive call and this is O(n) where n is the maximum number of subdirectory in the directory in the worst case, and the worst case will be in the situation if all the subdirectory are in a single directory

time complexity-
In this Problem we we are iterating in the whole directory and time complexity for iteration is O(n) where n is total number of files and folder in it.
and then we are searching for suffix in each file and folder so time complexity for searching the suffix in the string is O(m*l) in worst case where l is length of suffix and m is length of file or folder path , So the overall time complexity for iteration and searching for the suffix is O(n*m*l).
and the time complexity for iterating and checking for subdirectory as well as the time complexity for recursion is less then O(n*m*l)



Problem_3  ->
In this problem we are using a tree to store the data according to the frequency of it.

space complexity-
In creating a tree we needs O(n) space and also it decoding we are storing the string and it will take a space of O(n) so its overall space complexity is O(n)

time complexity-
In this problem we are creating the tree and in creating it on the basis of character frequency we have time complexity of O(nlogn) and in the decoding part we are having a external loop and then we are searching for a character by getchar  it will take time of O(logn) for searching it so its complexity is O(nlogn)
so its overall time complexity is O(nlogn)




Problem_4  ->
In this problem first we traverse the list of users in the Group class if the user is present in it then we return True otherwise we will check in each group in the groups list and if the user is in any users list then we will return True else return False
 
time complexity-
we are having a users list and if we do not find the required user in it then we have to check it in the each group of groups list and if there are n group in the groups list and again it is having l number of user in its users list(taking the worst case possible) 
so the time complexity will be O(n*l) but generally we do not have every group in groups list with l users so we can neglect this case and in approximation the time complexity will be O(n)

space complexity-
if we do not take the case of inserting the data in group and user list the space complexity is O(1)
but if we consider this case then the space complexity will be O(n*l) where n is number of element in groups list and l is the number of elements in the users list.



Problem_5  ->
In this problem we made a blockchian contains timestrap,data,previous node data,its current hash and next node

Space complexity-
Here if we are having n blocks in the block chain the the total space needed is O(n*5) which we will treat as O(n).

Time complexity-
In adding the new block we have to traverse the blockchain and at last we have to add our next block so it will take O(n) time and similarly for printing the block it will also take O(n) time
So its overall time complexity is O(n) 
   
   

Problem_6  ->
In this Problem in union function we create a set and storing the elements of the first linked list and then elements of second linked list in this and finally creating a new liked list having elements of set and return this linked list as the union.
And in intersection fuction we store the elements of the first linked list in it and then iterating in second linked list and append the element in ll linked list if element is present in the set a and delete the element from the set for not taking the repetation of a number.

Space complexity-
Extra space is used to store elements in the set and to store the elements in the linked list so in wrost case space complexity is O(n+m) where n is the number of element in first linked list and m is the number of elements in the second linkef list and in worst case there is no common elements in both the linked list

Time complexity-
In union as we are iterating through the linked list and inserting the element in set so its time complexity is O(n) , where n is number of nodes in linked list (in this case i am cosidering the insertion operation of set in O(1))
but in intersection we are iterating through second list and searching a element in the set so the time complexity is O(n)(time complexity for searching in set is O(1)) in worst case where n is total number of the elemets in the linked list and in worst case all elements in both linked list matches.
