import streamlit as st
import numpy as np
import random
import time
from PIL import Image
import io

if "page" not in st.session_state:
    st.session_state.page = "main"

if st.session_state.page == "main":
	st.title('hello, love')
	st.title("happy st. valentine's day")
	st.image('welcome.jpg')
	st.title('i prepared some quests for you')
	start = st.button('start', use_container_width = True)

	if start:
		#st.switch_page('pages/1_quiz.py')
		st.session_state.page = "quiz"

elif st.session_state.page == "quiz":
	st.title('quest 1: quiz')
	st.subheader('welcome to the first quest of the game. to pass it you will need to complete this mini-quiz:')

	answers = []
	feedbacks = []

	st.subheader('question 1:')
	answers.append(st.radio('when did we start dating?', ['5 october', '7 september', '7 october', '12 september']))
	feedbacks.append(st.empty())

	st.subheader('question 2:')
	answers.append(st.radio('what is the name of the pigeon you gifted me?', ['pablo', 'pip', 'clover', 'vladislav']))
	feedbacks.append(st.empty())

	st.subheader('question 3:')
	answers.append(st.radio('which project did we do togetra for the statistical learning class?', ['digit classification', 'cat-dog classification', 'usd-try forecasting', 'body fat percentage prediction']))
	feedbacks.append(st.empty())

	st.subheader('question 4:')
	answers.append(st.radio('which game did you play when you first came to my room?', ['hogwarts', 'assassins creed', 'red dear redemption', 'lego']))
	feedbacks.append(st.empty())

	st.subheader('question 5:')
	answers.append(st.radio('which is not a part of my (usual) breakfast?', ['overnight oats', 'portakalli kahve', 'a sun ray', 'peanut cikolata']))
	feedbacks.append(st.empty())

	st.subheader('question 6:')
	answers.append(st.radio('from the given, what would i do if i could do only one thing to you?', ['kiss', 'hug', 'bite', 'be sad that i can do only one']))
	feedbacks.append(st.empty())

	st.subheader('question 7:')
	answers.append(st.radio("who wrote the song 'numb'?", ['linkin park', 'nirvana', 'arctic monkeys', 'жігіттер']))
	feedbacks.append(st.empty())

	st.subheader('question 8:')
	answers.append(st.radio('renklerden bir yay, ama onunla ok atılmaz. yağmurun peşine takılır, kara takılmaz.', ['görünüş', 'gökkuşağı', 'sandalye', 'pense']))
	feedbacks.append(st.empty())

	st.subheader('question 9:')
	answers.append(st.radio('what was not there on our first ever turkish night?', ['sarma', 'içli köfte', 'mantı', 'mercimek köftesi']))
	feedbacks.append(st.empty())

	st.subheader('question 10:')
	answers.append(st.text_input('How would you describe me in one word?'))
	feedbacks.append(st.empty())

	done = st.button('done')

	correct = ['7 october', 'pablo', 'usd-try forecasting', 'hogwarts', 'a sun ray', 'be sad that i can do only one', 'linkin park', 'gökkuşağı', 'mercimek köftesi']

	if "quiz_completed" not in st.session_state:
		st.session_state.quiz_completed = False

	if done or st.session_state.quiz_completed:
		st.session_state.quiz_completed = True
		num_correct = 0
		for i in range(9):
			if answers[i] == correct[i]:
				feedbacks[i].success('yaaay, good job, love')
				num_correct += 1
			else:
				feedbacks[i].error('IIIIHHHH')
		feedbacks[9].success('aaaaawwwww, i love you')

		if num_correct == 9:
			st.title('good job, you did it perfectly!')
			st.image('good job quiz.jpg')
			st.title('now we move on the next quest')

			moveon = st.button('move on', use_container_width = True)

			if moveon:
				st.session_state.page = "tic-tac-toe"
				st.rerun()

		else:
			st.title('ooh noo, you have some mistakes')
			st.image('not perfect quiz.jpg')
			st.title('try again, please')

