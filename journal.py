#!/usr/bin/python3

import argparse
import time
import os
import shutil
#import StringIO
import csv

entry_count = 0
content = {}

# TODO - 
# add tagged entries
# allow searching by tag(s)
# allow listing all tags

def count_entries():
    print("counting entries")
    with open(fname) as f:
        global content
        content = f.readlines()
    global entry_count
    entry_count = len(content)
    print("found " + str(entry_count) + " items")
    
def backup():
    print("backing up journal file")
    print (fname, "=>", fname_backup)
    shutil.copy (fname, fname_backup)
    if os.path.isfile (fname_backup): print ("success")
    
def list(num_items):
    print("listing entries:")
    with open(fname) as f:
        global content
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    #content = [x.strip() for x in content] 
    #print(content)
    index = 0
    for line in content:
        index += 1
        print(index, line)

def list_n(num_items):
    print("listing last " + str(num_items) + " entries")
    count_entries()
    #with open(fname) as f:
    #    global content
    #    content = f.readlines()
    index = 0
    global content
    for line in content:
        index += 1
        if index > (entry_count - num_items):
            print(index, line)

def list_tags(tags):
    print("listing entries with tags: " + tags)
    #str = StringIO.StringIO(tags)
    reader = csv.reader(tags)#,delimiter=',')
    for row in reader:
        print(row)
        
def add():
    f = open(fname, 'a')
    print (time.strftime("%d/%m/%Y-%H:%M:%S,") + args.add, file=f)        
    
def delete():
    print("deleting entry: " + str(args.delete))
    with open(fname) as f: 
        global content
        content = f.readlines()
    f.close()
    f = open(fname,"w")
    index = 0
    for line in content:
        index += 1
        #print(index, args.delete)
        if index != args.delete:
            f.write(line)
    f.close()
    list(0)

def output():
    print("outputting entries")
    
if __name__ == '__main__':
   
    parser = argparse.ArgumentParser()

    # A list command
    parser.add_argument('-l','--list', help='List entries', dest="list", action="store_true", default=False)
    parser.add_argument('-a','--add', help='Add an entry', dest="add", action="store")
    parser.add_argument('-b','--backup', help='Backup journal file', dest="backup", action="store_true", default=False)
    parser.add_argument('-d','--delete', help='Delete a journal entry', dest="delete", action="store", type=int, default=0)
    parser.add_argument('-o','--output', help='Output journal in wiki format', dest="output", action="store_true", default=False)
    parser.add_argument('-n','--number', help='List the last n entries', dest="number", action="store", type=int, default=0)
    parser.add_argument('-t','--tag', help='List entries with the suplied tag', dest="tag", action="store")

    args = parser.parse_args()
    print (args)
    
    fname = 'journal.csv'
    fname_backup = 'journal.csv.bak'
           
    # copy journal file to backup copy
    if args.backup:
        backup()
        
    # print out current journal file, with index number
    if args.list:
        list(0)
        
    # add an entry to the end of the file, with current timestamp
    if args.add:
        add()
        
    # delete an entry from the file
    if args.delete:
        delete()
      
    # output the journal in wiki format
    if args.output:
        output()

    # output the last n entries
    if (args.number > 0):
        list_n(args.number)

    if args.tag:
        list_tags(args.tag)
    
