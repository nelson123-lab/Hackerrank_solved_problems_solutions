filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
final_file=[]
for element in filenames:
    if element.endswith(".hpp"):
        final_file.append(element.replace(".hpp",".h"))
    else:
        final_file.append(element)
print(final_file)

# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
"""
# longer method
new_filename=[]
new_list=[]
final_file=[]
for element in filenames:
    if element.endswith("p"):
        new_filename.append(element)
for element1 in new_filename:
    new_list.append(element1.split("pp")[0])
for element3 in filenames:
    if not element3.endswith("p"):
        final_file.append(element3)
final_file[1:1] =new_list
print(final_file)
"""
