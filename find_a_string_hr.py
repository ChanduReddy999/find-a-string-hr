"""find a string problem using Python (HackerRank)"""

'''method 1'''

# def count_substring(string, sub_string):
#     count=0
#     for i in range(0, len(string)-len(sub_string)+1):
#         if string[i] == sub_string[0]:
#             flag=1
#             for j in range (0, len(sub_string)):
#                 if string[i+j] != sub_string[j]:
#                     flag=0
#                     break
#             if flag==1:
#                 count += 1
#     return count
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#     count = count_substring(string, sub_string)
#     print(count)
    

'''method 2'''

# def count_substring(string, sub_string):
#     count=0
#     string=list(string)
#     new_string=string.copy()
#     new_string=''.join(new_string)
#     for i in range(len(string)):
#         if new_string.startswith(sub_string):
#             count+=1
#             new_string=list(new_string)
#             new_string.pop(0)
#             new_string=''.join(new_string)
#         else:
#             new_string=list(new_string)
#             new_string.pop(0)
#             new_string=''.join(new_string)
#     return count
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#     count = count_substring(string, sub_string)
#     print(count)
