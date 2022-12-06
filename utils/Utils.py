from os import path


class Utils:
    @staticmethod
    def file_to_lines(str_path):
        url = path.join(path.dirname(__file__), "../inputs", str_path)
        f = open(url, 'r')
        lines = []

        for line in f.readlines():
            lines.append(line.strip('\n'))

        f.close()

        return lines

