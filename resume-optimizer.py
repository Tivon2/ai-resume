import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API client using environment variable 
client = OpenAI(api_keys=os.getenv("OPENAI_API_KEY"))

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

# Load API client using environment variable
client = OpenAI(api_key=api_key)


def optimize_resume(resume_text, job_description, model="gpt-4o-mini"):
    """
    Uses OpenAI to edit resume to any description via prompt engineering
    """

    system_prompt = """
You are a senior technical recruiter and ATS optimization expert with 15+ years in tech consulting hiring, specializing in AI Transformation Consultant and Software Engineering roles.

Style: Professional, confident, human-centered (align with "fiercely human" cultures like Slalom). Use strong action verbs, quantify where possible, keep bullets concise (1-2 lines), ATS-friendly (no fancy formatting, natural keyword inclusion).

Process:
1. Analyze JD: Extract key skills, tech, responsibilities, keywords (e.g., AI Maturity Assessments, AIOps, agentic workflows, prompt engineering, GenAI landscape, SDLC, DevOps).
2. Compare to resume: Highlight matches, rephrase for alignment, note real gaps (no fabrication).
3. Rewrite sections: Job bullets, skills list, optional summary.
4. Suggest 5-10 ATS keywords to add naturally.
5. Output in clean markdown: Before/After for each section + recommendations.
"""

    user_prompt = f"""
Job Description:
{job_description}

Users Current Resume Text:
{resume_text}

Now optimize and tailor the resume for this role. Show Before/After versions of key sections (especially Bell bullets and skills). Suggest keywords. Keep it honest.
"""

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error occurred: {str(e)}\n(Check your API key, internet, or OpenAI account credits.)"


