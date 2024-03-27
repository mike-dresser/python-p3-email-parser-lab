import re

class EmailAddressParser:
    
    def __init__(self, string) -> None:
        self.string = string 

    def parse(self):
        pattern = r'[\s,]+'
        split = re.split(pattern, self.string)
        print(f'split: {split}')
        output = []
        for item in split:
            pattern = re.compile(r'[A-z0-9\.+-]+@[A-z0-9]+\.[A-z]+')
            print(f'item: {item}, match: {pattern.match(item)}')
            if pattern.match(item):
                output.append(item)
        unique = list(set(output))
        unique.sort()
        return unique
