
# GroqMail Documentation

## Overview

**GroqMail** is an AI-powered email assistant leveraging Groq's Llama Versatile model for generating emails and **Llama Guard 3 8B** for content safety. This documentation provides an in-depth look at each key function, highlighting the safety checks, email generation process, and usage guidelines.

## Table of Contents

1. [Setup and Configuration](#setup-and-configuration)
2. [Key Functions](#key-functions)
    - [check_email_safety](#check_email_safety)
    - [generate_email](#generate_email)
    - [generate_reply](#generate_reply)
3. [User Interface](#user-interface)
4. [Content Safety with Llama Guard](#content-safety-with-llama-guard)
5. [Badge System](#badge-system)

---

## Setup and Configuration

To run GroqMail, ensure you’ve followed the setup instructions provided in the main **README.md** file. The `.env` file should contain your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

## Key Functions

### `check_email_safety`

The `check_email_safety` function is responsible for evaluating each generated email or reply for potentially unsafe content using **Llama Guard**. Here’s how it works:

```python
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
```

**Explanation**:
- **Input**: The generated email content.
- **Process**: The content is sent to the Llama Guard model for analysis. If unsafe content is detected, a `ValueError` is raised with a message.
- **Output**: Either a safe result, allowing the email to be displayed, or an error message if unsafe content is detected.

### `generate_email`

The `generate_email` function prompts the conversational model to generate a new email based on user inputs for recipient details, purpose, tone, and length. 

**Code Block**:
```python
def generate_email(prompt):
    completion = client.chat.completions.create(
        model=conversational_model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
    )
    return completion.choices[0].message.content
```

**Explanation**:
- **Input**: A prompt generated from user inputs.
- **Process**: The prompt is processed by the conversational model to create an email draft.
- **Output**: The generated email content, which is then checked by `check_email_safety` for safety.

### `generate_reply`

The `generate_reply` function works similarly to `generate_email` but is tailored to create responses based on a previously received email. This function takes inputs for the received email, relationship with the sender, response details, tone, and length.

**Code Block**:
```python
def generate_reply(prompt):
    completion = client.chat.completions.create(
        model=conversational_model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
    )
    return completion.choices[0].message.content
```

**Explanation**:
- **Input**: A prompt crafted from the user’s response context and the received email content.
- **Process**: The model generates a reply to the received email.
- **Output**: The reply, which is verified by `check_email_safety`.

## User Interface

GroqMail’s user interface is built with Streamlit and is designed to make email generation straightforward and efficient. It includes the following sections:

1. **Main Page**: Introduction to GroqMail’s features and usage.
2. **Write an Email**: Collects user inputs for recipient information, purpose, tone, and length, then generates an email.
3. **Reply to an Email**: Allows users to paste an email and specify response details, tone, and length to generate an appropriate reply.
4. **Contact**: Provides links to the developer's social profiles and portfolio.

Each section includes instructions, placeholders, and a responsive design to facilitate smooth navigation and email generation.

## Content Safety with Llama Guard

Content safety is a critical aspect of GroqMail, ensuring that generated emails adhere to professional and safe standards. Here’s how **Llama Guard** enhances content safety:

1. **Real-Time Checks**: Each email draft and reply is passed through Llama Guard for analysis.
2. **Automated Alerts**: If unsafe content is detected, GroqMail raises an alert, and the potentially harmful email is blocked from display.
3. **Business-Ready Security**: Llama Guard’s rigorous content filtering makes GroqMail suitable for professional environments where communication quality is paramount.

This approach minimizes the risk of inappropriate or harmful content in business and personal communications, offering peace of mind for users in sensitive industries or high-stakes roles.


## Error Handling

GroqMail includes detailed error handling for both the content generation and safety-checking processes. Notable exceptions include:

- **Safety Warnings**: If unsafe content is flagged by Llama Guard, a `ValueError` is raised, and an error message informs the user.
- **API Errors**: Any issues with API calls are caught and displayed to the user, ensuring smooth operation and troubleshooting.

For any additional information on error codes and handling, please refer to the error documentation provided by Groq.

