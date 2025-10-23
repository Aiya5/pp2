'''
Key Operations and Modules:
os module: This module provides a way of using operating system dependent functionality.
os.getcwd(): Gets the current working directory.
os.chdir(path): Changes the current working directory to path.
os.mkdir(dirname): Creates a new directory named dirname.
os.makedirs(path): Creates directories recursively (including any necessary parent directories).
os.rmdir(dirname): Removes an empty directory named dirname.
os.remove(filename): Deletes a file.
os.rename(src, dst): Renames a file or directory from src to dst.
os.listdir(path): Returns a list of all files and directories within the specified path.
os.walk(top): Generates file names in a directory tree by walking the tree either top-down or bottom-up.
os.path module: This sub-module of os provides common pathname manipulations.
os.path.join(path1, path2, ...): Joins one or more path components intelligently.
os.path.exists(path): Checks if a path exists.
os.path.isfile(path): Checks if a path points to a file.
os.path.isdir(path): Checks if a path points to a directory.
os.path.basename(path): Returns the base name of a path.
os.path.dirname(path): Returns the directory name of a path.
pathlib module: Offers an object-oriented approach to file system paths.
Path('my_directory'): Creates a Path object.
Path.cwd(): Returns the current working directory as a Path object.
Path.mkdir(): Creates a new directory.
Path.is_file(), Path.is_dir(): Checks if the path is a file or directory.
Path.iterdir(): Iterates over the contents of a directory.
shutil module: Provides high-level file operations.
shutil.copy(src, dst): Copies a file.
shutil.copytree(src, dst): Copies an entire directory tree.
shutil.rmtree(path): Deletes a directory and all its contents (use with caution).

'''
'''# Quick Notes:
# os.path.exists(path) - Check if path exists
# os.listdir(path) - List everything in folder  
# os.path.isdir(item) - Check if folder
# os.path.isfile(item) - Check if file
# os.path.join(path, item) - Combine paths safely
# os.access(path, os.R_OK) - Can read?
# os.access(path, os.W_OK) - Can write?
# os.access(path, os.X_OK) - Can execute?
# os.path.dirname(path) - Get folder path
# os.path.basename(path) - Get filename
# os.remove(path) - Delete file
# with open(file, 'r') - Read file
# with open(file, 'w') - Write file
'''