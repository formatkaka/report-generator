# import fileinput

# for line in fileinput.input('repo_file',inplace=1):
# 	if line.endswith(".git"):
# 		print line.replace(line, line[:-6]).rstrip()
# 	else:
# 		print line.replace(line, line).rstrip()


from tempfile import mkstemp
from shutil import move
from os import remove

fh, target_file = mkstemp()
with open('repo_file_2','a') as t:
	with open('repo_file','r') as r:
		for line in r.readlines():
			t.write(line[:-6])
			t.write("\n")

	remove('repo_file')
	move('repo_file_2','repo_file')