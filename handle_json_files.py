import json

student_info = {
    "id" : 12,
    "name" : "Josh",
    "address" : "Dubai, UAE"
}

# with open('studentinfo.json', 'w') as file:
#     json.dump(student_info, file, indent=2)

# read a json file

with open('studentinfo.json', 'r') as file:
    student_details = json.load(file)


student_details["dob"] = "26 Sept 2005"

print(student_details)

with open('studentinfo.json', 'w') as file:
    json.dump(student_details, file, indent=2)