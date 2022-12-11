import glob

csv_files = glob.glob("PetClinicdata/*.csv")


for filename in csv_files:
    print("Putting %s" % filename.split("\\")[1])
    # print(filename.split("\\")[1])
    
