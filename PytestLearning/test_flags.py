# pytest -v    show more details about each test run, including the names of the tests being executed.
# pytest -rA: Show all information including passed, skipped, and failed tests.


# pytest -rA: Show all information including passed, skipped, and failed tests.
# pytest -rp: Show only the summary of passed tests.
# pytest -rf: Show only the summary of failed tests.
# pytest -rs: Show only the summary of skipped tests.
# pytest -rx: Show the reason for skipping tests.

# pytest -k "test_login"
# pytest -k "not login"     -->run specific tests based on their names.

# pytest -k test      -->Running tests matching a pattern


# To generate different kind of reports
# pytest -rA --junitxml=report.xml   -->for xml reports generation

# pip install pytest-html--->       install it For html reports generation
# run command --->      pytest -rA --html="HTMLReports.html"
