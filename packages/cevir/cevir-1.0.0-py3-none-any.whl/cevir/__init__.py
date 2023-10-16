def lower(string):
	liste = str.maketrans("ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVXWYZ0123456789","abcçdefgğhıijklmnoöpqrsştuüvxwyz0123456789")
	return string.translate(liste)

def upper(string):
	liste = str.maketrans("abcçdefgğhıijklmnoöpqrsştuüvxwyz0123456789","ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVXWYZ0123456789")
	return string.translate(liste)