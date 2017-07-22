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
        has_error = self.__create_file()
        if has_error is not None:
            return has_error

        result = None
        try:
            command = [self.command, self.input_path]
            result = run(command, stdout=PIPE, stderr=PIPE).stdout
        except Exception as err:
            result = str(err)
        return result

    def __exit__(self, exc_type, exc_value, traceback):
        self.__clean_file()

    def __create_file(self):
        error = None
        try:
            input_file = open(self.input_path, 'w')
            output_file = open(self.output_path, 'w')
            input_file.write(self.code)
        except Exception as err:
            error = str(err)
        finally:
            input_file.close()
            output_file.close()
        return error

    def __clean_file(self):
        os.remove(self.input_path)
        os.remove(self.output_path)
