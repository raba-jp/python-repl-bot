import os
from nose.tools import ok_, raises
from plugins.repl import Repl


class TestRepl:
    def setup(self):
        self.repl = Repl()
        self.repl.input_path = './tmp/tmp.py'
        self.repl.output_path = './tmp/tmp.txt'
        self.repl.code = 'print("sample")'
        self.repl.command = 'python3'

    def teardown(self):
        if os.path.isfile(str(self.repl.input_path)):
            os.remove(self.repl.input_path)
        if os.path.isfile(str(self.repl.output_path)):
            os.remove(self.repl.output_path)

    @raises(TypeError)
    def test_none_input_path(self):
        self.repl.input_path = None
        self.repl.run_cmd()

    @raises(FileNotFoundError)
    def test_blank_input_path(self):
        self.repl.input_path = ''
        self.repl.run_cmd()

    @raises(TypeError)
    def test_none_output_path(self):
        self.repl.output_path = None
        self.repl.run_cmd()

    @raises(FileNotFoundError)
    def test_blank_output_path(self):
        self.repl.output_path = ''
        self.repl.run_cmd()

    @raises(TypeError)
    def test_none_code(self):
        self.repl.code = None
        self.repl.run_cmd()

    def test_blank_code(self):
        self.repl.code = ''
        self.repl.run_cmd()
        file = open(self.repl.input_path, 'r')
        ok_(file.read() == '')

    def test_with_syntax(self):
        with Repl() as repl:
            repl.input_path = './tmp/tmp.py'
            repl.output_path = './tmp/tmp.txt'
            repl.code = 'print("sample")'
            repl.command = 'python3'
            repl.run_cmd()
        ok_(not os.path.exists('./tmp/tmp.py'))
        ok_(not os.path.exists('./tmp/tmp.txt'))
