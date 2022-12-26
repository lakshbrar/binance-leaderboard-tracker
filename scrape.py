import time
from requests_html import HTMLSession
from scrape_helper import *

old_dict = get_old_dict()
print("start:----")

try:
	while True:
		print("sleeping ",end = "\r")
		time.sleep(60)
		print("                          ",end = "\r")
	
		try:
			body = get_html_body()

			if body == 1:
				sec = 30
				while body == 1:
					print("html error:---- trying again in ",sec," sec")
					time.sleep(sec)
					body = get_html_body(t_out = 60)
					sec += 30
				print("done    ")
				new_dict = get_dict(body)
				if old_dict:
					write_old_dict_backup(old_dict)
			else:
				new_dict = get_dict(body)	
		except Exception as e:
			print("html_block error")		
			print(e)
		try:		
			any_change = compare_dict(old_dict,new_dict,body)

			if any_change:

				tweet_string = ""

				for change in any_change:

					print(change)
					tweet_string += change
					tweet_string += "\n"

				# try:
				# 	tweet_now(tweet_string[:-1])
					
				# except Exception as e:
				# 	print("tweet_error:---")
				# 	print(e)
						
				# 	try:	

				# 		for change in any_change:
				# 			tweet_now(change)
							
				# 		print("tweet done")
				# 	except:
				# 		print("not tweeted")		
				write_old_dict(new_dict)
				old_dict = new_dict
				print("change")	
		except Exception as e:
			print("Some error:---")	
			print(e)

except:

	print("big exception error:------")					







# print(html_bytes)

# print(len(html_bytes))	
# for i in range(len(html_bytes)):
# 		if html_bytes[i] == "d":
 
# 			count += 1
# print(count)			



