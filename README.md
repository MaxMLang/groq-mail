# GroqMail - The AI-Powered Email Assistant

<img src="powered_by_groq.svg" style="width: 300px; height: auto;">

## Overview

**GroqMail** is a sophisticated email assistant designed to streamline your email communication with the power of AI, ensuring every message is crafted professionally, effectively, and securely. Leveraging **Llama Guard 3 8B** powered by Groq for robust content filtering, GroqMail maintains a high standard of safety by analyzing generated email content for potentially unsafe language, making it a reliable choice for business and personal use.

This project is created for the **Groq Bounty** competition, showcasing the capabilities of Groq’s Llama Guard in ensuring safe, AI-powered email generation.


## Why This Project Matters

Email communication is a critical aspect of both personal and business interactions, and AI-powered tools like GroqMail can save users time, enhance professionalism, and improve communication efficiency. However, as AI applications generate content autonomously, maintaining safety becomes essential, especially when inappropriate or harmful content could damage business reputation or compromise user trust.

**GroqMail** addresses this by integrating **Llama Guard 3 8B** for real-time content safety checks, ensuring that every generated email aligns with safety standards. This integration underscores the importance of reliable and safe AI tools in sensitive areas like business communications.

## Features

- **Content Filtering with Llama Guard**: Every generated email is checked by **Llama Guard 3 8B** for unsafe content. If inappropriate content is detected, it raises an alert, ensuring that only safe emails are displayed.
- **AI-Driven Email Generation**: Users can generate custom emails for various tones (formal, friendly, professional) and relationships, tailoring each email to the context.
- **Easy-to-Use Interface**: A streamlined, user-friendly interface built with Streamlit that allows users to quickly draft or respond to emails with minimal input.
- **Groq-Powered Badge**: Displays a "Powered by Groq" badge in the UI, showcasing the advanced technology behind GroqMail.

## How to Run the App

### Prerequisites

- Python 3.7 or higher
- Required packages: `Streamlit`, `groq-sdk`, `python-dotenv`, `streamlit-option-menu`

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/groqmail.git
   cd groqmail
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory with your Groq API key.
   ```env
   GROQ_API_KEY=your_groq_api_key
   ```

4. **Run the App**:
   ```bash
   streamlit run app.py
   ```

5. **Access the App**:
   Open your browser and navigate to `http://localhost:8501`.

### Using the App

1. **Navigate Using the Sidebar**: Select the function you need (Main Page, Write an Email, Reply to an Email).
2. **Write an Email**: Fill in the recipient's name, relationship, email purpose, tone, and length. GroqMail generates a custom email for you.
3. **Reply to an Email**: Paste the received email, specify the relationship with the sender, and any details for your response. GroqMail generates a context-aware reply.
4. **Content Safety Check**: Each email goes through **Llama Guard 3 8B** for safety, and users are notified if any unsafe content is detected.

---

## Business Use Case

GroqMail offers significant value for professionals and businesses by providing an efficient, safe, and adaptable email assistant. Ideal for sales, customer service, and client communications, GroqMail assists users in drafting emails that match professional standards, fostering clarity, and maintaining a polished image.

- **Time Efficiency**: Reduces the time spent drafting and responding to emails, letting users focus on higher-priority tasks.
- **Safety Compliance**: Llama Guard’s content filtering is essential for industries requiring strict adherence to communication standards, ensuring professionalism and avoiding harmful language.
- **Scalable Solution**: GroqMail’s adaptability makes it ideal for both small businesses and large enterprises looking for reliable and safe AI-powered communication tools.

---

## Technology Stack

- **Backend**: Groq API using Llama Guard 3 8B for content filtering and **Llama Versatile 70B** for email generation.
- **Frontend**: Streamlit, providing an interactive and user-friendly interface.
- **Deployment**: Easily deployable on platforms supporting Python and Streamlit, such as Heroku or Vercel.

---

## Additional Documentation

For an in-depth look at each function and safety feature, refer to [docs.md](docs.md). This document contains detailed explanations of the `check_email_safety` function and safety protocols, as well as usage guidelines for GroqMail’s email generation capabilities.

This README provides a comprehensive overview, emphasizing **Llama Guard's** safety features and the business use case, making it suitable for submission to the Groq Bounty competition.
