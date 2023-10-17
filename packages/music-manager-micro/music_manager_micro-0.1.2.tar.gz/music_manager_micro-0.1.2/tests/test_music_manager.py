from src.music_manager_micro import MusicManager as mm
from File import File as F

library_name = '###TESTABC###'
mm.app_environment['root_dir'] = '.cache/'
def test_active():
    assert(1==1)
    assert(1!=0)
    
# Tests the collation of music files in a root directory
def test_getfiles():
    dir = 'tests/multi_sample'
    l = mm.__getFilesFromFolder(dir)
    assert(len(l) == 2)
    assert(l[0] == 'tests/multi_sample/2.mp3')
    assert(l[1] == 'tests/multi_sample/1.mp3')
    
# Tests a music file can generate a valid string representation
def test_build_entry():
    dir = 'tests/multi_sample'
    l = mm.__getFilesFromFolder(dir)
    e = mm.__build_entry(l[0])
    assert(e[0] == 1690570765.6394708)
    assert(e[1] == 'tests/multi_sample/2.mp3')

# Tests that a root directory can generate a list of valid strings
def test_build_list():
    dir = 'tests/multi_sample'
    e = mm.__build_list(dir)
    assert(e[0][0] == 1690570765.6394708)
    assert(e[1][1] == 'tests/multi_sample/1.mp3')

def test_execute():
    dir = './tests/multi_sample'
    mm.app_environment['root_dir'] = mm.default_root_dir
    l = mm.execute(library_name, dir)
    assert(len(l) == 2)
    l = mm.get_list()
    assert(len(l) == 2)

def test_get_list():
    l = mm.get_list()
    assert(len(l) == 2)