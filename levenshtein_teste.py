import Levenshtein
str1 = "tem pão"
str2 = "chover"
distancia = Levenshtein.distance(str1, str2)
print("A distância de Levenshtein entre '{}' e '{}' é: {}".format(str1, str2, distancia))