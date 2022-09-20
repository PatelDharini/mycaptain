#program to find extension of file
file_name = input("Input the Filename: ")
extns = file_name.split(".")
extension=repr(extns[-1])
if extension==repr(extns[-1]):
    print('The extension for the filename is:"python"')
else:
    print(extension)

