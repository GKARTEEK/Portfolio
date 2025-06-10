
from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    """Home page view with portfolio data"""
    
    # Personal Information
    personal_info = {
        'full_name': 'Gavara Karteek',
        'email': 'karteekgavara@gmail.com',
        'phone': '+91 7207085626',
        'linkedin': 'https://linkedin.com/in/karteekgavara',
        'github': 'https://github.com/karteekgavara',
        'website': 'https://karteekgavara.portfolio.com',
        'location': 'Vijayawada, Andhra Pradesh, India'
    }
    
    # Career Objective
    career_objective = "Passionate B.Tech CSE student seeking opportunities as a Full Stack Developer or DevOps Engineer. Experienced in Django, Python, and cloud technologies with a strong foundation in problem-solving and clean code practices."
    
    # Skills data (enhanced)
    skills = [
        {
            'category': 'Programming Languages',
            'items': ['Python', 'C', 'Java', 'JavaScript', 'SQL'],
            'color': 'primary'
        },
        {
            'category': 'Web Technologies', 
            'items': ['Django', 'Flask', 'HTML', 'CSS', 'REST APIs'],
            'color': 'secondary'
        },
        {
            'category': 'Database & Tools',
            'items': ['MySQL', 'SQLite', 'PostgreSQL', 'Git', 'VS Code'],
            'color': 'accent'
        },
        {
            'category': 'DevOps & Cloud',
            'items': ['Docker', 'CI/CD', 'GitHub Actions', 'AWS', 'Linux'],
            'color': 'primary'
        },
        {
            'category': 'Core Concepts',
            'items': ['DSA', 'OOPs', 'System Design', 'Algorithms'],
            'color': 'secondary'
        }
    ]
    
    # Enhanced Projects data
    projects = [
        {
            'title': 'TechStack Web App',
            'description': 'Django + SQLite application with categorized 500+ questions and 35% faster DB performance through indexing optimization.',
            'tech': ['Django', 'SQLite', 'Python', 'HTML/CSS'],
            'demo_url': '#',
            'github_url': '#',
            'role': 'Full Stack Developer'
        },
        {
            'title': 'E-Commerce Platform',
            'description': 'Complete e-commerce solution with user authentication, payment integration, and admin dashboard.',
            'tech': ['Django', 'MySQL', 'Bootstrap', 'JavaScript'],
            'demo_url': '#',
            'github_url': '#',
            'role': 'Backend Developer'
        },
        {
            'title': 'Student Management System',
            'description': 'Web application for managing student records, attendance, and grade tracking with role-based access.',
            'tech': ['Flask', 'SQLite', 'HTML/CSS', 'jQuery'],
            'demo_url': '#',
            'github_url': '#',
            'role': 'Full Stack Developer'
        }
    ]
    
    # Education data
    education = [
        {
            'institution': 'KL University',
            'degree': 'B.Tech in Computer Science Engineering',
            'duration': '2022 - 2026',
            'cgpa': '9.29',
            'location': 'Guntur, AP'
        },
        {
            'institution': 'Sri Chaitanya Junior College',
            'degree': 'Intermediate (XII)',
            'duration': '2020 - 2022',
            'percentage': '95.2%',
            'board': 'AP Board'
        },
        {
            'institution': 'Narayana High School',
            'degree': 'Secondary School (X)',
            'duration': '2019 - 2020',
            'percentage': '96.5%',
            'board': 'AP Board'
        }
    ]
    
    # Enhanced Certifications data
    certifications = [
        {
            'name': 'AWS Cloud Practitioner',
            'platform': 'AWS',
            'status': 'In Progress',
            'date': '2024',
            'color': 'yellow'
        },
        {
            'name': 'Python (Advanced)',
            'platform': 'HackerRank',
            'status': 'Certified',
            'date': 'Nov 2023',
            'color': 'green'
        },
        {
            'name': 'SQL (Expert)',
            'platform': 'HackerRank',
            'status': 'Certified',
            'date': 'Oct 2023',
            'color': 'blue'
        },
        {
            'name': 'Python for Everybody',
            'platform': 'Coursera',
            'status': 'Completed',
            'date': 'Sep 2023',
            'color': 'purple'
        }
    ]
    
    # Internships & Training
    internships = [
        {
            'company': 'NxtWave',
            'role': 'CCBP 4.0 Intensive',
            'duration': 'Jan 2023 - Dec 2023',
            'description': 'Completed intensive training in Full Stack Development with focus on Python, Django, and React.',
            'technologies': ['Python', 'Django', 'React', 'SQL']
        }
    ]
    
    # Achievements & Awards
    achievements = [
        {
            'title': 'Dean\'s List',
            'description': 'Achieved Dean\'s List recognition for maintaining 9+ CGPA',
            'date': '2023',
            'category': 'Academic'
        },
        {
            'title': 'Coding Contest Winner',
            'description': 'First place in college-level coding competition',
            'date': '2023',
            'category': 'Technical'
        },
        {
            'title': 'Hackathon Participant',
            'description': 'Top 10 finalist in state-level hackathon',
            'date': '2023',
            'category': 'Competition'
        }
    ]
    
    # Co-curricular Activities
    activities = [
        {
            'title': 'Technical Club Secretary',
            'organization': 'CSE Department',
            'duration': '2023 - Present',
            'description': 'Organized technical workshops and coding competitions for 200+ students'
        },
        {
            'title': 'Event Coordinator',
            'organization': 'College Tech Fest',
            'duration': '2023',
            'description': 'Coordinated technical events and managed participant registrations'
        }
    ]
    
    # Languages
    languages = [
        {'name': 'English', 'proficiency': 'Fluent'},
        {'name': 'Telugu', 'proficiency': 'Native'},
        {'name': 'Hindi', 'proficiency': 'Conversational'}
    ]
    
    # Contact information
    contact_info = {
        'email': personal_info['email'],
        'phone': personal_info['phone'],
        'github': personal_info['github'],
        'linkedin': personal_info['linkedin']
    }
    
    context = {
        'developer_name': personal_info['full_name'],
        'title': 'Full Stack Developer | DevOps Enthusiast',
        'summary': 'B.Tech CSE student at KL University with 2+ years of backend experience in Django, REST APIs, and DevOps. Passionate about cloud automation, clean code, and problem-solving.',
        'career_objective': career_objective,
        'personal_info': personal_info,
        'cgpa': '9.29',
        'experience_years': '2+',
        'skills': skills,
        'projects': projects,
        'education': education,
        'certifications': certifications,
        'internships': internships,
        'achievements': achievements,
        'activities': activities,
        'languages': languages,
        'contact': contact_info,
    }
    
    return render(request, 'home.html', context)