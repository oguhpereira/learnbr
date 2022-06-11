import requests


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
    'csharp'
]

## get template
file = open('./template.md','r')
template = file.read()


## get content
def getContent(name):
    content = requests.get('https://raw.githubusercontent.com/oguhpereira/learnbr/tree/main/docs/' + name + 'README.md')
    return content

## write content
def writeContent(prefix, fileName, content):
    file = open(prefix + '2021-01-01-'+ fileName +'.md','a')
    file.write(template + content.text)
    file.close()

def mountPosts(postContents):
    for post in postContents:
        content = getContent(post)
        fileName = post.replace('https://raw.githubusercontent.com/oguhpereira/learnbr/tree/main/docs/','').replace('README.md','')
        writeContent('../_posts/', fileName, content)


mountPosts(contents)
