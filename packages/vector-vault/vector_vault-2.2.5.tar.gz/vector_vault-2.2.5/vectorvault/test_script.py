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

article_list = ['Technology', 'Science', 'Politics', 'Health', 'Sports', 'Entertainment', 'Business', 'Education', 'Environment', 'Travel']

article = '''
Title: The Transformational Power of Online Learning

In the modern era, education has experienced a remarkable transformation, 
moving beyond the traditional boundaries of classrooms and textbooks. Online 
learning has emerged as a powerful tool, revolutionizing the way people acquire 
knowledge and skills. With the convenience and flexibility it offers, online learning 
has become increasingly popular across different age groups and in various domains.

Online learning provides opportunities for individuals to access education from the 
comfort of their homes or any other location of their choice. The elimination of 
geographical barriers allows students to learn from the best institutions and 
instructors around the world, expanding their horizons and gaining diverse perspectives.
The flexibility of online learning allows for personalized learning experiences, 
suiting the pace and needs of every learner.

One of the greatest advantages of online learning is the ability to learn at any 
time, enabling those with busy schedules or multiple commitments to pursue their 
education. Whether you are a working professional, a parent, or someone with a 
tight schedule, online learning provides the flexibility to balance your learning 
journey with other responsibilities.

Another key benefit of online learning is its accessibility. People from all walks 
of life, regardless of their socio-economic background, can access quality education 
through online platforms. This inclusivity is transforming education, as it reduces 
the educational divide and empowers individuals to improve their knowledge and skills, 
ultimately leading to enhanced professional opportunities and personal growth.

Online learning also fosters a collaborative and interactive learning environment. 
Through discussion forums, virtual classrooms, and social media platforms, students 
can connect with peers and instructors worldwide, engage in meaningful discussions, 
and gain from a diverse range of perspectives. This exchange of ideas helps in broadening 
understanding, challenging conventional thoughts, and fostering a global learning community.

Furthermore, online learning opens up new opportunities for continuous learning and 
upskilling. With rapidly evolving industries and technological advancements, it is crucial 
to stay updated. Online platforms offer a vast array of courses and programs catering to 
different fields of study, enabling individuals to acquire new skills or enhance existing 
ones conveniently.

As online learning continues to gain momentum, it is essential to acknowledge the potential 
of technology in shaping education for future generations. However, it is equally important to 
ensure the quality and integrity of online education platforms and maintain a balance between the 
benefits of virtual learning and the advantages of in-person instruction.

In conclusion, online learning has revolutionized the education landscape, offering flexibility, 
accessibility, collaboration, and personalization. Its transformative power is evident in breaking 
down barriers, bringing education to individuals worldwide, and fostering a lifelong learning mindset.
 As technology continues to advance, the potential for online learning to positively impact education 
 and empower learners is boundless.
'''

tools = vault.tools

article_category = tools.get_binary(article, zero_if="this is about education", one_if="this is about technology")

print(article_category, print(type(article_category)))

if article_category == 0:
    print("this is an example of AI programming")