# --- Main Exec ---
if __name__ == "__main__":

    # Put resume here
    my_resume = """Resilient and outcome-focused Computer Science graduate with professional industry experience supporting and developing enterprise systems. Skilled in Python and Java with hands-on experience troubleshooting production issues through log analysis and SQL queries, building backend logic, and working with cloud platforms such as AWS and Azure. Comfortable collaborating in Agile teams to deliver reliable and scalable software solutions. Strong interest in software engineering, cloud technologies, and applying AI/ML tools to improve system intelligence, automation, and data-driven applications.


9000 Jane Street, Vaughan, 
ON, L4K 0M6, Canada
(289) 941-4061
Nosahare@outlook.com
Linkedin
Areas of Interest: Software Engineering • Backend Development • Distributed Systems • Cloud Computing (AWS/Azure) • DevOps & CI/CD • API Development • Microservices Architecture • AI/ML Applications • Automation & Scripting • Scalable System Design

WORK EXPERIENCE

Bell, Remote, Toronto — Junior Data Engineer
May 2023 - Current
Conducted in-depth troubleshooting and root-cause analysis of backend systems and API workflows using logs, SQL queries, and diagnostic tools—building investigative skills transferable to digital forensics and incident response.
Developed Python and SQL scripts for automated data validation, quality checks, and regression testing, supporting rapid detection and resolution of anomalies in enterprise environments.
Collaborated in Agile teams to plan, execute, and resolve issues across distributed systems, demonstrating resilience and flexibility in fast-paced, high-impact scenarios.
Supported CI/CD pipelines with Jenkins, validating builds/deployments to ensure system integrity—aligning with security practices for reliable operations.
Gained exposure to AWS and Azure cloud platforms in telecom-scale architectures, relevant to cloud incident response and threat hunting.

Trent University Peterborough, ON — Computer Lab Assistant (Linux/Mac/Windows)
Sept 2024 - April 2025
Worked with students to translate functional requirements into structured implementation plans across Python, Java, C#, and SQL.
Diagnosed logic, runtime, and design issues by comparing expected behavior, written specifications, and actual code execution.
Assisted with debugging, environment setup, and cross-platform issues across Linux, macOS, and Windows.
EDUCATION
Trent University, Peterborough, ON — BSc. Honours Computer Science and  Business Administration (Double degree)
09 2020 -  07 2025
Mohawk college, Hamilton, ON — Business Administration 
09 2018 - 05 2020
CERTIFICATIONS 
CompTIA A+ (220-1201/220-1202) - 1 exam remaining
AWS Cloud Practitioner (CLF-C02)
Microsoft Azure developer  - In Progress
PROJECTS
Pulse: iOS Health Tracking App Prototype (Swift, Firebase, REST APIs, Postman)
Designed and prototyped an AI-ready health tracking application integrating iOS frontend, Firebase backend, and RESTful services to support scalable user data workflows.
Converted Figma designs into a polished, functional UI with gesture-based interactions.
Used Postman to test and validate backend APIs for creating, updating, and retrieving user entries, verifying response structures and error handling before iOS integration.
Performed API regression testing using Postman collections to ensure backend changes did not break existing functionality.
Validated data contracts and edge cases to support a shift-left quality approach during development.
Gesture-Controlled Zoom Tool (Python, OpenCV, MediaPipe)
OpenCV, MediaPipe, AI-assisted development workflows, API automation
Developed a real-time hand gesture system for cursor and zoom control.
Optimized frame processing to improve accuracy and reduce latency.
Conducted root-cause analysis on system anomalies via logs and queries, akin to forensic troubleshooting

TECHNICAL SKILLS
Languages: Python (scripting & automation), Java, JavaScript, SQL, C#
Cloud & AI: AWS, Azure , AI/ML/GenAI concepts, cloud-native patterns
DevOps & Infrastructure: Git/Version Control, Jenkins/CI/CD pipelines, Docker/containers (exposure), Kubernetes (interest), DevOps/DevSecOps practices
APIs & Data: REST APIs (design, implementation, testing with Postman), event-driven (interest in Kafka/Flink)
Agile & Tools: Agile/Scrum, User Stories, Requirements Analysis, JIRA/Confluence 
Other: Selenium (Java automation), OpenCV/MediaPipe (AI workflows), SQL queries/data validation, OOP/Data Structures/Algorithms, SDLC

INTERPERSONAL  SKILLS
Actively exploring cybersecurity domains through self-study (e.g., incident response basics, threat hunting concepts) and AI applications in security.
Proactive learner with strong initiative to explore new tools (genAI, containers, event-driven tech) and deliver creative, client-focused solutions.
Clear communicator: Actively listens, simplifies complex data/technical scenarios, and conveys insights positively in collaborative settings.

Team-oriented with Agile experience in requirements translation, cross-functional problem-solving, and driving data reliability/impact.

Committed to Design Thinking, diverse viewpoints, and long-term growth in data services development.
"""

    # Put Job description here
    slalom_jd = """job Title: AI Transformation Consultant (New role)

Practice: Transformation Design & Leadership 

What You’ll Do

 • Support AI Maturity Assessments: Assist in evaluating client capabilities across data readiness, technology infrastructure, and talent. You will help gather data, perform gap analysis, and contribute to reports that define how an organization can evolve from AI-aware to AI-native.

 • Contribute to Platform Decisions: Support the team in navigating the complex ecosystem of AI vendors and tools. You will perform research and competitive analysis to provide framework-driven recommendations on build-vs-buy scenarios.

 • Assist in Establishing AIOps: Work alongside technical leads to help bridge the gap between "pilot" and "production" by supporting the design of AIOps processes. You will contribute to the documentation of governance, monitoring, and continuous integration workflows.

 • Support Transformation Delivery: Act as a core member of cross-functional delivery teams. You will assist in tracking AI transformation roadmaps, ensuring technical tasks stay synchronized with organizational change and value realization.

 • Identify AI Workflows: Collaborate with team members to identify opportunities for agentic workflows, AI-augmented decision-making, and frictionless human-machine collaboration.

• Facilitate Workshop Success: Support the delivery of workshops and training sessions that help client leaders shift from "decision-makers" to "learners," promoting a culture of experimentation and ethical AI adoption.

What You’ll Bring

 • Experience: 2–3 years of experience in technology consulting, organizational change, or a related strategic support role.

 • AI Fluency: A strong foundational understanding of the GenAI landscape (LLMs, prompt engineering, agentic patterns) and their practical business applications.

 • Operational Mindset: An understanding of the software development lifecycle (SDLC) or DevOps principles, with an interest in how those evolve into AIOps.

 • Collaborative Spirit: A proven ability to work effectively within a team, taking ownership of specific workstreams while staying aligned with broader project goals.

 • Communication: Exceptional interpersonal skills; you can clearly communicate findings and updates to both internal team members and client stakeholders.
"""

    print("Sending request to OpenAI...\n")
    result = optimize_resume(my_resume, slalom_jd)
    print(result)