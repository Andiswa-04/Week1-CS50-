user_file = input("File name:").strip().lower()

#Learnt that match arent use for boolean expressions 

# match user_file:
#     case user_file.endswith("gif"):
#         print("image/gif")
#     case user_file.endswith("jpg") | user_file.endswith(".jpeg") :
#         print("image/jpeg")
#     case user_file.endswith("png"):
#         print("image/png")
#     case user_file.endswith("pdf"):
#         print("application/pdf")
#     case user_file.endswith("txt"):
#         print("text/plain")
#     case user_file.endswith("zip"):
#         print("application/zip")
#     case user_file.endswith("mp4"):
#         print("video/mp4")
#     case _ :
#         print("application/octet-stream")

if user_file.endswith(".gif"):
    print("image/gif")
elif user_file.endswith(".jpg") or user_file.endswith(".jpeg"):
    print("image/jpeg")
elif user_file.endswith(".png"):
    print("image/png")
elif user_file.endswith(".pdf"):
    print("application/pdf")
elif user_file.endswith(".txt"):
    print("text/plain")
elif user_file.endswith(".zip"):
    print("application/zip")
elif user_file.endswith(".mp4"):
    print("video/mp4")
else:
    print("application/octet-stream")
    
    
    