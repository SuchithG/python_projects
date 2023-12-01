f = open('sample.txt', 'w+')

f.write("Python is awesome\n")
f.writelines(["Python\n","Django\n","DRF\n"]) # writes a list in new line in list