import glob

csv_files = glob.glob("PetClinicdata/*.csv")


for filename in csv_files:
    # print("Putting %s" % filename.split("\\")[1]) # for window
    print("Putting %s" % filename.split("/")[1]) # for linux
    # print(filename.split("\\")[1])
    # print(filename)
    
nums = [i for i in range(1, 6)]
## passsing list using the * (use for unpack list)
print(*nums)
print(nums)
