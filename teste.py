import operator

class Language(object):
    def __init__(self,year,name):
        self.year = year
        self.name = name

    def __repr__(self):
        return ' - '.join(map(str,(self.name,self.year)))


java = Language(1995,'Java')
python = Language(1991,'Python')
ruby = Language(1995,'Ruby')
haskell = Language(1990,'Haskell')
javascript = Language(1995,'Javascript')
self = Language(1986,'Self')
perl = Language(1987,'Perl')

languages = [java,python,ruby,haskell,javascript,self,perl]

#print(languages)
languages.sort(key=operator.attrgetter('year'))
print(languages)
#Apenas Python 2.5 agora!
# languages.sort(key=operator.attrgetter('year','name'))
# print(languages)