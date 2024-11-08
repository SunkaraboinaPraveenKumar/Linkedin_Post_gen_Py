from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()


def get_length_str(length):
    if length == 'Short':
        return "5 to 10 lines"
    if length == 'Medium':
        return "10 to 15 lines"
    if length == 'Long':
        return "15 to 20 lines"


def generate_post(length, language, tag):
    prompt = get_prompt(length, language, tag)
    response = llm.invoke(prompt)
    return response.content


def get_prompt(length, language, tag):
    length_str = get_length_str(length)

    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be English.
    '''

    examples = few_shot.get_filtered_posts(length, language, tag)

    if len(examples) > 0:
        prompt += "4) Use Writing style as per the following examples"

    for i, post in enumerate(examples):
        post_text = post['text']
        prompt += f'\n\n Example {i + 1}: \n\n {post_text}'

        if i == 1:
            break

    return prompt


if __name__ == '__main__':
    print(generate_post("Medium", "English", "Mental Health"))
