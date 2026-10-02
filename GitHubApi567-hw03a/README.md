# GitHub API - HW03b Mocking

[![Build Status](https://app.travis-ci.com/github-mahima/SSW-567-QA.svg?branch=HW03b_Mocking)](https://app.travis-ci.com/github-mahima/SSW-567-QA?branch=HW03b_Mocking)

## Description

This project uses the GitHub API to retrieve repository names and the number of commits for each repository. For HW03b, the GitHub API calls are mocked so that the unit tests do not depend on the live GitHub API.

## Files

* `GitHubApi.py` - Contains the GitHub API functions.
* `test_GitHubApi.py` - Contains the unit tests with mocked GitHub API calls.
* `requirements.txt` - Contains the Python dependency required by the application.
* `.travis.yml` - Configures Travis CI to run the tests.

## Running the Tests

From the `GitHubApi567-hw03a` folder, run:

```text
python -m unittest test_GitHubApi.py