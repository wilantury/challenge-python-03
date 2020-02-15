import re

# Resolve the problem!!
p = re.compile('[a-z]')

def run():
    # Start coding here
    with open('src/encoded.txt', 'r', encoding='utf-8') as f:
        text_list = p.findall(f.read())
        text = ''.join(text_list)
        print(text_list)
        print(text)

if __name__ == '__main__':
    run()
