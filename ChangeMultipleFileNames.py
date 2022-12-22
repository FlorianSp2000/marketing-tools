import os
dir_path = os.path.dirname(os.path.realpath(__file__))
for file_name in os.listdir(dir_path):
    new_file_name = file_name.replace("IMG","Riley")
    source = os.path.join(dir_path,file_name)
    destination = os.path.join(dir_path,new_file_name)
    os.rename(source, destination)