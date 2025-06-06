# Youtube-Video-Summarizer

## Overview
The **YouTube Video Summarizer** is a Streamlit-based web application that allows users to input a YouTube video link and get a detailed summary of the video's transcript. The app uses OpenAI's GPT models (via LangChain) to generate concise and meaningful summaries. It also includes a **Key Takeaways** section, providing a bullet-point list of the most important points from the video.

## Flow of the Project
![Youtube Video Summarizer Architecture](https://github.com/user-attachments/assets/9d4109f2-0479-4fb9-a202-838ad8862cc2)


## Demo Video
[Final_YoutubeVideoSummarizer.webm](https://github.com/user-attachments/assets/7cd3654d-826b-4e61-b5f2-be64fff99d38)


## Features
- **Transcript Extraction**: Automatically fetches the transcript of a YouTube video.
  
- **AI-Powered Summarization**: Uses OpenAI's GPT models to generate a summary of the video.
  
- **Key Takeaways**: Provides a bullet-point list of the most important points from the video.
  
- **Customizable Summary Length**: Users can select the summary length (100–500 words) using a slider.

- **Caching**: Caches transcript data to avoid redundant API calls.

- **Error Handling**: Gracefully handles errors like invalid links or missing transcripts.

## Tech Stack
- **Python**: For developing backend logic and integrating with AI models.

- **Streamlit**: For building the web application.
  
- **OpenAI GPT Model**: For generating summaries and answering questions using ```gpt-4o```.
  
- **Langchain**: For managing interactions with the OpenAI API and handling text chunking.

- **YouTube Transcript API**: For extracting video transcripts.

- **Python-dotenv**: For managing environment variables.
  
  
## Steps to Run the **Youtube Video Summarizer** on Your Local Machine:
- ### Clone the Repository
Open a terminal and run the following command to clone the repository:

```
git clone https://github.com/AmaanSyed110/Youtube-Video-Summarizer.git
```
- ### Set Up a Virtual Environment
It is recommended to use a virtual environment for managing dependencies:

```
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```
- ### Install Dependencies
Install the required packages listed in the ```requirements.txt``` file
```
pip install -r requirements.txt
```
- ### Add Your OpenAI API Key
Create a ```.env``` file in the project directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```
- ### Run the Application
Launch the Streamlit app by running the following command:
```
streamlit run app.py
```
