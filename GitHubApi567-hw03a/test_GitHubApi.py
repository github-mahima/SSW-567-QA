import unittest

from GitHubApi import getRepos, getCommits, getRepoInfo

class TestGitHubApi(unittest.TestCase):
    def setUp(self):
        self.user = "richkempinski"
        self.repo = "hellogitworld"
    def testGetRepos(self):
        repos = getRepos(self.user)
        self.assertIn(self.repo, repos)
    def testGetNumberOfCommits(self):
        commits = getCommits(self.user, self.repo)
        self.assertTrue(len(commits) > 0)
    def testGetRepoInfo(self):
        result = getRepoInfo(self.user)
        repo_names = []
        for repo, commits in result:
            repo_names.append(repo)
        self.assertIn(self.repo, repo_names)

if __name__ == '__main__':
    unittest.main()