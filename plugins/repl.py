import os
from subprocess import run, PIPE


class Repl:
    def __init__(self):
        self.input_path = None
        self.output_path = None
        self.code = None
        self.command = None

    def __enter__(self):
        return self

    def run_cmd(self):
        self.__create_file()
        result = None
        try:
            command = [self.command, self.input_path]
            result = run(command, stdout=PIPE, stderr=PIPE).stdout
        except Exception as err:
            result = err
        return str(result)

    def __exit__(self, exc_type, exc_value, traceback):
        self.__clean_file()

    def __create_file(self):
        with open(self.input_path, 'w') as input, open(self.output_path, 'w'):
            input.write(self.code)

    def __clean_file(self):
        if os.path.isfile(self.input_path):
            os.remove(self.input_path)
        if os.path.isfile(self.output_path):
            os.remove(self.output_path)
