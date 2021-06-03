import os
import requests
import random
import shutil

url_path = 'urls/'
new_path = 'NSFW_Images/train'
if not os.path.exists(new_path):
    os.makedirs(new_path)
image_extensions = ['jpg','jpeg','png']

def downloader():
    for file_name in os.listdir(url_path):
        image_loc = new_path+'/'+file_name.split('.txt')[0]
        if not os.path.exists(image_loc):
            os.makedirs(image_loc)

        with open(url_path+file_name,'r') as f:
            for line in f:
                line = line.strip()
                image_name = line.split('/')[-1]
                try:
                    if image_name.split('.')[-1] in image_extensions:
                        print('Downloading {} ... '.format(image_name))
                        f = open(image_loc+'/'+image_name,'wb')
                        f.write(requests.get(line).content)
                        f.close()
                except Exception as e:
                    pass


def create_tarining_dataset():
    source = 'NSFW_Images/train'
    destination = 'NSFW_Images/test'
    if not os.path.exists(destination):
        print('Creating Test Directory')
        os.makedirs(destination)
    for f in os.listdir(source):
        if f[0] == '.':
            continue
        print('source folder  ',f)
        dest = destination+'/'+f
        if not os.path.exists(dest):
            os.makedirs(dest)
        files = os.listdir(source+'/'+f)
        no_of_files = len(files) // 5

        for file_name in random.sample(files, no_of_files):
            shutil.move(os.path.join(source+'/'+f, file_name), dest)

def main():
    print('-----Starting Downloader-----')
    downloader()
    print('---downloaded all the required files----')
    print('\n\n --- Starting the splitter ---\n\n')
    create_tarining_dataset()
    print('-----Ending the execution, required directories created -----')

if __name__ == '__main__':
    main()