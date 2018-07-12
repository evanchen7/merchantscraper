#!/usr/bin/env python3
import glob, os, datetime, time, regex

class LocalFilesCompetitionChecker:
    def __init__(self, pathToFolder, fileType, targetWords, merchantName = 'concantenated'):
        if type(pathToFolder) != str and type(fileType) != str or type(targetWords) != list:
            raise TypeError('(pathToFolder, keywords, targetWords, merchantName) need to be (str, list, int, boolean)')
        self.pathToFolder = pathToFolder
        self.fileType = fileType
        self.targetWords = targetWords
        self.merchantName = merchantName

    def grabAllFiles(self):

        patterns = self.regexGenerator()
        all_files_with_extension = list()
        allFolders = glob.iglob('{}/**/*{}'.format(self.pathToFolder, self.fileType), recursive=True)

        with open("{}/{}.txt".format(self.pathToFolder, self.merchantName),'a+') as outfile:
            outfile.write("\n-----BEGIN LOGS-----\n{}\n\n".format(self.getTimeStamp()))
            for filename in allFolders:
                splitFileName = os.path.normpath(filename).split(os.path.sep)
                with open(filename, errors='ignore') as infile:
                    for index, line in list(enumerate(infile)):
                        if patterns.findall(line):
                            try:
                                print('filename: {} -----'.format(splitFileName[-1]), int(index))
                                print(line)
                                outfile.write(str(splitFileName[-2]) + '/' + str(splitFileName[-1]) + ' Line:' + str(index))
                                outfile.write(str(line) + '\n')
                            except:
                                print('Outfile Error')
                                pass
            outfile.write("\nTotal file count: {}".format(self.countFiles()))
            outfile.write("\n{}\n-----END LOGS-----\n\n".format(self.getTimeStamp()))

    def stichAll(self, fileTypes):
        files_extension = fileTypes
        all_files_with_extension = list()
        for files in files_extension:
            try:
                all_files_with_extension.extend(glob.iglob('{}/**/*{}'.format(self.pathToFolder, files), recursive=True))
            except:
                print('Error in stitchAll')
        print(all_files_with_extension)

    def countFiles(self):
        cpt = sum([len(files) for r, d, files in os.walk(self.pathToFolder)])
        return cpt

    def regexGenerator(self):
        patterns = [(("(?i){}*".format(x))) for x in self.targetWords]
        return regex.compile('|'.join(patterns), regex.IGNORECASE)

    def getTimeStamp(self):
        localtime = time.asctime(time.localtime(time.time()))
        return localtime

if __name__ == "__main__":
    try:

        start = time.time()

        path = '/Users/evanchen/Downloads/theme_export__www-amarilojewelry-com-icon-afterpay-edits__09JUL2018-0502pm'
        fileType = ['.liquid']
        keywords = ['sezzle']
        name = 'Amarilo'

        test = LocalFilesCompetitionChecker(path, fileType, keywords, name)
        test.grabAllFiles()
        # stichAll(path, ['.liquid', '.png'], name)
        end = time.time()

    finally:
        print('{} took {} seconds to run'.format(__name__, time.time() - start))
