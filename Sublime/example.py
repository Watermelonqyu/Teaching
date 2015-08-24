import sublime, sublime_plugin
#　import requests
import urllib

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		author = {'nickname': 'John'}
		postAuthor = {'author': author}
		content = self.view.substr(sublime.Region(0, self.view.size()))
		body = {'body': content}
		postContent = [author, body]
		# url = '127.0.0.1:5000/index'
		#　getr = requests.get(url)
		#　postr = requests.post(url, data=content)
 
		self.view.insert(edit, 0, str(postContent))
