import streamlit as st
from dotenv import load_dotenv
import os
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load environment variables
load_dotenv()

# Configure OpenAI API
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the ChatOpenAI model with gpt-4
llm = ChatOpenAI(api_key=openai_api_key, temperature=0.7, model="gpt-4o")

# Function to extract video ID from different YouTube link formats
def extract_video_id(youtube_link):
    if "v=" in youtube_link:
        video_id = youtube_link.split("v=")[1]
        video_id = video_id.split("&")[0]
        return video_id
    elif "youtu.be" in youtube_link:
        return youtube_link.split("/")[-1]
    elif "embed/" in youtube_link:
        return youtube_link.split("embed/")[1]
    else:
        raise ValueError("Invalid YouTube link format")

# Function to extract transcript details with caching
@st.cache_data
def extract_transcript_details(youtube_video_url):
    try:
        video_id = extract_video_id(youtube_video_url)
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([i["text"] for i in transcript_text])
        return transcript
    except Exception as e:
        st.error(f"Error fetching transcript: {e}")
        return None

# Function to split transcript into chunks
def split_text_into_chunks(text, chunk_size=1000, chunk_overlap=200):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = text_splitter.split_text(text)
    return chunks

# Function to summarize chunks and refine the final summary
def summarize_transcript(transcript_text, summary_length):
    try:
        # Split the transcript into chunks
        chunks = split_text_into_chunks(transcript_text, chunk_size=1000, chunk_overlap=200)
        
        # Summarize each chunk
        summaries = []
        for chunk in chunks:
            summary = summarization_chain.run(text=chunk)
            summaries.append(summary)
        
        # Combine the summaries into a single text
        combined_summary = " ".join(summaries)
        
        # Refine the combined summary to make it concise and coherent
        refined_summary = summarization_chain.run(text=combined_summary)
        
        # Truncate to match word limit
        if len(refined_summary.split()) > summary_length:
            refined_summary = " ".join(refined_summary.split()[:summary_length])
        return refined_summary
    except Exception as e:
        st.error(f"Error summarizing transcript: {e}")
        return None

# Function to generate key takeaways
def generate_key_takeaways(transcript_text):
    try:
        # Define the prompt for key takeaways
        key_takeaways_prompt = PromptTemplate(
            input_variables=["text"],
            template="""Extract the key takeaways from the following text. Present them as a bullet-point list.
            Text: {text}

            Key Takeaways:
            -"""
        )
        # Initialize the key takeaways chain
        key_takeaways_chain = LLMChain(llm=llm, prompt=key_takeaways_prompt)
        # Generate key takeaways
        key_takeaways = key_takeaways_chain.run(text=transcript_text)
        return key_takeaways
    except Exception as e:
        st.error(f"Error generating key takeaways: {e}")
        return None

# Streamlit app
st.title("YouTube Video Summarizer")
youtube_link = st.text_input("Enter YouTube Video Link:")

# Add a slider for summary length
summary_length = st.slider(
    "Select Summary Length (in words)",
    min_value=100,
    max_value=500,
    value=150,  # Default value
    step=50
)

if youtube_link:
    try:
        video_id = extract_video_id(youtube_link)
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width =True)
    except ValueError as e:
        st.error(str(e))

if st.button("Get Summary"):
    with st.spinner("Fetching transcript..."):
        transcript_text = extract_transcript_details(youtube_link)
    
    if transcript_text:
        # Define the prompt template for summarization
        prompt_template = PromptTemplate(
            input_variables=["text"],
            template=f"""You are a YouTube video summarizer. Your task is to summarize the entire video transcript in a concise yet comprehensive manner. 
            The summary should:
            1. Cover all the key points discussed in the video.
            2. Be easy to read and understand.
            3. Be no longer than {summary_length} words.
            4. Avoid unnecessary details or repetition.

            Transcript: {{text}}

            Summary:"""
        )

        # Initialize the summarization chain
        summarization_chain = LLMChain(llm=llm, prompt=prompt_template)

        with st.spinner("Summarizing transcript..."):
            summary = summarize_transcript(transcript_text, summary_length)
        
        if summary:
            st.markdown("## Summary:")
            st.write(summary)

            # Generate and display key takeaways
            with st.spinner("Generating key takeaways..."):
                key_takeaways = generate_key_takeaways(transcript_text)
            
            if key_takeaways:
                st.markdown("## Key Takeaways:")
                st.write(key_takeaways)