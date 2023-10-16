#Python lower ve upper string fonksiyonlarına zaten sahiptir. Fakat Python 3.12 versiyonuna gelmiş olmasına rağmen
#hala lower ve upper fonksiyonları utf-8 mantığıyla değil ascii mantığıyla çalışmakta ve harf dönüşümleri Türkçe için
#hatalı olabilmektedir. Bu paket ise bu derdi ortadan kaldırmaya yöneliktir.
##Bu python paketi şu şekilde kullanılır:

import cevir

yazi = "ÇEMİŞGEZEK"
print(cevir.lower(yazi)) # Sonuç = çemişgezek

yazi2 = "çemizgezek"
print(cevir.upper(yazi)) # Sonuç = ÇEMİŞGEZEK

YA DA

from cevir import lower,upper

yazi = "ÇEMİŞGEZEK"
print(lower(yazi)) # Sonuç = çemişgezek

yazi2 = "çemizgezek"
print(upper(yazi)) # Sonuç = ÇEMİŞGEZEK
