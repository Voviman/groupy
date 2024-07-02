from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.errors import BadRequest
import nltk
from time import sleep as son

app = Client("my_account")

words = 'THIS USER WAS HACKED//ПОЛЬЗОВАТЕЛЬ БЫЛ ВЗЛОМАН'
tokens = nltk.word_tokenize(words)
flood_text = nltk.Text(tokens)
stop = False
echo = False

@app.on_message(filters.command(["kick_all"]))
def get_chat(client, message):
	x = app.iter_chat_members(message.chat.id)
	for i in x:
		try:
			son(0.1)
			app.kick_chat_member(message.chat.id, i.user.id)

		except BadRequest:
			print('error')

		except Exception as e:
			app.send_message(message.chat.id, e)
			print(e)


@app.on_message(filters.command(["hack"]))
def hack(client, message):
	x = app.iter_chat_members(message.chat.id)
	for i in x:
		msg = f'{i.user.mention}\nUSER - {i.user.first_name} - {i.user.id} WAS HACKED\n'
		msg += f'USER STATUS - {i.status}\n JOINED_DATE:{i.joined_date}'
		app.send_message('me', msg)


@app.on_message(filters.command(["hack_tome"]))
def hack_tome(client, message):
	x = app.iter_chat_members(message.chat.id)
	for i in x:
		try:
			msg = f'{i.user.mention}\nUSER - {i.user.first_name} - {i.user.id} WAS HACKED\n'
			msg += f'USER STATUS - {i.status}\n JOINED_DATE:{i.joined_date}'
			app.send_message(message.chat.id, msg)
		except Exception as e:
			pass


@app.on_message(filters.command(["get_admin"]))
def get_admin(client, message):
	x = app.iter_chat_members(message.chat.id)
	for i in x:
		try:
			if i.status != 'member':
				msg = f'{i.user.mention}\nUSER - {i.user.first_name} - {i.user.id}\n'
				msg += f'USER STATUS - {i.status}\n JOINED_DATE:{i.joined_date}'
				app.send_message(1850643439, msg)
		except Exception as e:
			pass

	
@app.on_message(filters.command(["time"]))
def time(client, message):
	app.send_message(message.chat.id, message.date)


@app.on_message(filters.command(["flood"]))
def flood(client, message):
	global stop
	stop = False
	i = 1
	while (stop == False):
		try:
			i += 1
			app.send_message(message.chat.id, '1')
		except BadRequest:
			print('Flood')


@app.on_message(filters.command(["flood_off"]))
def flood_off(client, message):
	global stop
	stop = True


@app.on_message(filters.command(["user_info"]))
def user_info(client, message):
	app.send_message(message.chat.id, message)


@app.on_message(filters.private)
def hello(client, message):
	message.reply_text(message.text)


@app.on_message(filters.command(['stop']))
def stop(client, message):
	global echo
	echo = True


app.run()