class TextAnalyser(object):
    def __init__(self, file_or_path, equivalence_function):
        if isinstance(file_or_path, file):
            self._file = file_or_path
            self._cleanup_required = False
        else:
            self._file = open(file_or_path)
            self._cleanup_required = True

        self._equivalence_function = equivalence_function

        self._counter = {}

    def analyse(self):
        for line in self._file.readlines():
            words = line.split()
            for word in words:
                self._analyse_word(word)

    def most_common(self):
        item = None
        count = 0

        for k, v in self._counter.items():
            if v > count:
                item = k
                count = v

        return item

    def cleanup(self):
        if self._cleanup_required:
            self._cleanup()

    def _cleanup(self):
        self._file.close()

    def _analyse_word(self, word):
        value = self._equivalence_function(word)
        if value in self:
            self[value] += 1
        else:
            self[value] = 1

    def __getitem__(self, key):
        return self._counter[key]

    def __setitem__(self, key, value):
        self._counter[key] = value

    def __contains__(self, key):
        return key in self._counter


def find_most_common_first_letter(path):
    analyser = TextAnalyser(path, lambda word: word[0])
    analyser.analyse()
    return analyser.most_common()


if __name__ == '__main__':
    letter = find_most_common_first_letter('sample.txt')
    print 'The most common first letter is', letter
