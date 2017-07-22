import os
from slackbot.bot import respond_to
from plugins.repl import Repl


@respond_to(r'.+')
def response(message):
    result = None
    with Repl() as repl:
        repl.input_path = os.getenv('PYTHON_INPUT', './tmp/tmp.py')
        repl.output_path = os.getenv('PYTHON_OUTPUT', './tmp/tmp.txt')
        repl.code = message.body['text']
        repl.command = 'python3'
        result = repl.run_cmd()
    message.reply(result)
