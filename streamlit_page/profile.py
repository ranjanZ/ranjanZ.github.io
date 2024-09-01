import streamlit as st


base_path="https://github.com/ranjanZ/ranjanZ.github.io/blob/master/streamlit_page/"

# Page title and layout
st.set_page_config(page_title="My Streamlit Profile", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
tabs = ["About", "Experience", "Skills", "Projects", "Publications", "Blogs", "Contact"]
selected_tab = st.sidebar.selectbox("Select a tab", tabs)

# Main content based on selected tab
if selected_tab == "About":
    st.header("About")
    st.image(base_path+"data/profile_picture.jpg")  # Replace with your image path
    st.write("Applied AI/ML | Machine Learning Researcher")
    st.write("Email: ranjan.rev@gmail.com | Phone: +91 6290153508")
    st.write("Website: https://ranjanz.github.io/")

elif selected_tab == "Experience":
    st.header("Experience")
    experience_data = [
        ("JP Morgan Chase & Co", "Bangalore, India", "Jan 2023 - Present", "Applied AI/ML as AVP, Working on applied AI/ML in financial domain..."),
        ("Samsung Research", "Bangalore, India", "2021 - 2023", "Lead Research Engineer, Worked on state-of-the-art video panoptic segmentation...")
    ]

    for company, location, dates, description in experience_data:
        with st.expander(company):
            st.write(f"**Location:** {location}")
            st.write(f"**Dates:** {dates}")
            st.write(description)

elif selected_tab == "Skills":
    st.header("Skills")
    skills_data = ["Python", "Machine Learning", "Deep Learning", "Computer Vision", "Data Science", "Natural Language Processing"]

    st.write(" ".join([f'<span class="badge badge-pill badge-primary">{skill}</span>' for skill in skills_data]))

elif selected_tab == "Projects":
    st.header("Projects")
    projects_data = [
        ("Morphological Network for Image De-raining", "A project using morphological networks to remove rain from images...", "https://github.com/ranjanZ/2D-Morphological-Network"),
        # Add more projects here
    ]

    for title, description, link in projects_data:
        with st.expander(title):
            st.write(description)
            st.write(f'<a href="{link}">GitHub Link</a>', unsafe_allow_html=True)

elif selected_tab == "Publications":
    st.header("Publications")
    publications_data = [
        ("Morphological Network: How Far Can We Go with Morphological Neurons?", "Ranjan Mondal, Sanchayan Santra, Soumendu Sundar Mukherjee, and Bhabatosh Chanda", "https://arxiv.org/abs/2208.09790"),
        # Add more publications here
    ]

    for title, authors, link in publications_data:
        with st.expander(title):
            st.write(authors)
            st.write(f'<a href="{link}">Preprint</a>', unsafe_allow_html=True)

elif selected_tab == "Blogs":
    st.header("Blogs")
    blog_posts = [
        ("Blog Post 1", "Link to Blog Post 1"),
        ("Blog Post 2", "Link to Blog Post 2"),
        # Add more blog posts here
    ]

    for title, link in blog_posts:
        st.write(f'<a href="{link}">{title}</a>', unsafe_allow_html=True)

elif selected_tab == "Contact":
    st.header("Contact")
    st.write("**Email:** ranjan.rev@gmail.com")
    st.write("**Phone:** +91 6290153508")
    st.write("**Website:** https://ranjanz.github.io/")

# Footer
st.write("© 2024 Ranjan Mondal")




