import sublime, sublime_plugin
#　import requests
import urllib.request, http.client, http.cookiejar
import json
# from tkinter import *

class InputUserInfoCommand(sublime_plugin.TextCommand):
	def prompt_sequence(g):
        def progress(result):
            try:
                progress.caption, progress.initial_text = g.send(result)
                sublime.active_window().show_input_panel(
                    progress.caption,
                    progress.initial_text,
                    progress, None, None
                )
            except StopIteration:
                pass

        progress(None)

    def getInfo():
        user_id = yield ('User ID', '')
        user_name = yield ('User Name', '')
        # server_address = yield ('Server Address', '')

        sublime.message_dialog('Your answers: ' + answers)

    # prompt_sequence(foo())

	def on_done(self, user_input):
		# sublime.status_message("User said: " + user_input)
		# this is a dialog box, with same message
		sublime.message_dialog("User ID: " + user_input + "is been stored! ")

	def run(self, edit):
		userfile = open('userInfo', 'w')
		# userfile.readline()
		if userfile.readline():
			# read the file
			for line in userfile:
				content += line

			# replace with the correct information
			jcontent = json.dump(content)

		# replace whole file content with user inputs
		prompt_sequence(getInfo())
		jcontent.userid = user_id
		jcontent.username = user_name
		# jcontent.serveraddr = server_address

		# fcontent = [{"userid":jcontent.userid}, {"username":jcontent.username}]
		userfile.write(jcontent)
