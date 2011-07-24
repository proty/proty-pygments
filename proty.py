from pygments.lexer import RegexLexer
from pygments.token import *

class ProtyLexer(RegexLexer):
    name = 'Proty'
    aliases = ['proty', 'pr']
    filenames = ['*.pr']

    tokens = {
        'root': [
            (r'\n', Text),
            (r'\s+', Text),
            (r'/\*(.|\n)*\*/', Comment.Multiline),
            (r'//(.*?)\n', Comment.Single),
            (r'[]{}(),[]', Punctuation),
            (r'\\\n', Text),
            (r'\\', Text),
            (r'!=|==|=|,|\+|-|\*|/|>|<', Operator),
            (r'(while|if|else|do|try|catch|end)', Keyword),
            (r'(self|true|false|nil)', Name.Builtin.Pseudo),
            (r'"(.*)"', String),
            (r':[a-zA-Z_][a-zA-Z0-9_]*', String.Symbol),
            (r'[a-zA-Z_][a-zA-Z0-9_]*', Name),
            (r'(\d+\.?\d*)', Number.Float),
            (r'\d+', Number.Integer),
        ]
    }
