#!python3

import re
from os import walk
from os import getcwd
from os import path
import logging
import csv

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

currentDir = getcwd()

INPUT_DIRECTORY = 'originals/'
OUTPUT_DIRECTORY = 'processed/'
MAP_DIRECTORY = 'map/'

GID_PATH = path.join(currentDir, MAP_DIRECTORY, 'gid-path.csv')
PID_NAME = path.join(currentDir, MAP_DIRECTORY, 'pid-name.csv')
PID_GID = path.join(currentDir, MAP_DIRECTORY, 'pid-gid.csv')
POSTID_NAME = path.join(currentDir, MAP_DIRECTORY, 'postid-name.csv')
POSTID_PPATH = path.join(currentDir, MAP_DIRECTORY, 'postid-ppath.csv')

galleryPattern = re.compile('([\\\|\[]*)(imagebrowser\s\w+=|nggallery\s\w+=)(\d+)([\\\|\]]*)')
photoPattern = re.compile('([\\\|\[]*)(singlepic\s\w+=)(\d+)(.*)([\\\|\]]*)')

outputDir = path.join(currentDir, OUTPUT_DIRECTORY)
filesInDir = [f for p, d, f in walk(path.join(currentDir, INPUT_DIRECTORY))]


def load_map(csvFile):
    mapping = {}
    with open(csvFile, newline='') as tmp:
        csvReader = csv.reader(tmp, delimiter=',', quotechar='"')
        for row in csvReader:
            break

        for row in csvReader:
            mapping[row[0]] = row[1].replace('wp-content/gallery', '{photo}')
    print(mapping)

    return mapping


def join_photo_path(gidPath, pidName, pidGid):
    photoMapPath = {}
    for k, v in pidGid.items():
        photoMapPath[k] = gidPath[v] + '/' + pidName[k]

    return photoMapPath


def find_and_replace(fContent, pattern, mapping):

    findings = re.findall(pattern, fContent)
    patterns = {''.join(f): f[2] for f in findings}
    elements = []
    if patterns:
        for k, v in patterns.items():
            fContent = fContent.replace(k, mapping[v])
            elements.append(mapping[v])

    return elements, fContent


def enrich_meta(fContent, elements, mdType):
    metadata = '\n' + mdType + ': ' + ', '.join(elements) + '\n\n'
    fContent = re.sub('(?!\w+:\s.+)(\n\n)', metadata, fContent, 1)

    return fContent


if __name__ == '__main__':

    gidPath = load_map(GID_PATH)

    # find photo path
    pidName = load_map(PID_NAME)
    pidGid = load_map(PID_GID)
    photoMapPath = join_photo_path(gidPath, pidName, pidGid)

    # find post's photo path
    pidName = load_map(PID_NAME)
    pidGid = load_map(PID_GID)
    pPath = join_photo_path(gidPath, pidName, pidGid)

    # link posts to photos
    postidPpath = load_map(POSTID_PPATH)
    postidName = load_map(POSTID_NAME)
    postPpath = {}

    for k, v in postidPpath.items():
        print(k, v)
        try:
            if '.jpg' in postidPpath[k]:
                postPpath[postidName[k]] = v
                print(postidName[k], v)
        except KeyError as e:
            print('Error: ', e)

    # for k, v in postPpath.items():
    #     print(k, v)

    print(len(postPpath))

    for f in filesInDir[0]:
        with open(path.join(currentDir, INPUT_DIRECTORY, f), 'r') as tmp, open(path.join(outputDir, f), 'w+') as out:
            fContent = tmp.read()

            trash, fContent = find_and_replace(fContent, photoPattern, photoMapPath)

            elements, fContent = find_and_replace(fContent, galleryPattern, gidPath)
            if elements:
                fContent = enrich_meta(fContent, elements, 'Gallery')

            # change Category to NZ - category to trange
            try:
                categories = re.search('(?<=Category:\s)(.+)', fContent).groups()[0].split(', ')
                fContent = re.sub('(?<=Category:\s)(.+)', 'New Zealand', fContent, 1)
                if categories:
                    fContent = enrich_meta(fContent, categories, 'Tags')
            except AttributeError as e:
                print('Error:  ', e)
            # post image
            title = re.search('(?<=Title:\s)(.+)', fContent).groups()[0]

            try:
                postImage = [postPpath[title].replace('http://www.voyage-nz.org/wp-content', '{photo}')]
                if postImage:
                    fContent = enrich_meta(fContent, postImage, 'Image')
            except KeyError as e:
                print('Error: ', e)

            out.write(fContent)
