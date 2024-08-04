from PIL import Image, ImageDraw, ImageFont
print("ГЕНЕРАТОР МЕМОВ ЗАПУЩЕН!")

top_text = input("Введи верхнюю часть текста: ")
bottom_text = input("Введи нижнюю часть текста: ")

print(top_text, bottom_text)

print("Список картинок:")
print("1. Джотаро ловит пулю")
print("2. Джотаро стыдно ")
print("3. удевлённый Джоске")

image_number = int(input("Введите номер картинки: "))

if image_number == 1:
  image_file = "джотаро ловит пулю.jpg"
elif image_number == 2:
  image_file = "джотаро стыдно.jpg"
elif image_number == 3:
  image_file = "удевлённый джоске.jpg"
else:
  print("такой картинки нет")

image = Image.open(image_file)
width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=130)


text = draw.textbbox((0, 0), top_text, font)
draw.text(((width - text[2]) / 2, 10), top_text, font=font, fill="white")

text = draw.textbbox((0, 0), bottom_text, font)
draw.text(((width - text[2]) / 2, height - text[3] - 10), bottom_text, font=font, fill="white")

image.save("new_meme.jpg")