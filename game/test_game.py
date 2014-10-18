from contextlib import contextmanager
from cStringIO import StringIO
import random
import sys

import game


# Fix the random number generator so it always produces the same sequence.
random.seed(1)


# Context manager to capture stdout.
@contextmanager
def capture_stdout():
    original_stdout = sys.stdout
    new_stdout = StringIO()

    try:
        sys.stdout = new_stdout
        yield new_stdout
    finally:
        sys.stdout = original_stdout


# Get expected output.
with open('sample_game.txt') as f:
    expected_output = f.read()


# Get actual output.
with capture_stdout() as captured_stdout:
    game.play()

actual_output = captured_stdout.getvalue()


# Compare actual with expected output.
if actual_output == expected_output:
    print 'Output was as expected'
    exit(0)
else:
    print 'Output was not as expected'
    exit(1)
