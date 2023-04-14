aclNum=int (input ('Cual es el numero de la ACL IPv4?'))
if aclNum>= 1 and aclNum <=99:
	print ('Esta es una ACL IPv4 Estandar')
elif aclNum>= 100 and aclNum<= 217:
	print ('Esta es una ACL IPv4 Extendida')
else:
	print ('Esta no es ni ACL IPv4 Extendida ni ACL IPv4 Estandar')
