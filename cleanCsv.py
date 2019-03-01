#!/usr/bin/env python
#!-*- CODING:UTF-8 -*-
from argparse import ArgumentParser
from pathlib import Path
import os
import csv
import string

# TODO:
# - Insert first line with column names
# - Add options to delete single columns (readedFile will become 2d array instead of list of strings)

def main():
	inputFile=Path.cwd()
	outputFile=Path.cwd()
	parser = ArgumentParser()
	parser.add_argument("-i", "--input", dest="inputFile", help="open CASSY txt file", metavar="FILE")
	parser.add_argument("-o", "--output", dest="outputFile", help="output file")

	args = parser.parse_args()

	inputFile=inputFile / args.inputFile

	outputFileName = args.outputFile if args.outputFile else args.inputFile
	outputFileName =checkCsvExtension(outputFileName)
	outputFile = outputFile / outputFileName

	readedFile = removeFirstLines(str(inputFile))

	readedFile = replaceCommaAndDel(readedFile)
	#print(readedFile)
	writeNewFile(readedFile,str(outputFile))
 
def removeFirstLines(fileName):

	with open(fileName,'r', encoding = "ISO-8859-1") as inputFileStream:
		fileLines = inputFileStream.readlines()
		if not fileLines:
			print('Error: Input file is empty\nExiting...')
			exit(0)
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
		if newLine[len(newLine)-2] == ',':
			newLine = newLine[:len(newLine)-2]+newLine[len(newLine)-1:]
		if newLine[len(newLine)-1] == ',':
			newLine = newLine[:len(newLine)-1]
		newFile.append(newLine)
	return newFile

def writeNewFile(readedFileList, outputFileName):
	with open(outputFileName,'w') as outputFile:
		outputFile.seek(0)
		for row in readedFileList:
			outputFile.write(row)
	
def checkCsvExtension(fileName):
	newFileName=str()
	sFileName = fileName.split('.')
	fileNameLen=len(sFileName)
	if fileNameLen > 2:
		print('Output filename error\nExiting...')
		exit(0)
	newFileName = sFileName[0] + '.csv'
	return newFileName
	
if __name__ == "__main__":
	main()
