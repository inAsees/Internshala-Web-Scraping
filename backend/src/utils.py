import urllib.parse
from typing import List


class Utils:
    @staticmethod
    def get_categories() -> List[str]:
        categories = ['.NET Development', '3D Printing', 'Accounts', 'Acting', 'Aerospace Engineering',
                      'Agriculture and Food Engineering', 'Analytics', 'Anchoring', 'Android App Development',
                      'Angular.js Development', 'Animation', 'Architecture', 'Artificial Intelligence (AI)',
                      'ASP.NET Development', 'Audio Making/Editing', 'Automobile Engineering', 'Backend Development',
                      'Big Data', 'Bioinformatics', 'Biology', 'Biotechnology Engineering', 'Blockchain Development',
                      'Blogging', 'Brand Management', 'CAD Design', 'Campus Ambassador', 'Chartered Accountancy (CA)',
                      'Chemical Engineering', 'Chemistry', 'Cinematography', 'Civil Engineering', 'Client Servicing',
                      'Cloud Computing', 'Commerce', 'Company Secretary (CS)', 'Computer Science', 'Computer Vision',
                      'Content Writing', 'Copywriting', 'Creative Writing', 'Culinary Arts', 'Customer Service',
                      'Cyber Security', 'Data Entry', 'Data Science', 'Database Building', 'Design',
                      'Dietetics/Nutrition', 'Digital Marketing', 'Editorial', 'Electrical Engineering',
                      'Electronics Engineering', 'Embedded Systems', 'Engineering', 'Engineering Design',
                      'Engineering Physics', 'Environmental Sciences', 'Event Management', 'Facebook Marketing',
                      'Fashion Design', 'Film Making', 'Finance', 'Flutter Development', 'Front End Development',
                      'Full Stack Development', 'Fundraising', 'Game Development', 'General Management', 'Government',
                      'Graphic Design', 'Hospitality', 'Hotel Management', 'Human Resources (HR)', 'Humanities',
                      'Image Processing', 'Industrial and Production Engineering', 'Industrial Design',
                      'Information Technology', 'Instrumentation and Control Engineering', 'Interior Design',
                      'Internet of Things (IoT)', 'iOS App Development', 'Java Development', 'Javascript Development',
                      'Journalism', 'Law', 'Legal Research', 'Machine Learning', 'Magento Development',
                      'Manufacturing Engineering', 'Market/Business Research', 'Marketing/Sales', 'Material Science',
                      'Mathematics', 'Mathematics and Computing', 'MBA', 'Mechanical Engineering', 'Mechatronics',
                      'Media', 'Medicine', 'Merchandise Design', 'Mobile App Development', 'Motion Graphics', 'Music',
                      'Network Engineering', 'NGO', 'Node.js Development', 'Operations', 'Pharmaceutical',
                      'Photography', 'PHP Development', 'Physics', 'Political/Economics/Policy Research',
                      'Public Relations (PR)', 'Product Management', 'Programming', 'Project Management',
                      'Proofreading', 'Psychology', 'Python/Django Development', 'Recruitment', 'Robotics',
                      'Ruby on Rails', 'Science', 'Search Engine Optimization (SEO)', 'Social Media Marketing',
                      'Social Work', 'Software Development', 'Software Testing', 'Statistics', 'Strategy',
                      'Subject Matter Expert (SME)', 'Supply Chain Management (SCM)', 'Talent Acquisition', 'Teaching',
                      'Telecalling', 'Transcription', 'Translation', 'Travel and Tourism', 'UI/UX Design',
                      'Video Making/Editing', 'Videography', 'Volunteering', 'Web Development', 'Wordpress Development']

        return sorted(categories)

    @staticmethod
    def get_url_encoded_data(data: str) -> str:
        url_encoded_form_data = urllib.parse.quote(data, safe='')
        return url_encoded_form_data
