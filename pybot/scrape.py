

from __future__ import print_function
import basc_py4chan
import urllib3, shutil
import os
os.system('cmd /c "color A"')
file = []
# get the board we want
board = basc_py4chan.Board('wsg')

i = 0
while i < 1000:
	i += 1
	# select the first thread on the board
	all_thread_ids = board.get_all_thread_ids()
	first_thread_id = all_thread_ids[i]
	thread = board.get_thread(first_thread_id)
	wasd = len(all_thread_ids) - 2
	if i >= wasd:
		break
	topic = thread.topic
	x = topic.subject
	if x == "YLYL":
		# print thread information
		print(thread)
		print('Sticky?', thread.sticky)
		print('Closed?', thread.closed)
		print('Replies:', len(thread.replies))

		# print topic post information
		topic = thread.topic
		print('Topic Repr', topic)
		print('Postnumber', topic.post_number)
		print('Timestamp', topic.timestamp)
		print('Datetime', repr(topic.datetime))
		print('Subject', topic.subject)
		print('Comment', topic.comment)

		post = thread.posts
		p = 0
		length = len(post) - 3
		print(len(post))

		while p < length:

			p += 1
			if post[p].has_file:
				url = post[p].file_url
				c = urllib3.PoolManager()
				if "webm" in post[p].filename:
					filename = "scraper/wsg/webm/" + post[p].filename
					file.append(filename)
					print(filename)
					with c.request('GET', url, preload_content=False) as res, open(filename, 'wb') as out_file:
						shutil.copyfileobj(res, out_file)
				else:
					filename = "scraper/wsg/" + post[p].filename
					print(filename)
					with c.request('GET', url, preload_content=False) as res, open(filename, 'wb') as out_file:
						shutil.copyfileobj(res, out_file)
	if x == "ylyl":
		# print thread information
		print(thread)
		print('Sticky?', thread.sticky)
		print('Closed?', thread.closed)
		print('Replies:', len(thread.replies))

		# print topic post information
		topic = thread.topic
		print('Topic Repr', topic)
		print('Postnumber', topic.post_number)
		print('Timestamp', topic.timestamp)
		print('Datetime', repr(topic.datetime))
		print('Subject', topic.subject)
		print('Comment', topic.comment)

		post = thread.posts
		p = 0
		length = len(post) - 3
		print(len(post))

		while p < length:

			p += 1
			if post[p].has_file:
				url = post[p].file_url
				c = urllib3.PoolManager()
				if "webm" in post[p].filename:
					filename = "scraper/wsg/webm/" + post[p].filename
					file.append(filename)
					print(filename)
					with c.request('GET', url, preload_content=False) as res, open(filename, 'wb') as out_file:
						shutil.copyfileobj(res, out_file)
				else:
					filename = "scraper/wsg/" + post[p].filename
					print(filename)
					with c.request('GET', url, preload_content=False) as res, open(filename, 'wb') as out_file:
						shutil.copyfileobj(res, out_file)
	if x == "war":
		# print thread information
		print(thread)
		print('Sticky?', thread.sticky)
		print('Closed?', thread.closed)
		print('Replies:', len(thread.replies))

		# print topic post information
		topic = thread.topic
		print('Topic Repr', topic)
		print('Postnumber', topic.post_number)
		print('Timestamp', topic.timestamp)
		print('Datetime', repr(topic.datetime))
		print('Subject', topic.subject)
		print('Comment', topic.comment)

		post = thread.posts
		p = 0
		length = len(post) - 3
		print(len(post))

		while p < length:

			p += 1
			if post[p].has_file:
				url = post[p].file_url
				c = urllib3.PoolManager()
				if "webm" in post[p].filename:
					filename = "scraper/wsg/webm/" + post[p].filename
					file.append(filename)
					print(filename)
					with c.request('GET', url, preload_content=False) as res, open(filename, 'wb') as out_file:
						shutil.copyfileobj(res, out_file)
				else:
					filename = "scraper/wsg/" + post[p].filename
					print(filename)
					with c.request('GET', url, preload_content=False) as res, open(filename, 'wb') as out_file:
						shutil.copyfileobj(res, out_file)
	if x == "WAR":
		# print thread information
		print(thread)
		print('Sticky?', thread.sticky)
		print('Closed?', thread.closed)
		print('Replies:', len(thread.replies))

		# print topic post information
		topic = thread.topic
		print('Topic Repr', topic)
		print('Postnumber', topic.post_number)
		print('Timestamp', topic.timestamp)
		print('Datetime', repr(topic.datetime))
		print('Subject', topic.subject)
		print('Comment', topic.comment)

		post = thread.posts
		p = 0
		length = len(post) - 3
		print(len(post))

		while p < length:

			p += 1
			if post[p].has_file:
				url = post[p].file_url
				c = urllib3.PoolManager()
				if "webm" in post[p].filename:
					filename = "scraper/wsg/webm/" + post[p].filename
					file.append(filename)
					print(filename)
					with c.request('GET', url, preload_content=False) as res, open(filename, 'wb') as out_file:
						shutil.copyfileobj(res, out_file)
				else:
					filename = "scraper/wsg/" + post[p].filename
					print(filename)
					with c.request('GET', url, preload_content=False) as res, open(filename, 'wb') as out_file:
						shutil.copyfileobj(res, out_file)
	if x == "War":
		# print thread information
		print(thread)
		print('Sticky?', thread.sticky)
		print('Closed?', thread.closed)
		print('Replies:', len(thread.replies))

		# print topic post information
		topic = thread.topic
		print('Topic Repr', topic)
		print('Postnumber', topic.post_number)
		print('Timestamp', topic.timestamp)
		print('Datetime', repr(topic.datetime))
		print('Subject', topic.subject)
		print('Comment', topic.comment)

		post = thread.posts
		p = 0
		length = len(post) - 3
		print(len(post))

		while p < length:

			p += 1
			if post[p].has_file:
				url = post[p].file_url
				c = urllib3.PoolManager()
				if "webm" in post[p].filename:
					filename = "scraper/wsg/webm/" + post[p].filename
					file.append(filename)
					print(filename)
					with c.request('GET', url, preload_content=False) as res, open(filename, 'wb') as out_file:
						shutil.copyfileobj(res, out_file)
				else:
					filename = "scraper/wsg/" + post[p].filename
					print(filename)
					with c.request('GET', url, preload_content=False) as res, open(filename, 'wb') as out_file:
						shutil.copyfileobj(res, out_file)
	else:
		# print thread information
		print(thread)
		print('Sticky?', thread.sticky)
		print('Closed?', thread.closed)
		print('Replies:', len(thread.replies))

		# print topic post information
		topic = thread.topic
		print('Topic Repr', topic)
		print('Postnumber', topic.post_number)
		print('Timestamp', topic.timestamp)
		print('Datetime', repr(topic.datetime))
		print('Subject', topic.subject)
		print('Comment', topic.comment)

		post = thread.posts
		p = 0
		length = len(post) - 3
		print(len(post))

		while p < length:

			p += 1
			if post[p].has_file:
				url = post[p].file_url
				c = urllib3.PoolManager()
				if "gif" in post[p].filename:
					filename = "scraper/wsg/gif/" + post[p].filename
					print(filename)
					with c.request('GET', url, preload_content=False) as res, open(filename, 'wb') as out_file:
						shutil.copyfileobj(res, out_file)
				if "jpg" in post[p].filename:
					filename = "scraper/wsg/img/" + post[p].filename
					print(filename)
					with c.request('GET', url, preload_content=False) as res, open(filename, 'wb') as out_file:
						shutil.copyfileobj(res, out_file)
				if "png" in post[p].filename:
					filename = "scraper/wsg/img/" + post[p].filename
					print(filename)
					with c.request('GET', url, preload_content=False) as res, open(filename, 'wb') as out_file:
						shutil.copyfileobj(res, out_file)

