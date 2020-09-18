from PIL import Image
import random


def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst
	
	
	


board = []
possible_num = list(range(1, 26))
print(possible_num)
possible_num.remove(13)
print(possible_num)


# i == 2 and j == 2 is free space

for i in range(0, 5):
	temp = []
	for j in range (0, 5):
		if i == 2 and j == 2:
			temp.append(13)
			pass
		else:
			num = random.choice(possible_num)
			possible_num.remove(num)
			temp.append(num)
	board.append(temp)
	
for row in board:
	print(row)
	


for y in range (0, 5):
	for x in range(0, 5):
		if x == 0:
			temp_filename = "bingo/" + str(board[y][x]) + ".png"
			seed_img = Image.open(temp_filename)
		elif y == 2 and x == 2:
			temp_filename = "bingo/13free.png"
			temp_img = Image.open(temp_filename)
			seed_img = get_concat_h(seed_img, temp_img)
		else:
			print(str(y) + " " + str(x))
			print(str(board[y][x]))
			temp_filename = "bingo/" + str(board[y][x]) + ".png"
			temp_img = Image.open(temp_filename)
			seed_img = get_concat_h(seed_img, temp_img)
	if y == 0:
		seed_row = seed_img
	else:
		seed_row = get_concat_v(seed_row, seed_img)

#106, 633

base_img = Image.open("bingo/base_board.jpg")

base_img.paste(seed_row, (106, 633))

base_img.save("bingo/generated_board.png")