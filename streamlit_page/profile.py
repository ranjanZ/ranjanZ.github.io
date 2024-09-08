import streamlit as st
from blogs import *

base_path="https://raw.githubusercontent.com/ranjanZ/ranjanZ.github.io/master/streamlit_page/"

# Page title, icon, and layout
st.set_page_config(
    page_title="Ranjan's Profile",
    page_icon=":robot:",  # Add a robot icon (adjust if desired)
    layout="wide",
)


# Sidebar navigation
st.sidebar.title("Navigation")
tabs = ["About", "Carrier and  Experience", "Projects", "Publications", "Blogs", "Contact","My Story"]
selected_tab = st.sidebar.selectbox("Select a tab", tabs)

# Custom CSS for background image and styling (optional)
css="""
body {
    margin: 0;
    padding: 0;
    font-family: sans-serif;
    background-image: url("path/to/your/background_image.jpg");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    background-attachment: fixed;  
  # Ensures image stays fixed on scroll
}

.sidebar .sidebar-content {
    background-color: rgba(0, 0, 0, 0.7);  # Semi-transparent sidebar background
    color: white;
}

.st-cb {  # Adjust padding for "Select a tab" based on your font size
    padding-top: 10px;
    padding-bottom: 10px;
}

.st-sh {  # Adjust header font size based on your preference
    font-size: 2.5em;
}

.st-t {  # Adjust body text size based on your preference
    font-size: 1.1em;
    line-height: 1.5;
}
"""

st.markdown("<style>" + css + "</style>", unsafe_allow_html=True)


if selected_tab == "About":
    st.header("About")
    st.image(base_path + "data/profile_picture1.jpg",width=300)  # Replace with your image path


    # About text
    st.write("""
    Currently, I am an applied AI/ML industry researcher at JP Morgan Chase & Co, Bangalore, India

    Beyond my professional pursuits, I'm fascinated by:
    - Entrepreneurship: Turning ideas into impact
    - Algorithmic Trading
    - Robotics & Drones
    """)

    # Links to profiles
    st.write("""
    [:linkedin: LinkedIn]((https://www.linkedin.com/in/ranjan-mondal-176b0362/))
    [:google-scholar: Google Scholar](https://scholar.google.com/citations?user=JWuX_HsAAAAJ&hl=en)
    [:github: GitHub](https://github.com/ranjanZ)
    """)


    st.write("Let's connect and shape the future of AI/ML together!")



    st.header("Updates")


    # Create a list of your talks and tutorials with links
    talks_and_tutorials = [
        ("July 2024", "Invited talk at SERB Sponsored Workshop", "Deep Learning: Foundation to Cutting Edge Technologies", "UPES, Dehradun, India", "https://www.linkedin.com/feed/update/urn:li:activity:7218653272482471936/"),
        ("Nov 2022", "Accepted full paper at BMVC ", "Morphological Network: How Far Can We Go with Morphological Neurons?","London, UK", "https://bmvc2022.mpi-inf.mpg.de/"),
        ("March 2022", "Invited talk", "Learning with structuring elements", "Winter School on Deep Learning, ISI, Kolkata, India", "https://sites.google.com/view/wsdl2022/home?authuser=0"),
        ("March 2020", "Invited talk", "Deep Learning", "Indian Institute of Information Technology (IIIT), Guwahati, India", "https://www.iiitg.ac.in/event?per_page=1"),
        ("July 2019", "Tutorial", "Data Visualization using Python", "ISI-ICTP Summer School on Internet of Things, Indian Statistical Institute, Kolkata", "https://www.isical.ac.in/~ss_iot/"),
        ("Jan. 2019", "Invited talk", "Object Supervised Learning to Adversarial Learning", "Techno Main, Salt Lake, Faculty Development Program on Image and Vision Computing", ""),
        ("June. 2018", "Tutorial", "Convolutional Neural Network and Autoencoder", "Indian Statistical Institute (Kolkata), Fourth Summer School on Computer Vision, Graphics and Image Processing", "https://www.isical.ac.in/~ecsu/?q=CFP"),
        ("April. 2017", "Invited talk", "Python", "Midnapore college (Medinipur, West Bengal), Workshop in Python", "https://midnaporecollege.ac.in/"),
        ("Feb. 2016", "Invited talk", "System Administration", "University of Calcutta, IEEE Electron Devices Society sponsored workshop in Python and System Administration", ""),
    ]


    # Display the talks and tutorials as bullet points with links
    for year, talk_type, topic, location, link in talks_and_tutorials:
        st.markdown(f"- **{year}**: {talk_type} on **{topic}** at **{location}** [Link]({link})")



