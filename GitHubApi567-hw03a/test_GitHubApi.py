import unittest
from unittest import mock
from GitHubApi import getRepos, getCommits, getRepoInfo

class TestGitHubApi(unittest.TestCase):
    def setUp(self):
        self.user = "richkempinski"
        self.repo = "hellogitworld"

    @mock.patch('requests.get')
    def testGetRepos(self, mockedReq):
        mockedReq.return_value.text = '[{"name":"hellogitworld"}]'
        repos = getRepos(self.user)
        self.assertIn(self.repo, repos)

    @mock.patch('requests.get')
    def testGetNumberOfCommits(self, mockedReq):
        mockedReq.return_value.text = '[{"sha":1},{"sha":2},{"sha":3},{"sha":4},{"sha":5},{"sha":6},{"sha":7},{"sha":8}]'
        commits = getCommits(self.user, self.repo)
        self.assertEqual(len(commits), 8)
        
    @mock.patch('requests.get')
    def testGetRepoInfo(self, mockedReq):
        mockedReq.side_effect = [
            mock.Mock(text='[{"name":"hellogitworld"}]'),
            mock.Mock(text='[{"sha":1},{"sha":2},{"sha":3}]')
        ]
        result = getRepoInfo(self.user)
        self.assertEqual(result, [("hellogitworld", 3)])

if __name__ == '__main__':
    unittest.main()