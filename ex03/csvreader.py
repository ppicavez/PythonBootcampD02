class CsvReader():
    def __init__(self, file_name, sep=',', header=False, skip_top=0,
                 skip_bottom=0):
        self.name = file_name
        self.sep = sep
        self.header = header
        self.top = skip_top
        self.bot = skip_bottom
        self.fileCSV = None

    def __enter__(self):
        try:
            self.fileCSV = open(self.name, 'r')
        except FileNotFoundError:
            return None
        lines_list = self.fileCSV.read().split('\n')
        if self.header:
            self.header = lines_list[0].split(self.sep)
            lines_list = lines_list[1:]
        else:
            self.header = "[ No header ]"
        lines_list = lines_list[self.top: len(lines_list) - self.bot - 1]
        self.data = [i.split(self.sep) for i in lines_list]
        i = 1
        while i < len(self.data):
            if len(self.data[i]) != len(self.data[0]):
                return None
            else:
                i = i + 1
        return self

    def __exit__(self, *args):
        self.fileCSV.close()

    def getheader(self):
        return self.header

    def getdata(self):
        return self.data


print("=== Good ===")
with CsvReader("good.csv", ',', False) as reader:
    if reader is None:
        print("File corrupted!")
    else:
        print(reader.getheader())
        for val in reader.getdata():
            print(val)

print("\n=== Bad ===")
with CsvReader("bad.csv", ',', True) as reader:
    if reader is None:
        print("File corrupted!")
    else:
        print(reader.getheader())
        for val in reader.getdata():
            print(val)
