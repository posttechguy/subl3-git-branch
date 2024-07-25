import sublime, sublime_plugin
import re

class git_branch( sublime_plugin.TextCommand ):
    def run( self, edit ):

        clipboard = sublime.get_clipboard()
        result = re.match("^(([A-Z0-9]*)-([0-9]*))((\n)*)([A-Za-z.,-: |\'\"\(\)\[\]&<>]*)", clipboard)
        ticket = result.group(1)
        group6 = result.group(6)
        group6 = group6.replace( " ", "-" ).replace( "&", "and" ).replace( "\n", "--" ).replace( "->", "" )

        chars = ".,:'&#\"|\(\)<>"
        for c in chars:
            group6 = group6.replace(c, "")

        group6 = group6.lower()
        sublime.set_clipboard("git checkout -b feature/" + ticket + "--" + group6 + "\n")
        self.view.run_command( "paste" )
        sublime.set_clipboard(clipboard)
