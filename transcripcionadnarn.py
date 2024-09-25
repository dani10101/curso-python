#ATGATC
#transcripcion de el primer string al segundo
#TACTAG
adn_a_arn= lambda adn: adn.replace("T","a").replace("A","t").replace("G","c").upper()
#cadena a transcribir
cadena_adn= "TACTAGAGCaTT"
cadena_arn = adn_a_arn(cadena_adn)
print("la cadena de ARN es:",cadena_arn)