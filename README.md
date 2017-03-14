# journal
A simple command line journal, written in Python. Add, delete and list timestamped journal entires

Creates a journal.csv file in current directory.

## Run
```
$ python3 journal.py -h
usage: journal.py [-h] [-l] [-a ADD] [-b] [-d DELETE] [-o] [-n NUMBER]
                  [-t TAG]

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            List entries
  -a ADD, --add ADD     Add an entry
  -b, --backup          Backup journal file
  -d DELETE, --delete DELETE
                        Delete a journal entry
  -o, --output          Output journal in wiki format (not implemented yet)
  -n NUMBER, --number NUMBER
                        List the last n entries
  -t TAG, --tag TAG     List entries with the suplied tag
```


Tags can be supplied anywhere in the message string and are identified by '#'
```
$>python3 journal.py -a "this is a new message with a tag #urgent #work"
```

## Still to do:
- finish off the -o output as markdown for wikis, perhaps output JSON too.
- Store location of journal file and allow writing to journal file from wherever journal is run from

