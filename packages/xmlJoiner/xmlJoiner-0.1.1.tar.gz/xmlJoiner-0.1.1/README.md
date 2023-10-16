# xmlJoiner

Join two or more PARC Telemetry files downloaded from ESA EDDS.

## Installation

To install the reader you can use the command:

```console
$ python3 -m pip install xmlJoiner
```

## Usage

To join all the XML files *myxml_01.xmlr* and *myxml_02.xml* in a single file called *myxml.xml* you can use the command:

```console
$ xmlJoin myxml01.xml myxml_02.xml -o myxml.xml
``````

You can join also directly all the files in a folder:

```console
$ xmlJoin -f myfolder -o myfolder.xml
```

**N.B.:** be careful the file are sorted alphabetically. if they are numered the file #10 is befre the file #2. Please check the order using the command 

```console
$ xmlJoin -f myfolder --show-list
```
and change the file names if it is necessary.

You can use it also as library:

```python
from xmlJoiner import xmlJoin

xmlJoin(fileList, "joined.xml",verbose=True)
```