elif st.session_state.page == "tic-tac-toe":
	st.title('quest 2: tic tac toe')

	st.write('now we will play tic-tac-toe')

	if "tictactoe_completed" not in st.session_state:
		st.session_state.tictactoe_completed = False

	if "board" not in st.session_state:
	    st.session_state.board = np.full((3, 3), "", dtype=str)
	    st.session_state.current_player = "X"
	    st.session_state.winner = None

	def check_winner():
	    board = st.session_state.board
	    for i in range(3):
	        if board[i, 0] == board[i, 1] == board[i, 2] and board[i, 0] != "":
	            return board[i, 0]
	        if board[0, i] == board[1, i] == board[2, i] and board[0, i] != "":
	            return board[0, i]
	    if board[0, 0] == board[1, 1] == board[2, 2] and board[0, 0] != "":
	        return board[0, 0]
	    if board[0, 2] == board[1, 1] == board[2, 0] and board[0, 2] != "":
	        return board[0, 2]
	    if "" not in board:
	        return "Draw"
	    return None

	def computer_move():
	    empty_cells = [(r, c) for r in range(3) for c in range(3) if st.session_state.board[r, c] == ""]
	    if empty_cells:
	        r, c = random.choice(empty_cells)
	        st.session_state.board[r, c] = "O"

	for row in range(3):
	    cols = st.columns(3)
	    for col in range(3):
	        with cols[col]:
	            if st.button(st.session_state.board[row, col] or " ", key=f"{row}-{col}", use_container_width = True):
	                if st.session_state.board[row, col] == "" and st.session_state.winner is None:
	                    # Player move
	                    st.session_state.board[row, col] = "X"
	                    st.session_state.winner = check_winner()

	                    # Computer move if game not over
	                    if st.session_state.winner is None:
	                        computer_move()
	                        st.session_state.winner = check_winner()

	if st.session_state.winner:
	    if st.session_state.winner == "Draw":
	        st.warning("it's a draw! we will play until you win")
	    elif st.session_state.winner == 'X':
	    	st.title('everytime she wins ya everytime')
	    	st.image('she won tictactoe.jpg')
	    	st.title('off yaa off yaa')
	    	st.title('tamam, next quest')

	    	moveon = st.button('move on', use_container_width = True)
	    	
	    	if moveon:
	    		st.session_state.page = "memory-matching"

	    elif st.session_state.winner == 'O':
	    	st.title('muhahahaha, i won')
	    	st.image('i won tictactoe.jpg')
	    	st.title('start again')

	    	if st.button("restart"):
	    		st.session_state.board = np.full((3, 3), "", dtype=str)
	    		st.session_state.current_player = "X"
	    		st.session_state.winner = None

elif st.session_state.page == 'memory-matching':
	st.title('quest 3: match the photos')
	st.write('this is a memory game. choose two photos, they will need to match')

	image_urls = [
	"image_1.jpg", "image_2.jpg", "image_3.jpg", "image_4.jpg",
	"image_5.jpg", "image_6.jpg", "image_7.jpg", "image_8.jpg"]

	if "cards" not in st.session_state:
		images = image_urls * 2  # Duplicate images for pairs
		random.shuffle(images)  # Shuffle the cards
		st.session_state.cards = images
		st.session_state.revealed = [False] * 16  # Track revealed cards
		st.session_state.selected = []  # Track selected cards
		st.session_state.matched = set()  # Track matched pairs

	cols = st.columns(4)
	for i in range(16):
		with cols[i % 4]:  # Place in correct column
			if st.session_state.revealed[i] or i in st.session_state.matched:
				st.image(st.session_state.cards[i], use_container_width=True)
			else:
				if st.button("?", key=f"card_{i}", use_container_width=True):
					st.session_state.revealed[i] = True
					st.session_state.selected.append(i)

	if len(st.session_state.selected) == 2:
		idx1, idx2 = st.session_state.selected
		if st.session_state.cards[idx1] == st.session_state.cards[idx2]:
			st.session_state.matched.update([idx1, idx2])  # Mark as matched
		else:
			time.sleep(1)  # Delay before hiding cards again
			st.session_state.revealed[idx1] = False
			st.session_state.revealed[idx2] = False
		st.session_state.selected.clear()
		st.rerun()

	if len(st.session_state.matched) == 16:
		st.title('yaaay, good job, love')
		st.image('after-matching.jpg')
		st.title("that's it")
		moveon = st.button('move on', use_container_width = True)
		
		if moveon:
			st.session_state.page = "finish"

elif st.session_state.page == "finish":
	st.title('good job, love')
	st.image('finish.jpg')
	st.title('i love you')