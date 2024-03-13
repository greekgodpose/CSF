#initialising empty lists, set, and dictionary
Books_list=[]
Authors_set=set()
Book_dict={}

#Add books
Books_list.append("Python programming")
Authors_set.add("John Smith")
Book_dict["Python programming"]

Books_list.append("Data Structures and Algorithms")
Authors_set.add("Jane doe")
Book_dict["Data Structures and Algorithms"]="Jane Doe"
Books_list.append("Machine Learning Basics")
Authors_set.add("Alice Johnson")
Book_dict["Machine Learning Basics"]

#Search for books
Search_title= input("Enter the title:")
if Search_title in Books_list:
    print("Bookfound Author: (Book_dict(Search Search_title)")