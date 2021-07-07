import os

def image_converter():
    i = 0
    path = "C:/Users/User/Desktop/BulkImage/"
    for filename in os.listdir(path):
        my_dest = "image" + str(i) + ".jpg"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == '__main__':
    image_converter()
