>>> from array import array
>>> codes = array('B', b'Bonjour')
>>> codes
array('B', [66, 111, 110, 106, 111, 117, 114])
>>> codes[0]
66
>>> codes[1]
111
>>> codes[-1]
114

---------------------------------------------------

>>> s = 'Bonjour'
>>> type(s)
<class 'str'>
>>>
>>> s_bytes = bytes(s, 'utf8')
>>> type(s_bytes)
<class 'bytes'>
>>>
>>> codes = array('B', s_bytes)
>>> codes
array('B', [66, 111, 110, 106, 111, 117, 114])

---------------------------------------------------

>>> list(s_bytes)
[66, 111, 110, 106, 111, 117, 114]

---------------------------------------------------

>>> chaine = "Bonjour le monde"
>>> chaine.encode('hex')
'426f6e6a6f7572206c65206d6f6e6465'
>>> chaine2 = "426f6e6a6f7572206c65206d6f6e6465"
>>> chaine2.decode('hex')
'Bonjour le monde'
>>>

--------------------------------------------------

>>> ascii("Ë")
"'\\xcb'"

---------------------------------------------------

>>> str = "G ë ê k s f ? r G ? e k s"
>>> print (ascii(str))
'G \xeb \xea k s f ? r G ? e k s'

---------------------------------------------------

>>> ord('h')
104
>>> ord('a')
97
>>> ord('^')
94

----------------------------------------------------

>>> chr(104)
'h'
>>> chr(97)
'a'
>>> chr(94)
'^'

----------------------------------------------------

# afficher juste quelques caractères d'une string
>>> "Hello Wikibooks!"[0:5]
'Hello'
>>> "Hello Wikibooks!"[5:11]
' Wikib'
>>> "Hello Wikibooks!"[:5] #equivalent of [0:5]
'Hello'
