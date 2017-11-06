# addr=["you@mail.com","my@mail.com"]
#
# for email in addr:
#     if "mail" in email:
#         print(email)

# while True:
#     pw=input('your password ? ')
#
#     if pw =="1234":
#         break

names=['Johns','james','jack']
addr=['gmail','hotmail','yahoo']

for i,j in zip(names,addr):
    print(i,j)
