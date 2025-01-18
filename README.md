# **PixelPerfect AI** 📸🤖: Unlocking Visual Intelligence with AI

Welcome to **PixelPerfect AI** 🚀, an advanced image analysis tool that leverages the power of **Generative AI** to provide intelligent, insightful responses based on any uploaded image. Whether it's identifying objects, interpreting visual features, or understanding the context, **PixelPerfect AI** brings **Visual Intelligence** to life, allowing you to interact with images like never before! 🌟

---

## **Features** ✨

- **Seamless Image Upload**: Easily upload images in formats like JPG, PNG, or JPEG. 🖼️
- **Generative AI Insight**: Ask any question about the image and receive AI-powered insights instantly. 💬
- **Interactive UI**: Simple and elegant user interface built with **Streamlit** for smooth and engaging user interaction. 🖥️
- **Real-time Analysis**: Get instant responses based on your image content in a matter of seconds. ⏱️
- **AI Accuracy**: Powered by Google’s **Generative AI** (Gemini-1.5-Flash) for high-quality, context-aware analysis. 🔍

---

## **Screenshots** 📸

### Homepage
![Homepage](https://github.com/abhinishtiwari/PixelPerfect-AI/blob/52fc870aa7a3d3240e2a31708a795a9b21ff7855/Screenshot%20(547).png)

### Image Upload and Analysis
![Image Upload](https://github.com/abhinishtiwari/PixelPerfect-AI/blob/52fc870aa7a3d3240e2a31708a795a9b21ff7855/Screenshot%20(548).png)

### AI-Generated Insights
![AI Insights](https://github.com/abhinishtiwari/PixelPerfect-AI/blob/52fc870aa7a3d3240e2a31708a795a9b21ff7855/Screenshot%20(551).png)

---

## **Technologies Used** 🛠️

- **Python 3.7+** 🐍
- **Streamlit** for building interactive web apps 🌐
- **Google Generative AI** (Gemini-1.5-Flash) for content generation 💡
- **Pillow** for image processing 🖼️
- **ngrok** for public URL creation (optional) 🌍

---

## **Installation Guide** 📥

### 1. **Clone the repository**  
Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/abhinishtiwari/PixelPerfect-AI.git
cd PixelPerfect-AI
```

### 2. **Install required dependencies**  
Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### 3. **Set up Google Generative AI API Key**  
To use Google's AI model, you'll need to configure your **API key**. Follow these steps:

- Create an API key from [Google Cloud Console](https://console.cloud.google.com/).
- Replace the `api_key` variable in the `app.py` file with your own key:

```python
api_key = "YOUR_GOOGLE_GENERATIVE_AI_API_KEY"
```

### 4. **Run the app locally**  
Run the application with the following command:

```bash
streamlit run app.py
```

Once the app starts, you can open it in your browser by navigating to `http://localhost:8501`.

---

## **How It Works** 🔧

1. **Upload an Image**: Click on the "Choose a file" button and select an image file (JPG, PNG, JPEG). 🖼️
2. **Ask a Question**: Enter a question related to the image, such as "What objects are in this image?" or "Describe the color of the object". 🤔
3. **Get AI Response**: Press the "Generate Insight" button, and receive AI-powered analysis in seconds. ⚡
4. **Explore Insights**: **PixelPerfect AI** will generate responses related to the visual content, such as object identification, color description, and other contextual information. 💬

---

## **Charts and Visual Insights** 📊

In this project, various insights are analyzed, such as:
- **Image Quality & AI Response Accuracy**: Higher-quality images improve AI response accuracy. 📈
- **User Interaction Trends**: Insights into which questions users prefer to ask. 🗣️
- **Response Time Analysis**: Understanding how image size affects response time. ⏱️
- **AI Insight Accuracy**: Evaluating the accuracy of the AI’s answers for different types of questions. 🎯

Charts visualizing these insights can be found in the `assets` folder, showcasing the project's performance and user engagement data.

---

## **Contributing** ✍️

We welcome contributions to make **PixelPerfect AI** even better! To contribute, please follow these steps:

---

## **Contact** 📬

For any queries or issues, feel free to contact me:

- **Abhinish Tiwari**
  - [GitHub](https://github.com/abhinishtiwari) 🖥️
  - [Portfolio](https://abhinishtiwari.github.io/Portfolio/) 🌐
  - [LinkedIn](https://www.linkedin.com/in/abhinish-tiwari-945914260/) 👔
  - **Email**: abhinishtiwari03@gmail.com 📧

---

## **Acknowledgements** 🙏

- **Streamlit** for making app development seamless and interactive. 🌟
- **Google Generative AI** for providing the backbone for the image analysis. 🔮
- **Pillow** for handling image operations and transformations. 🖼️
