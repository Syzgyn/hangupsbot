import unicodedata, string

import hangups

from hangupsbot.parser import ChatMessageParser, tokens

def text_to_segments(text):
    """Create list of message segments from text"""
    parser = ChatMessageParser(tokens)
    return parser.parse(text)


def unicode_to_ascii(text):
    """Transliterate unicode characters to ASCII"""
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()


def word_in_text(word, text):
    """Return True if word is in text"""
    word = unicode_to_ascii(word).lower()
    text = unicode_to_ascii(text).lower()

    # Replace delimiters in text with whitespace
    for delim in '.,:;!?':
        text = text.replace(delim, ' ')

    return True if word in text.split() else False


def strip_quotes(text):
    """Strip quotes and whitespace at the beginning and end of text"""
    return text.strip(string.whitespace + '\'"')
