from google import genai
import json
import pathlib
import base64

client = genai.Client()
gemini_flash = "gemini-3.8-flash"
gemini_flash_lite = "gemini-3.1-flash-lite"

def interact(text_input, previous_interaction_id=None):
    """
    Parameters
    ---
    text_input: str
        input from the user that will prompt the chatbot.

    previous_interaction_id (optional): str
        allows for continuation of the conversation.

    The function returns the interaction object which contains the response from the chatbot.

    Returns
    ---
    interaction: Obj
        contains the interactions.text_output property which is the response from the chosen chatbot
        contains the interactions.id property which shows the interaction id for stateful conversations.
    """

    interaction = client.interactions.create(
        model=gemini_flash_lite,
        input=text_input,
        previous_interaction_id=previous_interaction_id
    )
    return interaction

def chatbot_welcome_message(survey_data, previous_interaction_id=None):
    """
    Used at the start of the program at the start of the day after the survey is done by the user. This function properly feeds in the proper system instructions including research papers that will inform the chatbot on the relevant data to better serve the user.

    Parameters
    ---
    survey_data: dict
        a python dictionary containing data from the user on the survey
    previous_interaction_id: str
        id from the previous interaction to allow for the continuation of the conversation

    Returns
    ---
    interaction: Obj
        contains the interactions.text_output property which is the response from the chosen chatbot
        contains the interactions.id property which shows the interaction id for stateful conversations.
    """
    survey_data = json.dumps(survey_data)

    system_instruction = "You are a counseller for a student to assess whether he/she is going to experience burnout. "

    file_path = pathlib.Path('./papers/redefining_burnout_key_symptoms.pdf')

    prompt = [
            {"type": "text", "text": survey_data},
            {"type": "document", "data": base64.b64encode(file_path.read_bytes()).decode("utf-8"), "mime_type": "application/pdf"}
    ]

    prompt = "Here are the results of a survey:\n" + survey_data

    interaction = client.interactions.create(
        model=gemini_flash_lite,
        input=prompt,
        system_instruction=system_instruction,
        previous_interaction_id=previous_interaction_id
    )
    return interaction


if __name__ == "__main__":
    interaction = chatbot_welcome_message({})
    print(interaction.output_text)
