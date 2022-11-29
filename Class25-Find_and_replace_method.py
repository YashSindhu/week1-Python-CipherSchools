string = "She is beautiful and is a good dancer"
print(string.replace(" ","_"))
# it gives --> She_is_beautiful_and_is_a_good_dancer
print(string.replace("is","was"))
# it gives --> she was beautiful and was a good dancer
print(string.replace("is","was",1))
# it gives --> she was beautiful and is a good dancer


print(string.find("beautiful"))
#it gives --> 7