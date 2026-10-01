import requests
import json

def getRepos(user):
    getrepos_url = "https://api.github.com/users/" + user + "/repos"
    resp = requests.get(getrepos_url)
    repos_json = resp.text
    repos = json.loads(repos_json)
    result = []

    for item in repos:
        result.append(item['name'])
    return result


def getCommits(user, repo):
    getcommits_url = "https://api.github.com/repos/" + user + "/" + repo + "/commits"
    resp = requests.get(getcommits_url)
    repos_json = resp.text
    repos = json.loads(repos_json)
    result = []

    for item in repos:
        result.append(item['sha'])
    return result


def getRepoInfo(user):
    repos = getRepos(user)
    result = []
    for repo in repos:
        commits = getCommits(user, repo)
        result.append((repo, len(commits)))

    return result


if __name__ == "__main__":
    result = getRepoInfo("richkempinski")
    for repo, commits in result:
        print("Repo:", repo, "  |  Number of commits:", commits)