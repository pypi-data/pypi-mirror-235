# MusicManager
Build a list of media files from a root directory
# Usage
First time usage should use the execute function. This will return the python list of entries containing tuples in the form (mtime:int,path:str)
```python
import MusicManager as mm

library = '<library_name>'
root_dir = '/media/music'
music_list = mm.execute(library, root_dir)
# music_list = [(<mtime>,'<rel_path>'),...,(<mtime>,'<path>')]
```
Since the program stores the result in a sqlite DB in 
```
$HOME/.config/MusicManagerMicro/<library_name>
```
we can retrieve the data quickly without re-scanning the directory. We only need to execute when we want to check for new files.

Get an existing list
```python
import MusicManager as mm
library = '<library_name>'
mm.setLibrary(library)
music_list = mm.get_list()
```
# Features

* By default searches for .mp3 and .flac files
* Supports absolute and relative root directory

# Notes
* Library name is intended for internal use so should only contain characters acceptable for a folder name A-Z, a-z, _, -.