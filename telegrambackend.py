import os
import telebot
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

bot = telebot.TeleBot('token') # for privacy reasons im not showing my telegram token 
model = load_model('simple_model.keras')

label_mapping = {
    0: 'Chickenpox',
    1: 'Cowpox',
    2: 'Hand, foot and mouth disease',
    3: 'Healthy',
    4: 'Measles',
    5: 'Monkeypox'
}


def resize_image(input_image_path, output_image_path, size=(128, 128)):
    print(f"Resizing image at: {input_image_path}")
    with Image.open(input_image_path) as img:
        img_resized = img.resize(size)
        img_resized.save(output_image_path)
    print(f"Resized image saved as {output_image_path}")


def preprocess_image(image_path):
    with Image.open(image_path) as img:
        img = img.convert('RGB') 
        img_array = np.array(img)
    img_array = img_array.astype('float32') / 255.0
    img_array = np.expand_dims(img_array, axis=0)  
    return img_array



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Send me an image of a skin lesion, and I'll try to identify it.")

@bot.message_handler(content_types=['photo'])
def handle_image(message):
    try:
       
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        
        input_image_path = 'input_image.jpg'
        resized_image_path = 'resized_image.jpg'
        
        
        with open(input_image_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        
        
        resize_image(input_image_path, resized_image_path)
        
        
        processed_image = preprocess_image(resized_image_path)
        
        
        prediction = model.predict(processed_image)
        predicted_class = np.argmax(prediction, axis=1)[0]
        disease_name = label_mapping[predicted_class]
        
       
        bot.reply_to(message, f"Prediction: {disease_name} ({prediction[0][predicted_class] * 100:.2f}% confidence)")
    
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")
        print(f"Error: {e}")


bot.polling()
