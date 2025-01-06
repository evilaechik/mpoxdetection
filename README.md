# **Monkeypox Detection Bot**

## **Overview**
The Monkeypox Detection Bot is an AI-based solution designed to assist healthcare professionals in diagnosing skin diseases, including mpox (monkeypox), measles, chickenpox, cowpox, HFMD, and healthy skin conditions. Using a fine-tuned VGG16 convolutional neural network, the bot achieves an impressive **95% accuracy** and is accessible via a Telegram chatbot.
We, Artyom Lavrentyev and Yedigeyev Galym, have implemented this bot in website which we run on local host.

---

## **Features**
- **AI-Powered Diagnostics**: Classifies six different skin conditions with high accuracy.
- **Scalable Deployment**: Accessible through a Telegram bot for remote healthcare support.
- **Pre-Trained Model**: Built on the robust VGG16 architecture for efficient image analysis.
- **Healthcare Innovation**: Supports early diagnosis and reduces the burden on healthcare systems.

---

## **How It Works**
1. **Image Input**: Users upload a skin lesion image via the Telegram bot.
2. **Processing**: The image is processed using the fine-tuned VGG16 neural network.
3. **Output**: The bot returns a classification of the skin condition along with an accuracy score.

---

## **Technical Details**
- **Frameworks**: Keras, TensorFlow
- **Model**: VGG16, fine-tuned for multi-class classification
- **Dataset**: MSLD v2.0, containing over 500 images across six categories
- **Performance**:
  - Accuracy: **95%**
  - Precision: **97%**
  - Recall: **94%**
  - F1-Score: **95%**

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/evilaechik/mpoxdetection.git
cd mpoxdetection
```

### **2. Install Dependencies**
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### **3. Configure Telegram Bot**
1. Set up a bot using [BotFather](https://core.telegram.org/bots#botfather) on Telegram.
2. Add your bot token as an environment variable:
   ```bash
   export TELEGRAM_TOKEN="your-bot-token"
   ```

### **4. Run the Bot**
Start the Telegram bot:
```bash
python bot.py
```

---

## **Usage**
1. Open the Telegram bot.
2. Upload a clear image of a skin lesion.
3. Receive diagnostic results, including the classification and confidence score.

---

## **Contributing**
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

---

## **License**
This project is licensed under a **custom license**. The code for the training algorithm and Telegram bot is available for educational purposes only. The trained model is proprietary and cannot be downloaded, modified, or redistributed.

---

## **Acknowledgments**
- **Dataset**: MSLD v2.0  
- **Frameworks**: TensorFlow, Keras  
- Special thanks to everyone who supported the development of this project.

---

## **Contact**
For any inquiries, feel free to reach out:
- **Email**: artem@stemolympiads.kz
-            galymtashtek@gmail.com   
- **GitHub**: [evilaechik](https://github.com/evilaechik)
-             [Galym7707](https://github.com/Galym7707) 
