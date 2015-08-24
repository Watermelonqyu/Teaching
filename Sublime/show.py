import sublime, sublime_plugin

class ShowCommand(sublime_plugin.TextCommand):
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

    def foo():
        first_answer = yield ('First question', '')
        second_answer = yield ('Second question', '')
        third_answer = yield ('Thirdquestion', '')

        sublime.message_dialog('Your answers: ' + answers)

    prompt_sequence(foo())