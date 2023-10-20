import subprocess
from behave import *

@given('the CLI is installed')
def step_impl(context):
    pass  # No setup needed

@when('I run the "{command}" command with "--name {name}"')
def step_impl(context, command, name):
    command = f'python app.py {command} --name {name}'
    context.output = subprocess.check_output(command, shell=True).decode()

@then('it should print "{expected_output}"')
def step_impl(context, expected_output):
    assert expected_output in context.output
