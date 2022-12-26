from requests_html import HTMLSession
from binance_price import get_price

def get_html_body(t_out = 20):
	try:
		url = "enter url here"
		session = HTMLSession()
		r = session.get(url)
		print("rendering...    ",end = "\r")
		r.html.render(timeout=t_out)
		body = r.html.find(".bn-table-row")
		session.close()
	except Exception as e:
		session.close()
		print("html error:----")
		print(e)
		return 1

	return body	

def get_dict(body):
	a_dict = {}

	for element in body:
		element = element.text.split()
		a_dict[element[0]] = element[4]

	return a_dict
def get_entry(body):
	b_dict = {}
	for element in body:
		element = element.text.split()
		b_dict[element[0]] = []
		b_dict[element[0]].append(element[5])
		b_dict[element[0]].append(element[2])
		b_dict[element[0]].append(element[3])
	return b_dict	


def compare_dict(old_dict,new_dict,body):

	a_coins = old_dict.keys()
	b_coins = new_dict.keys()
	response = []
	entry = get_entry(body)

	for coin in a_coins:
		if coin not in b_coins:

			response.append("closed:--"+coin+" current price: "+get_price(coin))

	for coin in b_coins:
		if coin not in a_coins:
			if coin.lower() == "short" or coin.lower() == "long":
				print("html error handeled")
				return []
			response.append("New position:-- "+ coin+" "+new_dict[coin]+" entry at: "+entry[coin][0]+" "+entry[coin][1]+entry[coin][2]+" current price: "+get_price(coin))

	for obj in old_dict:
		try:

			if old_dict[obj] != new_dict[obj]:

				response.append("change:-- "+obj+" "+old_dict[obj]+" to "+new_dict[obj]+" entry at: "+entry[obj][0]+" "+entry[obj][1]+entry[obj][2]+" current price: "+get_price(obj))
		except:
			print("exception:--", obj)
	return response	

def write_old_dict(old_dict):

	with open("old.txt","w") as f:

		for key in old_dict.keys():
			f.write("%s:%s\n"% (key,old_dict[key]))
	return

def write_old_dict_backup(old_dict):

	with open("old_backup.txt","w") as f:

		for key in old_dict.keys():
			f.write("%s:%s\n"% (key,old_dict[key]))
	return


def get_old_dict():

	try:
		with open("old.txt","r") as f:

			a = f.read()
		a = a[:-1]
		a = a.split()

		old_dict = {}

		if a:

			for element in a:

				element = element.split(":")

				old_dict[element[0]] = element[1]
			print("old loaded:---")
			return old_dict	
		else:
			print("old not loaded from system:---")
			return get_dict(get_html_body()	)
	except:
		print("old error:---")
		return get_dict(get_html_body())