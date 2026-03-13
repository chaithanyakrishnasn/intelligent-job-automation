def generate_email(job):

    subject = f"Application for {job.title} Role"

    body = f"""
Dear Hiring Manager,

I am writing to express my interest in the {job.title} position at {job.company}.
My background in software development and backend systems makes me excited about this opportunity.

I would welcome the chance to contribute to your team.

Best regards,
Krishna Chaithanya
"""

    return {
        "subject": subject,
        "body": body
    }