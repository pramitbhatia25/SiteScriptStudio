import streamlit as st
import os
from jinja2 import Environment, FileSystemLoader

st.title("Site-Script-Studio")
st.info("""Introducing SiteSproutStudio - the one-stop solution for creating beautiful, modern
           and professional websites that are tailored to your specific needs. 
           With this powerful, easy-to-use website builder and a range of customizable features,
           you can create your dream website in minutes without any prior design or coding experience.""")
           
st.title("Page 1: Introduction")

title = st.text_input('Title')
primary_color = st.color_picker('Primary color')
name = st.text_input('Name')
job_title = st.text_input('Job title')
resume_pdf = st.file_uploader('Upload your resume (PDF) (Not Mandatory)', type='pdf')
resume=""
if resume_pdf:
    resume="/Resume.pdf"
links = st.multiselect("Select Links To Add", ["Instagram", "Github", "Linkedin", "Youtube", "Twitter"])
instagram_link = ""
github_link = ""
linkedin_link = ""
youtube_link = ""
twitter_link = ""

if "Instagram" in links:
    instagram_link = st.text_input('Instagram link')

if "Github" in links:
    github_link = st.text_input('Github link')

if "Linkedin" in links:
    linkedin_link = st.text_input('Linkedin link')

if "Youtube" in links:
    youtube_link = st.text_input('Youtube link')

if "Twitter" in links:
    twitter_link = st.text_input('Twitter link')

# Input element for personal image link
personal_image_link = st.text_input('Personal image link')

st.title("Page 2 -> N-1 : Sections")

sections = []
num_sections = st.number_input('How many sections do you want to add? (Eg. Projects, Experiences, etc.)', min_value=0, max_value=7, value=1, key='num_sections')
for j in range(num_sections):
    section_key = f'section-{j}'
    name_of_section = st.text_input(f'Section {j+1} Header', key=f'{section_key}-name')
    projects = []
    num_projects = st.number_input('How many sub-sections do you want to add? (Eg. Number of Projects, Number of Experiences)', min_value=0, max_value=10, value=1, key=f'{section_key}-num_projects')
    for i in range(num_projects):
        project_key = f'{section_key}-project-{i}'
        project_title = st.text_input(f'Sub-Section {i+1} title', key=f'{project_key}-title')
        project_description = st.text_area(f'Sub-Section {i+1} description', max_chars=200, key=f'{project_key}-description')
        project_link = st.text_input(f'Sub-Section {i+1} link', key=f'{project_key}-link')
        projects.append({'title': project_title, 'description': project_description, 'link': project_link})
    
    sections.append({'name':name_of_section, 'desc':projects})

st.title("Page N : Testimonials")

# Input elements for testimonials
testimonials = []
num_testimonials = st.number_input('How many testimonials do you want to add?', min_value=0, max_value=10, value=1, key=1)
for i in range(num_testimonials):
    quote = st.text_input(f'Testimonial {i+1} quote')
    speaker = st.text_input(f'Testimonial {i+1} speaker')
    testimonials.append({'quote': quote, 'speaker': speaker})

# Set up the Jinja environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Render the template with the user input values
# https://th.bing.com/th/id/OIP.Z_E-BG4f4fYbXVBkQXr2kAHaHa?pid=ImgDet&rs=1
if (st.button("Create") and title != ""):
    html = template.render(
        title=title,
        name=name,
        job_title=job_title,
        resume=resume,
        primary_color=primary_color,
        github_link=github_link,
        instagram_link=instagram_link,
        linkedin_link=linkedin_link,
        twitter_link=twitter_link,
        youtube_link=youtube_link,
        personal_image_link=personal_image_link,
        testimonials=testimonials,
        sections=sections
    )

    st.info("To view your complete portfolio website, make sure your resume and index.html files are in the same directory.")
    st.info("To host your website in seconds, you can use any of the following hosting resources below.")

    st.write("[Tiiny Hosting](%s)" % "https://tiiny.host/")
    st.write("[Github Pages Hosting](%s)" % "https://pages.github.com/")
    st.write("[Render Hosting](%s)" % "https://render.com/")

    # directory = title
    # if not os.path.exists(directory):
    #     os.makedirs(directory)

    # filename = directory + "/index.html"
    # with open(filename, 'w') as f:
    #     f.write(html)

    # if resume_pdf is not None:
    #     with open(directory + "/Resume.pdf", 'wb') as f:
    #         f.write(resume_pdf.read())

    st.download_button(
        label='Download Your Website!',
        data=html,
        file_name='index.html',
        mime='text/html'
    )

    st.title("Your Website:")

    st.components.v1.html(html,height=500, width=800, scrolling=1)

    


