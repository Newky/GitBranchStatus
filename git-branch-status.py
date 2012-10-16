#!/usr/bin/env python
import subprocess
import sys


def run_command(cmd, error_ok=False, error_message=None, exit_code=False,
	redirect_stdout=True):
	if redirect_stdout:
		stdout = subprocess.PIPE
	else:
		stdout = None
	proc = subprocess.Popen(cmd, stdout=stdout)
	output = proc.communicate()[0]
	if exit_code:
		return proc.returncode
	if not error_ok and proc.returncode != 0:
		sys.exit(1)
	return output


def run_git(args, **kwargs):
	cmd = ["git"] + args
	return run_command(cmd, **kwargs)


def get_branch_name():
	branch_ref = run_git(['symbolic-ref', 'HEAD']).strip()
	return branch_ref.replace("refs/heads/", "")


def set_branch_status(message):
	branch_name = get_branch_name()
	config_option = "branch.%s.notes" % branch_name
	run_git(['config', config_option, message])


def clear_branch_status():
	branch_name = get_branch_name()
	config_option = "branch.%s.notes" % branch_name
	run_git(['config', '--unset', config_option])


def get_branch_status():
	branch_name = get_branch_name()
	config_option = "branch.%s.notes" % branch_name
	output = run_git(['config', config_option])
	return output.strip()


def usage(filename):
	print """
	usage %s <command> <message>"
	commands are:
	set: set branch message to <message>
	get: get branch message
	""" % filename
	sys.exit(1)


def main(argv):
	if len(argv) < 2:
		usage(argv[0])
	command = argv[1]
	if command == "set":
		if len(argv) < 3:
			clear_branch_status()
		else:
			set_branch_status(argv[2])
	elif command == "get":
		branch_status = get_branch_status()
		print branch_status
	else:
		usage(argv[0])

if __name__ == '__main__':
	sys.exit(main(sys.argv))
