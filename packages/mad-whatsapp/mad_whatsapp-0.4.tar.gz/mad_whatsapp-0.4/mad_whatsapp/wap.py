import re
import datetime

ignore_messages = ['<Media Omitted>','null']

def parse_whatsapp_conversation(conversation):
    if isinstance(conversation, str):
        conversation = conversation.split('\n')
    messages = []
    buffer = []
    for line in conversation:
        # Check if the line starts with a date pattern
        match = re.match(r'\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2} - ', line)
        if match:
            if buffer:
                # Save the message from the buffer
                parsed_message = parse_message(''.join(buffer))
                if parsed_message['content']:
                    messages.append(parsed_message)
                buffer = []
        buffer.append(line)
    if buffer:
        parsed_message = parse_message(''.join(buffer))
        if parsed_message['content']:
            messages.append(parsed_message)

    return messages

def parse_whatsapp_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return parse_whatsapp_conversation(lines)

def parse_message(message):
    date_pattern = r'(?P<date>\d{1,2}/\d{1,2}/\d{2,4}), (?P<time>\d{1,2}:\d{2})'
    author_pattern = r'- (?P<author>.*?):'
    content_pattern = r'- .*?: (?P<content>.*)'

    date_match = re.search(date_pattern, message)
    author_match = re.search(author_pattern, message)
    content_match = re.search(content_pattern, message)

    content = content_match.group('content').strip() if content_match else None

    # Remove the unwanted phrases from content
    for phrase in ignore_messages:
        pattern = re.compile(re.escape(phrase), re.IGNORECASE)
        content = pattern.sub("", content)

    # Normalize the date format
    date_string = date_match.group('date') if date_match else None
    time_string = date_match.group('time') if date_match else None
    normalized_date = normalize_date_format(date_string)

    parsed_message = {
        'timestamp': f"{normalized_date} {time_string}" if normalized_date and time_string else None,
        'author': author_match.group('author') if author_match else None,
        'content': content
    }

    return parsed_message

def normalize_date_format(date_string):
    try:
        # Try parsing with day first
        date_obj = datetime.datetime.strptime(date_string, '%d/%m/%y')
    except ValueError:
        try:
            # If that fails, try parsing with month first
            date_obj = datetime.datetime.strptime(date_string, '%m/%d/%y')
        except ValueError:
            # If both fail, return the original string
            return date_string
    # Return the date in the desired format
    return date_obj.strftime('%d/%m/%y')
