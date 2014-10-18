from collections import Counter, defaultdict
import re

def commits_by_contributor(path):
    commits = Counter()

    with open(path) as f:
        for line in f:
            match = re.match('Author:.*<(.*)>$', line)
            if match:
                email_address = match.group(1)
                commits[email_address] += 1

    return commits


def commits_by_year(path):
    commits = Counter()

    with open(path) as f:
        for line in f:
            match = re.match('Date:.* (\d{4}) [+-]\d{4}$', line)
            if match:
                year = int(match.group(1))
                commits[year] += 1

    return commits


def commits_by_contributor_by_year(path):
    commits = defaultdict(Counter)

    with open(path) as f:
        for line in f:
            match = re.match('Author:.*<(.*)>$', line)
            if not match:
                continue

            email_address = match.group(1)
            line = next(f)
            match = re.match('Date:.* (\d{4}) [+-]\d{4}$', line)
            if not match:
                raise Exception('Expected {} to contain date'.format(line))

            year = int(match.group(1))
            commits[email_address][year] += 1

    return commits


if __name__ == '__main__':
    print 'The people with the most commits are:'
    commits = commits_by_contributor('git.log')
    for email_address, count in commits.most_common(10):
        print('{:>5} {}'.format(count, email_address))

    print
    
    print 'This is the number of commits there have been every year:'
    commits = commits_by_year('git.log')
    for year, count in sorted(commits.items()):
        print(' {} {}'.format(year, count))

    print

    print 'This is the number of commits that Russel has made each year:'
    commits = commits_by_contributor_by_year('git.log')
    commits_by_russell = commits['russell@keith-magee.com']
    for year, count in sorted(commits_by_russell.items()):
        print(' {} {}'.format(year, count))
