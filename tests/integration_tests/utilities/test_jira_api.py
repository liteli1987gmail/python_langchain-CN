"""Integration test for JIRA API Wrapper."""
from langchain.utilities.jira import JiraAPIWrapper


def test_search() -> None:
    """Test for Searching issues on JIRA"""
    jql = "project = TP"
    jira = JiraAPIWrapper()
    output = jira.run("jql", jql)
    assert "issues" in output


def test_getprojects() -> None:
    """Test for getting projects on JIRA"""
    jira = JiraAPIWrapper()
    output = jira.run("get_projects", "")
    assert "projects" in output


def test_create_ticket() -> None:
    """Test the Create Ticket Call that Creates a Issue/Ticket on JIRA."""
    issue_string = (
        '{"summary": "Test Summary", "description": "Test Description",'
        ' "issuetype": {"name": "Bug"}, "project": {"key": "TP"}}'
    )
    jira = JiraAPIWrapper()
    output = jira.run("create_issue", issue_string)
    assert "id" in output
    assert "key" in output