elif selected_tab == "Carrier and  Experience":
  st.header("**🚀 Experience**")

  industry_experience_data = [
    (
      "JP Morgan Chase & Co.",
      "Bangalore, India",
      "Jan 2023 - Present",
      """Applied AI/ML as AVP. Working on applied AI/ML in financial domain. Specifically, working on large scale graph learning, mathematical modeling of financial optimization problems, and large language models.""",
    ),
    (
      "Samsung Research",
      "Bangalore, India",
      "2021 - 2023",
      """Lead Research Engineer. Worked on state-of-the-art video panoptic segmentation problems for different embedded platforms. It involves real time instance tracking, temporal stability accurate mask prediction for video.""",
    ),
    (
      "Advanced Micro Devices (AMD), Bengaluru, India",  # Company
      "June 2014",  # Dates (assuming it was a one-month internship)
      "Summer Intern",  # Location
      """Mentored by Dr. Anasua Bhowmik (Principal Member of Technical Staff). [Brief description of your internship experience here]. Include details like the projects you worked on and the skills you gained."""  # Description
    ),
  ]

  academic_experience_data = [
    (
      "Indian Statistical Institute (ISI), Kolkata, India",
      "2015 - 2021",
      """Doctor of Philosophy in Machine Learning and Computer Vision""",
      """ Thesis: Morphological Network: Learning with Morphological Neurons. Supervisor: Prof. Bhabatosh Chanda.""",
    ),
    (
      "Indian Statistical Institute (ISI), Kolkata, India",
      "2013 - 2015",
      "Master of Technology (M.Tech), Computer Science",
      """Percentile: First Division with Distinction - 76%. Dissertation: Unified Pre-fabrication and Post-fabrication Hardware Security. Supervisor: Prof. Susmita Sur-Kolay.""",
    ),
    (
      "Kalyani Government Engineering College, Kalyani, India",
      "2009 - 2013",
      "Bachelor of Technology (B.Tech), Computer Science and Engineering",
      """DGPA: 8.08. Project: Linux Kernel and File System Development.""",
    ),
  ]

  st.subheader("🚀 Industry Experience")
  for company, dates, location, description in industry_experience_data:
    with st.expander(company, expanded=True):
      st.write(f"**Location:** {location}")
      st.write(f"**Dates:** {dates}")
      st.write(description)

  st.subheader("🎓 Academic Experience")
  for company, dates, location, description in academic_experience_data:
    with st.expander(company, expanded=True):
      st.write(f"**Location:** {location}")
      st.write(f"**Dates:** {dates}")
      st.write(description)





















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
    st.title("Publications and Preprints")
    st.write("[Google Scholar](https://scholar.google.com/citations?user=JWuX_HsAAAAJ&hl=en)", unsafe_allow_html=True)





elif selected_tab == "Blogs":
    st.title("Ranjan's Blog")
    st.write("A collection of thoughts and insights on AI, ML, Trading and more.")


    # Blog content section
    st.markdown("---")  # Horizontal separator
    # Looping through articles (replace with actual data)
    articles = [
        {
            "title": "Tensor differentiation",
            "excerpt": "Before going into Deep learning, one of the major concepts is needed tensor calculus...",
            "link": "",
            "date": "2016-04-28",
            "author": "Ranjan M.",
            "all content": blog_tensor_diff,

        },
        {
            "title": "Volume Spread analysis",
            "excerpt": "Volume Spread Analysis (VSA) is a technical analysis technique used to identify market trends and patterns by analyzing..",
            "date": "2024-07-21",
            "author": "Ranjan M.",
            "all content": VSA,
        },
         {
            "title": "Arbitrage: Making Free Money from Market!! Just Wait for the Opportunity",
            "excerpt": "Coming....",
            "date": "2024-10-20",
            "author": "Ranjan M.",
            "all content":Arbitrage ,
        },


    ]



    def render_blog_post(title, excerpt, date, author, all_content):
        st.subheader(title)
        st.markdown(f"**{date}** | {author}")
        st.markdown(excerpt)

        if st.button("Read More", key=date):
            st.markdown(all_content(st))

        st.markdown("---")  # Horizontal separator




    # Looping through articles
    for article in articles:
        render_blog_post(article["title"], article["excerpt"], article["date"], article["author"], article["all content"])



    # Pagination (example using placeholders)
    #st.markdown("**Page 1 of 2**")
    #st.markdown("[Older Posts &raquo;](placeholder_older_posts_link)", unsafe_allow_html=True)  # Replace with actual link

    # Footer section
    st.markdown("---")  # Horizontal separator
    st.markdown("© ranjan's blog")





















































elif selected_tab == "Contact":
    st.header("Contact")
    st.write("**Email:** ranjan.rev@gmail.com")
    st.write("**Phone:** +91 6290153xxx -- you have to try 10^3 times")
    st.write("**Website:** https://ranjanz.github.io/")



elif selected_tab == "My Story":
    st.header("My Story")
    st.write(
        """
    Applied Research Scientist 
    As a child, I dreamed of becoming a cricketer or an astronaut, but growing up in a lower middle-class family, I soon faced the harsh realities of life. I scaled down my ambitions and set my sights on becoming a primary school teacher, with a modest salary of ₹12,000/month. However, fate had other plans, and an injury crushed my cricketing aspirations.

    Until the 8th grade, I was an unenthusiastic student, believing that academic success wouldn't guarantee a bright future. But everything changed when I discovered my passion for mathematics, particularly geometry, and solving Olympiad problems, inspired by my brilliant friend Soumendu.

    From that moment on, I began my journey, and I'm still amazed at how far I've come. My story is one of perseverance, self-discovery, and the power of embracing one's true potential."

    I believe I don't have much natural brainpower, but I've learned to compensate for it with sheer hard work. I firmly believe that anyone can compensate for intelligence with hard work.

    """
    )



    st.subheader("Beyond the Maths, Stats, and Code")
    st.write(
        """
        - **My goal and Social Impact:** I believe that in India, the rich are getting richer while the poor are getting poorer, I want to reduce this gap. A farmer gives all his hard work to make the rich people richer, but they receive nothing. I am confident that I can make a positive change, even if it's only for a small percentage of our population.

        - **Algorithmic Trading:** I explore statistical arbitrage, backtesting, and finding an edge in the Indian market for derivatives as well as equity.
        - **Travelling:** "Thailand, France, Germany, Porugal, Australia, Jordan(upcoming..) "
        """
    )





# Footer
st.write("© 2024 Ranjan Mondal")






