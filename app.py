import streamlit as st
from groq import Client
from dotenv import load_dotenv
import os
from streamlit_option_menu import option_menu

# Load environment variables from .env file
load_dotenv()

# Set up the Groq client using the API key from secrets or environment
api_key = st.secrets["GROQ_API_KEY"]
client = Client(api_key=api_key)

# Set model names
conversational_model = "llama-3.1-8b-instant"
safety_model = "llama-guard-3-8b"

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Main Page", "Write an Email", "Reply to an Email", "Contact"],
        menu_icon="cast",
        icons=["house", "envelope", "reply", "person-fill"],
    )


# Function to check email content for safety using Llama Guard
def check_email_safety(content):
    try:
        completion = client.chat.completions.create(
            model=safety_model,
            messages=[{"role": "user", "content": content}],
            max_tokens=10,
            temperature=0.0,
        )

        response = completion.choices[0].message.content.lower()
        if "unsafe" in response:
            raise ValueError("Llama Guard detected potentially unsafe content in the generated email.")
    except Exception as e:
        raise ValueError(f"An error occurred during the safety check: {e}")


# Main Page
if selected == "Main Page":
    st.image("powered_by_groq.svg", width=200)
    st.title("Welcome to GroqMail: The AI-Powered Email Assistant")

    st.write("""
    GroqMail leverages cutting-edge generative AI to help you draft and reply to emails effortlessly. 
    Whether you need to write a formal email to a colleague or craft a friendly note to a friend, GroqMail has you covered.
    """)

    st.header("Features")
    st.write("""
    - **Write an Email**: Generate custom emails based on your specific needs, tone, and relationship with the recipient.
    - **Reply to an Email**: Craft thoughtful and appropriate responses to the emails you receive.
    """)

    st.header("How to Use GroqMail")
    st.write("""
    1. Navigate using the menu on the left.
    2. Choose between writing a new email or replying to an existing one.
    3. Fill in the required information such as the recipient's name, your relationship with them, the purpose of the email, and the preferred tone.
    4. Hit the "Go" button and let GroqMail generate a tailor-made email for you.
    """)

    st.write("Start crafting your emails with ease and confidence. Choose an option from the sidebar to begin!")
    st.divider()

# Write an Email Page
if selected == "Write an Email":
    st.image("powered_by_groq.svg", width=200)
    st.title("GroqMail: The AI-Powered Email Assistant")
    st.write(
        "Use GroqMail to craft personalized emails effortlessly. Just fill in the details about the recipient, your relationship, the email's purpose, and the tone you'd like to set. GroqMail will then generate a bespoke email that you can send with confidence.")
    st.divider()

    # Input fields
    recipient = st.text_input("Recipient Name", placeholder="Enter the recipient's name")
    recipient_rel = st.text_input("Relationship with Recipient", placeholder="E.g., colleague, friend, client")
    purpose = st.text_area("Purpose of the Email", placeholder="Describe the purpose of the email and provide context")
    selected_tone = st.selectbox("Tone of the Email", ["Formal", "Informal", "Friendly", "Professional", "Persuasive"])
    selected_length = st.radio("Length of the Email", ["Brief", "Descriptive"])

    # Generate Email Button
    if st.button(label="Generate Email"):
        if not recipient or not recipient_rel or not purpose:
            st.error("Please ensure all fields are filled out.")
        else:
            # Construct prompt
            prompt = f'''
            You are an AI email assistant. Given the following inputs, compose an email that addresses the recipient by name, fulfills the specified purpose, matches the desired tone, and adheres to the requested length.
            Email Recipient: {recipient}
            Relationship with Recipient: {recipient_rel}
            Purpose: {purpose}
            Tone: {selected_tone}
            Length: {selected_length}
            '''

            with st.spinner('Generating your email...'):
                try:
                    # Generate email using Groq's Llama Versatile model
                    completion = client.chat.completions.create(
                        model=conversational_model,
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=150,
                    )
                    result = completion.choices[0].message.content

                    # Check the generated email for safety
                    check_email_safety(result)

                    st.write(result)
                    st.success("Email generated successfully!")
                except ValueError as ve:
                    st.error(str(ve))
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

    st.divider()

# Reply to an Email Page
if selected == "Reply to an Email":
    st.image("powered_by_groq.svg", width=200)
    st.title("GroqMail: The AI-Powered Email Assistant")
    st.write(
        "Responding to emails has never been easier. Provide GroqMail with the email you've received, your relationship with the sender, and the details you wish to include in your reply. Choose the tone, and GroqMail will generate a thoughtful response for you.")
    st.divider()

    # Input fields
    received = st.text_area("Email Received", placeholder="Paste the email you received here")
    sender_rel = st.text_input("Relationship with Sender", placeholder="E.g., boss, colleague, family member")
    details = st.text_area("Details for Reply",
                           placeholder="Include any key points or information you'd like in your reply")
    selected_tone = st.selectbox("Tone of the Reply", ["Formal", "Informal", "Friendly", "Professional", "Persuasive"])
    selected_length = st.radio("Length of the Reply", ["Brief", "Descriptive"])

    # Generate Reply Button
    if st.button(label="Generate Reply"):
        if not received or not sender_rel or not details:
            st.error("Please ensure all fields are filled out.")
        else:
            # Construct prompt
            prompt = f'''
            You are an AI email assistant. Given the following inputs, compose an email reply that addresses the recipient by name, fulfills the specified purpose, matches the desired tone, and adheres to the requested length.
            Email Received: {received}
            Relationship with Recipient: {sender_rel}
            Details: {details}
            Tone: {selected_tone}
            Length: {selected_length}
            '''

            with st.spinner('Generating your email reply...'):
                try:
                    # Generate reply using Groq's Llama Versatile model
                    completion = client.chat.completions.create(
                        model=conversational_model,
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=150,
                    )
                    result = completion.choices[0].message.content

                    # Check the generated reply for safety
                    check_email_safety(result)

                    st.write(result)
                    st.success("Reply generated successfully!")
                except ValueError as ve:
                    st.error(str(ve))
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

    st.divider()
if selected == "Contact":
    st.title("Contact Me")
    st.write("Feel free to reach out to me:")
    st.divider()
    st.write(f"🔗 LinkedIn: [linkedin.com/in/maxmlang](https://www.linkedin.com/in/maxmlang/)")
    st.write(f"👨‍💻 GitHub: [github.com/MaxMLang](https://github.com/MaxMLang)")
    st.write(f"🌐 Portfolio: [maxmlang.github.io](https://maxmlang.github.io/)")
    st.divider()


