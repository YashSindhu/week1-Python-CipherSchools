# Ask a user for name:-
# Ex - Yash Sindhu
# print count of each words
# output:
#      Y : 1
#      a : 1
#      s : 1
#      h : 2
#        : 1
#      S : 1
#      i : 1
#      n : 1
#      d : 1
#      u : 1


# SOLUTION:-
  
name = input("enter your name")
i = 0
temp_var = "0"
while i < len(name):
    if temp_var not in name:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1