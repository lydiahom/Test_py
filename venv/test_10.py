# filename = '/home/lydia/桌面/py_test/pi_million_digits.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
#
# print(pi_string)
#
# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")

# filename = '/home/lydia/桌面/py_test/learning_py.txt'
# line_all = []
# with open(filename) as file_object:
#     lines = file_object.readlines()
#     #print(lines)
#
#
# completely_content = ''
# for line in lines:
#
#     line = line.replace('python','c')
#     print(line)
#     completely_content += line

"""写入文件"""
# filename = '/home/lydia/桌面/py_test/newfile.txt'
# with open(filename, 'r+') as file_object:
#     file_object.write("i love python22.")


"""写入文件 - 10-5"""
# filename = '/home/lydia/桌面/py_test/newfile.txt'
# while True:
#     user_name = input("Please input your name: ")
#     if user_name == 'q':
#         break
#     greeting = "Welcome come!" + user_name
#     print(greeting)
#     print("Enter 'q' to quit!")
#     reason = input("Why you like programming?")
#     if reason == 'q':
#         break
#     with open(filename, 'a') as file_object:
#         file_object.write(user_name+":" + reason + "\n")


"""10.3.1"""
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

"""10.3.3"""
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("you cannot divide by 0!")
#     else:
#         print(answer)

"""10.3.5"""
# filename = 'alice.txt'
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     print("File is not exist!")

"""10.3.6"""

# title = 'Alice is a girl'
# words = title.split()
# print(words)
# word_num = len(words)
# print(word_num)

# filename = '/home/lydia/桌面/py_test/alice.txt'
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     msg = "Sorry, the file " + filename + " does not exist."
#     print(msg)
# else:
# # 计算文件大致包含多少个单词
#     words = contents.split()
#     num_words = len(words)
#     print("The file " + filename + " has about " + str(num_words) + " words.")

"""10.3.7 使用多个文件"""
# file_1 = '/home/lydia/桌面/py_test/learning_py.txt'
# file_2 = '/home/lydia/桌面/py_test/newfile.txt'
# file_3 = '/home/lydia/桌面/py_test/alice.txt'
#
# def count_words(filename):
#     """计算一个文件大致包含多少个单词"""
#     try:
#         with open(filename) as f_obj:
#             content = f_obj.read()
#     except FileNotFoundError:
#         msg = "Sorry, the file: " + filename + " does not exist."
#         print(msg)
#     else:
#         words = content.split()
#         num_words = len(words)
#         print("The file" + filename + " has about " + str(num_words) + " words.")
#
# files = [file_1,file_2,file_3]
#
# for file in files:
#     count_words(file)


"""10.3.8 失败时一声不吭"""
# file_1 = '/home/lydia/桌面/py_test/learning_py.txt'
# file_2 = '/home/lydia/桌面/py_test/newfile.txt'
# file_3 = '/home/lydia/桌面/py_test/alice1.txt'
#
# def count_words(filename):
#     """计算一个文件大致包含多少个单词"""
#     try:
#         with open(filename) as f_obj:
#             content = f_obj.read()
#     except FileNotFoundError:
#         pass
#     else:
#         words = content.split()
#         num_words = len(words)
#         print("The file" + filename + " has about " + str(num_words) + " words.")
#
# files = [file_1,file_2,file_3]
#
# for file in files:
#     count_words(file)

"""动手试一试"""
#10-6
# while True:
#     num = input("please input an number: ")
#     try:
#         msg = int(num)
#         print(msg)
#     except ValueError:
#         print("Please input an integer.")
#     else:
#         break

#10-10
# line = "Row, row, row your boat"
# count_num = line.lower().count('row')
# print(count_num)

"""10.4.1 使用json.dump()和json.load()"""
# import json
#
# # numbers = [2, 3, 5, 7, 11, 13]
# # filename='/home/lydia/桌面/py_test/numbers.json'
# # with open(filename, 'w') as f_obj:
# #     json.dump(numbers, f_obj)
#
# filename = '/home/lydia/桌面/py_test/numbers.json'
# with open(filename) as f_obj:
#     numbers = json.load(f_obj)
# print(numbers)

"""10.4.2 保存和读取用户生成的数据"""
# import json
# username = input("Please input your name: ")
# filename = '/home/lydia/桌面/py_test/username.json'
# with open(filename, 'w') as f_obj:
#     json.dump(username, f_obj)
#     print("We'll remember you when you come back, " + username + "!")
#
# with open(filename) as f_obj:
#     username = json.load(f_obj)
#     print("Welcome back, " + username + "!")

"""动手试一试"""
#10-11 喜欢的数字
# import json
#
# def fav_num():
#     filename = '/home/lydia/桌面/py_test/like_number.json'
#     try:
#         with open(filename) as f_obj:
#             f_num = json.load(f_obj)
#     except FileNotFoundError:
#         f_num = input("Please input your favorite number: ")
#         with open(filename, 'w') as f_obj:
#             json.dump(f_num, f_obj)
#     else:
#         print("I know your favorite number! It’s " + f_num)
#
# fav_num()