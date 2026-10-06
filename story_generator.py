def generate_story(topic, genre, length):

    stories = {
        "Adventure": f"""
Once upon a time, a young hero named Alex discovered a mysterious map
related to {topic}. Alex decided to follow the map and began an exciting
adventure. Along the way, Alex faced many challenges but never gave up.
Finally, Alex discovered the secret behind {topic} and returned home as
a brave and confident person.
""",

        "Fantasy": f"""
In a magical kingdom, a young girl discovered a mysterious secret about
{topic}. She entered an enchanted forest where magical creatures helped
her on her journey. After facing many difficulties, she used her courage
and kindness to solve the mystery and save the kingdom.
""",

        "Horror": f"""
Late one night, a strange mystery appeared around {topic}. Nobody in the
town knew what was happening. A young student decided to investigate.
Inside an abandoned building, strange sounds could be heard. After a
terrifying journey, the student discovered the truth behind the mystery.
""",

        "Mystery": f"""
A strange mystery involving {topic} appeared in a quiet town. Detective
Alex started investigating the case and discovered several hidden clues.
After following the clues carefully, Alex finally solved the mystery and
revealed the surprising truth.
""",

        "Romance": f"""
Two people met unexpectedly because of {topic}. At first, they were
complete strangers, but their shared experiences brought them closer.
Through many conversations and challenges, they slowly discovered that
their friendship had become something much more meaningful.
""",

        "Science Fiction": f"""
In the year 2050, scientists made an amazing discovery connected to
{topic}. A young scientist was chosen to investigate it. The discovery
changed the way humans understood technology and opened the door to an
exciting new future.
"""
    }

    return stories.get(genre, stories["Adventure"])