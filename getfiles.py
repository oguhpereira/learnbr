import requests


## get content
def getContent(name):
    content = requests.get('https://raw.githubusercontent.com/learnbr/' + name + '/master/README.md')
    return content

## write content
def writeContent(prefix, fileName, content):
    file = open(prefix + '2021-01-01-'+ fileName +'.markdown','a')
    file.write(content.text)
    file.close()

def mountPosts(postContents):
    for post in postContents:
        content = getContent(post)
        fileName = post.replace('https://raw.githubusercontent.com/learnbr/','').replace('/master/README.md','')
        writeContent('_posts/', fileName, content)


contents = [
    'javascript', 
    'python',
    'php',
    'html-css', 
    'wordpress',
    'swift',
    'java',
    'rubyonrails',
    'go',
    'php',
    'elixir',
    'go',
]


mountPosts(contents)
