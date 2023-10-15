import json
import sys
from typing import Any, Dict
import click
from .util import get_client, FE_HOST
from gql import gql
import boto3


@click.group()
def suite():
    pass


def parse_suite_interactive():
    title = click.prompt("Test Suite Title")
    while title == "":
        title = click.prompt("Title cannot be empty. Reenter")

    description = click.prompt("Test Suite Description")

    i = 1
    keep_generating_prompts = True
    tests = []
    while keep_generating_prompts:
        click.secho(f"---Test {i}---", bold=True)
        input_under_test = click.prompt("Input under test (e.g. the prompt)")

        keep_generating_criteria = True
        j = 1
        checks = []
        while keep_generating_criteria:
            # TODO: Validation
            operator = click.prompt(f"Operator {j}")
            # TODO: Skip based on operator
            criteria = click.prompt(f"Criteria {j}")
            checks.append({"criteria": criteria, "operator": operator})
            j += 1

            keep_generating_criteria = click.confirm("Keep Generating Checks?")

        i += 1

        tests.append({"input_under_test": input_under_test, "checks": checks})
        keep_generating_prompts = click.confirm("Keep generating tests?")

    return {"title": title, "description": description, "tests": tests}


def parse_suite_file(file):
    return json.load(file)


def create_test_suite(data: Dict[str, Any]) -> str:
    query = gql(
        f"""
    mutation createTestSuite {{
        updateTestSuite(
            description: "{data['description']}",
            testSuiteId: "0",
            title: "{data['title']}"
        ) {{
            testSuite {{
            description
            id
            org
            title
            }}
        }}
    }}
    """
    )
    result = get_client().execute(query)
    suite_id = result["updateTestSuite"]["testSuite"]["id"]
    return suite_id


def add_tests(data, suite_id):
    for test in data["tests"]:
        # TODO: Escape chars better
        input_under_test = test["input_under_test"]
        # TODO: avoid double json
        checks = json.dumps(json.dumps(test["checks"]))
        # TODO: Do this server side

        sample_output = test["sample_output"] if "sample_output" in test else ""

        query = gql(
            f"""
        mutation addUpdateTest {{
              updateTest(
                  sampleOutput: {json.dumps(sample_output)},
                  checks: {checks}, 
                  inputUnderTest: {json.dumps(input_under_test)}, 
                  inputUnderTestType: "raw",
                  testId: "0",
                  testSuiteId: "{suite_id}") {{
                  test {{
                    checks
                    inputUnderTest
                    testId
                  }}
                }}
            }}
            """
        )
        get_client().execute(query)
        # TODO: Check response?


@click.command()
@click.option("--interactive", "-i", is_flag=True)
@click.argument("file", type=click.File("r"), required=False)
def create(interactive: bool, file: str):
    # try:
    if not interactive and file is None:
        click.echo(
            "Either --interactive must be passed, or an input file should be specified"
        )
        sys.exit(1)

    click.echo("Creating test suite...")

    if interactive:
        data = parse_suite_interactive()
    else:
        data = parse_suite_file(file)

    suite_id = create_test_suite(data)
    add_tests(data, suite_id)
    # Execute the query on the transport
    click.secho("Successfully created test suite.", fg="green")
    click.secho(f"{FE_HOST}/view?test_suite_id={suite_id}", bold=True)

    # except Exception as e:
    #     click.secho("Suite Creation Failed. Error: " + str(e), fg="red")


suite.add_command(create)
