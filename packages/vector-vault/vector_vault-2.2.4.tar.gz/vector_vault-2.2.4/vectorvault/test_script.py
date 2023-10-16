# AI Decision Making
# AI can take unstructured data and turn it into structured data
# This can process any data and create an actionable metric from the data 
# We can use this to go where code has never gone before

from vectorvault import Vault

vault = Vault(
    user = "john.rood@decision.com",
    api_key= "6632a45f_a49d_45b5_bf15_1760b5a26866",
    openai_key= "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",
    vault = "demo",
    verbose=True
)

llm = vault.ai.llm

article_list = ["Politics", "Sports", "Technology", "Entertainment", "Health", "Science", 
                "Business", "Education", "Travel", "Fashion", "Food", "Environment", 
                "Opinion", "Culture", "Finance", "Lifestyle", "Sports", "Music", "Art", "History"]

article = '''
Title: The Impact of Technology on Education: Bridging Gaps and Unlocking Potential

Introduction:
In recent years, the integration of technology in education has disrupted traditional teaching methods and 
revolutionized the way we learn. With advancements in technology permeating every aspect of our lives, it is 
no wonder that it has found its place in the educational sector. This article explores the immense impact of 
technology on education, elucidating the benefits, challenges, and transformative potential it brings to learners 
across the globe.

The Accessibility and Inclusivity Revolution:
One of the most significant advantages of technology in education is its ability to bridge physical 
and educational gaps. By employing online learning platforms, virtual classrooms, and educational apps, 
technology ensures that access to quality education is no longer restricted by geographical boundaries. 
Students living in remote areas or facing physical limitations can now gain knowledge and interact 
with teachers and peers in real-time, fostering a sense of inclusivity and creating an equitable 
learning environment.

Personalized Learning and Increased Engagement:
Technology enables educators to tailor teaching methods and adapt to individual student needs. 
Adaptive learning platforms use algorithms to assess students' strengths and weaknesses, 
allowing teachers to provide personalized instruction. This flexibility cultivates a student-centered 
learning experience, keeping students engaged and motivated. Interactive tools, such as educational 
games and augmented reality (AR), enhance comprehension and make learning enjoyable, transforming 
education into a vibrant and interactive experience.

Preparing Students for the Digital Age:
In today's digital world, technological literacy is an essential skill for success. Integrating 
technology effectively into classrooms equips students with the necessary digital literacy, 
information gathering, and critical thinking skills required for the 21st century. By familiarizing 
students with various technological tools and software, educational institutions empower them to 
become lifelong learners who adapt and thrive in an increasingly technology-dependent society.

Overcoming Challenges:
While technology has proven to be a valuable educational tool, it is not without its challenges. 
The digital divide, inadequate access to resources, and technological infrastructure constraints 
persist in certain regions, exacerbating educational inequalities. Moreover, concerns surrounding 
privacy and online safety require continuous vigilance and updates to security measures. However, 
acknowledging these challenges and actively working towards their resolution allows us to create 
a more inclusive and secure educational environment.

The Future of Education:
Technology will continue to reshape education by fostering innovation and paving the way for 
personalized, student-focused learning experiences. Emerging technologies like virtual 
reality (VR), artificial intelligence (AI), and blockchain hold immense potential to further 
revolutionize education. VR can transport students to virtual worlds, expanding their understanding 
beyond the confines of traditional education. AI can provide personalized guidance and feedback, 
ensuring every student maximizes their potential. Blockchain, with its transparency and 
immutability, can allow for the validation of credentials and enable lifelong learning.

Conclusion:
The integration of technology in education is no longer a choice but a necessity. As we witness the 
rapid evolution of technology, it becomes imperative to embrace its potential and harness it for the 
betterment of education worldwide. By utilizing technology to enhance accessibility, personalize 
learning, and prepare students for the digital age, we ensure that education remains relevant, 
inclusive, and empowers future generations to thrive in an ever-changing world.
'''

tools = vault.tools

match_ = tools.get_match(text=article, list_of_options=article_list)

print(match_)