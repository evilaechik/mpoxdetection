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
# Setup Instructions to Website Application

## Prerequisites
Before setting up this project, ensure you have the following installed on your system:
- [Python 3.8 or higher](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [Git LFS](https://git-lfs.github.com/)
- A code editor or IDE of your choice (e.g., [VS Code](https://code.visualstudio.com/))
- [Virtualenv](https://virtualenv.pypa.io/) (optional, but recommended for managing dependencies)

---

## Step 1: Clone the Repository
1. Open a terminal or command prompt.
2. Clone the repository to your local machine using Git:
   ```bash
   git clone git@github.com:evilaechik/mpoxdetection.git
   ```
3. Navigate into the project directory:
   ```bash
   cd mpoxdetection
   ```

---

## Step 2: Install Git LFS
This project uses Git Large File Storage (LFS) for managing large files. Install and initialize Git LFS:
1. Install Git LFS by following the instructions for your operating system: https://git-lfs.github.com/
2. Initialize Git LFS in the repository:
   ```bash
   git lfs install
   ```

---

## Step 3: Install Dependencies
It is recommended to use a virtual environment to manage dependencies.

1. Create a virtual environment (optional):
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Step 4: Configure the Project
If the project requires configuration (e.g., API keys, database settings), create and edit the `.env` file.

1. Create a `.env` file in the root directory:
   ```bash
   cp .env.example .env
   ```
2. Open the `.env` file and update the necessary environment variables.

---

## Step 5: Run the Project
Run the project locally to ensure everything is working correctly:
```bash
python app.py
```

---

## Step 6: Verify Installation
1. Open your browser and navigate to the URL specified in the console (e.g., `http://127.0.0.1:5000/`).
2. Ensure all functionality is working as expected.

---

## Troubleshooting
- **Error: Permission denied (publickey)**: Ensure you have added your SSH key to your GitHub account. Follow the instructions here: [Adding an SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).
- **Dependencies not installing**: Make sure you are using the correct version of Python and that your virtual environment is activated.
- **Missing large files**: Ensure Git LFS is installed and initialized. Run `git lfs pull` to fetch large files.

---

If you encounter issues during setup, feel free to create an issue in the repository or reach out to the repository maintainers for assistance.

## **Setup Instructions to Telegram Bot**

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
  galymtashtek@gmail.com   
- **GitHub**: [evilaechik](https://github.com/evilaechik)
  [Galym7707](https://github.com/Galym7707) 
