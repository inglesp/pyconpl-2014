import unittest
import gitstats


class TestGitstats(unittest.TestCase):
    def test_commits_by_contributor(self):
        commits = gitstats.commits_by_contributor('git.log')
        self.assertEqual(2802, commits['adrian@holovaty.com'])

    def test_commits_by_year(self):
        commits = gitstats.commits_by_year('git.log')
        self.assertEqual(1277, commits[2005])

    def test_commits_by_contributor_by_year(self):
        commits = gitstats.commits_by_contributor_by_year('git.log')
        self.assertEqual(619, commits['russell@keith-magee.com'][2010])


if __name__ == '__main__':
    unittest.main()
