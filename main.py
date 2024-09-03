meme_dictionary = {
            "CRINGE": "Garip ya da utandırıcı bir şey.",
            "LOL": "Komik bir şeye verilen cevap.",
            "ROFL" : "Bir şakaya karşılık verilen cevap.",
            "SHEESH" : "Onaylamama ifadesi.",
            "CREEPY" : "Tüyler ürpertici, ürkütücü anlamına gelen söz.",
            "AGGRO" : "Agresifleşmek, sinirlenmek anlamına gelen söz.",
            "OMG" : "Aman tanrım anlamında şaşırma ifadesi.",
            "NGL" : "Gerçekten öyle, yalan söylemiyorum anlamına gelen söz."
            }
kelime = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ").upper()
while kelime not in meme_dictionary:
    kelime = input("Düzgün girin!")
    

    
    
if kelime in meme_dictionary.keys():
    
    print(meme_dictionary[kelime])
