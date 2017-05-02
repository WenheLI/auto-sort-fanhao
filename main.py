import os
import re
import shutil


class Car:
    def __init__(self):
        self.features = re.compile('[a-z]+-+[0-9]+', flags=re.I)

    def get_file(self):

        if not os.path.isfile('address_source.txt'):
            address_source = input('input the source address')
            file1 = open('address_source.txt', 'w')
            file1.write(address_source)
            file1.close()
        else:
            file1 = open('address_source.txt', 'r')
            address_source = file1.read()
            file1.close()
        if not os.path.isfile('address_target.txt'):
            address_target = input('input the target address')
            file1 = open('address_target.txt', 'w')
            file1.write(address_target)
            file1.close()
        else:
            file1 = open('address_target.txt', 'r')
            address_target = file1.read()
            file1.close()

        os.chdir(address_source)
        if not os.path.exists(address_target):
            os.mkdir(address_target)
        for file_name in os.listdir(address_source):
            if self.features.match(file_name):
                if os.path.exists(address_target + '/' + file_name[:file_name.find('-')]):
                    shutil.move(file_name, address_target + '/' + file_name[:file_name.find('-')])
                else:
                    os.mkdir(address_target + '/' + file_name[:file_name.find('-')])
                    shutil.move(file_name, address_target + '/' + file_name[:file_name.find('-')])
        os.chdir(address_target)
        dirs = os.walk(address_target)
        for add, dir, files in dirs:
            for one in dir:
                for _add, _dir, file in os.walk(one):
                    if len(file) <= 3:
                        for name in file:
                            shutil.move(_add + '/' + name, address_target)
                        os.rmdir(_add)


car = Car()
car.get_file()