board = basc_py4chan.Board('pol')

i = 0
while i < 1000:
	i += 1
	# select the first thread on the board
	all_thread_ids = board.get_all_thread_ids()
	first_thread_id = all_thread_ids[i]
	thread = board.get_thread(first_thread_id)

	wasd = len(all_thread_ids) - 2
	if i >= wasd:
		break
	topic = thread.topic
	x = topic.subject
	if "humor" in x:
		# print thread information
		print(thread)
		print('Sticky?', thread.sticky)
		print('Closed?', thread.closed)
		print('Replies:', len(thread.replies))

		# print topic post information
		topic = thread.topic
		print('Topic Repr', topic)
		print('Postnumber', topic.post_number)
		print('Timestamp', topic.timestamp)
		print('Datetime', repr(topic.datetime))
		print('Subject', topic.subject)
		print('Comment', topic.comment)

		post = thread.posts
		p = 0
		length = len(post) - 3
		print(len(post))

		while p < length:

			p += 1
			if post[p].has_file:
				url = post[p].file_url
				c = urllib3.PoolManager()
				filename = "scraper/pol/" + post[p].filename
				print(filename)
				with c.request('GET', url, preload_content=False) as res, open(filename, 'wb') as out_file:
					shutil.copyfileobj(res, out_file)
	else:
		# print thread information
		print(thread)
		print('Sticky?', thread.sticky)
		print('Closed?', thread.closed)
		print('Replies:', len(thread.replies))

		# print topic post information
		topic = thread.topic
		print('Topic Repr', topic)
		print('Postnumber', topic.post_number)
		print('Timestamp', topic.timestamp)
		print('Datetime', repr(topic.datetime))
		print('Subject', topic.subject)
		print('Comment', topic.comment)

		post = thread.posts
		p = 0
		length = len(post) - 3
		print(len(post))

		while p < length:

			p += 1
			if post[p].has_file:
				url = post[p].file_url
				c = urllib3.PoolManager()
				if "gif" in post[p].filename:
					filename = "scraper/pol/gif/" + post[p].filename
					print(filename)
					with c.request('GET', url, preload_content=False) as res, open(filename, 'wb') as out_file:
						shutil.copyfileobj(res, out_file)
				else:
					filename = "scraper/pol/" + post[p].filename
					print(filename)
					with c.request('GET', url, preload_content=False) as res, open(filename, 'wb') as out_file:
						shutil.copyfileobj(res, out_file)


allfiles = [f for f in listdir("scraper/wsg/mp4/") if isfile(join("scraper/wsg/mp4/" , f))]
ii = 0
while ii < len(allfiles):
    file = allfiles[ii]
    for x in allfiles:
        if os.path.exists("scraper/wsg/mp4/" + file):
            os.remove("scraper/wsg/mp4/" + file)
    ii += 1

i = 0
length = len(file)
print(file[0])
while i < length:
	filepath = file[i]
	filepathh = filepath.replace("webm", "mp4")
	command = 'cmd /c "cd ffmpeg-20200106-1e3f4b5-win64-static/bin & ffmpeg -i ' + filepath + " " + filepathh + ' " '
	os.system(command)
	i += 1
