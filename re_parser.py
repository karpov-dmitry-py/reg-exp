import re

class ReParser:

    def __init__(self, re_pattern):
        self.pattern = re.compile(re_pattern)

    def go(self, re_string):

        matches = self.pattern.finditer(re_string)
        for match in list(matches):
            print(match.group())

def main():

    # Нужно написать одну регулярку, которая из этих строк выделит сущности:
    string_1 = '@a @ab @abc a@xyz !@ijmn,@123 0@321 @1a2b @qwerty'
    # expected result from string_1 = ["@abc", "@ijmn", "@123", "@1a2b"]

    string_2 = '@abc.a @stu..test _@nmp @x.yz.@klm @.1a2b .@2c3d.'
    # expected result from string_2 = ["@abc.a", "@stu", "@x.yz", "@klm", "@2c3d"]

    full_string = f'{string_1} {string_2}'
    re_pattern = r'@([a-c.]{3,5})|(@[i-n]{3,4})|(@[1-2]{2}[^1])|([s-u]{3})|([x-z.]{4})|(@[1-3a-d]{4})'
    re_parser = ReParser(re_pattern)
    re_parser.go(full_string)

if __name__ == '__main__':
    main()