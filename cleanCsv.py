#!/usr/bin/env python
#!-*- CODING:UTF-8 -*-
from argparse import ArgumentParser
from pathlib import Path
import os
import csv
import string

def main():
	inputFile=Path.cwd()
	outputFile=Path.cwd()
	parser = ArgumentParser()
	parser.add_argument("-i", "--input", dest="inputFile", help="open CASSY txt file", metavar="FILE")
	parser.add_argument("-o", "--output", dest="outputFile", help="output file")

	args = parser.parse_args()
	inputFile=inputFile / args.inputFile

	outputFileName = args.outputFile if args.outputFile else args.inputFile
	checkCsvExtension(outputFileName)
	outputFile = outputFile / outputFileName

	readedFile = removeFirstLines(str(inputFile))
	readedFile = replaceCommaAndDel(readedFile)
	writeNewFile(readedFile,str(outputFile))
 
def removeFirstLines(fileName):
	with open(fileName,'r', encoding = "ISO-8859-1") as inputFileStream:
		fileLines = inputFileStream.readlines()
		inputFileStream.seek(0)
		lineCounter=0
		readedFile=list()
		for i in fileLines:
			if lineCounter>4:
				readedFile.append(i)
			lineCounter = lineCounter + 1
	return readedFile
	
def replaceCommaAndDel(stringsToReplace):
	newFile=list()
	for row in stringsToReplace:
		newLine=str()
		newLine = row.replace(',','.')
		newLine = newLine.replace('\t',',')
		newFile.append(newLine)
	print(newFile)	

def writeNewFile(readedFileList, outputFileName):
	with open(outputFileName,'w') as outputFile:
		outputFile.seek(0)
		for row in readedFileList:
			outputFile.write(row)
	
def checkCsvExtension(fileName):
	fileNameLen=len(fileName.split('.'))
	if  fileNameLen == 1 or not fileName.split('.')[2]:
		fileName += 'csv' if '.' in fileName else '.csv'
	elif fileNameLen > 2:
		print('Output filename error\nExiting...')
		exit(0)
	
if __name__ == "__main__":
	main()
