import string

class MyTemplates(string.Template):
    delimiter = '%'
    idpattern = '[a-z+_[a-z]+'

temlpate_text= '''
    Delimiter   :%%
    Replaced    :%with_underscore
    Ignored     :%notunderscored
    '''
d = {
    'withunderscore' :'replaced',
    'notunderscore'  :'not replaced'
}

t = MyTemplates(temlpate_text)
print('Modified ID Pattern:')
print(t.safe_substitute(d))
