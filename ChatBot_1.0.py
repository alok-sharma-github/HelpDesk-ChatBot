import difflib
from transformers import pipeline
import streamlit as st


data =  [
    {"question": "Full support commitment developer working per business hour", "answer": "Inzint provides full support commitment with developers working per business hour."},
    {"question": "Who are you?", "answer": "Oh!, well if you really don't know Inzint's ChatBot for info retrieval."},
    {"question": "Custom software development", "answer": "Inzint offers custom software development services to provide innovative software designed as per the client's needs using the latest technology."},
    {"question": "Cloud computing services", "answer": "Inzint delivers hosting services that are reliable and provide network hosting globally, starting from cloud computing to remote resource hiring without additional entities, increasing productivity and adaptability by using remote resource services."},
    {"question": "Mobile app development", "answer": "Inzint specializes in developing Android as well as iOS apps that work across multiple platforms."},
    {"question": "Web development", "answer": "Inzint offers scalable web development services to automate work processes and enhance user experiences."},
    {"question": "Software consultation", "answer": "Inzint provides consultancy services to help identify and overcome technology barriers that hinder business growth."},
    {"question": "Why choose Inzint?", "answer": "Inzint is a pioneering software service provider in Noida, consistently delivering business value through the latest technology."},
    {"question": "Our mission and vision", "answer": "We are determined to be an organization working to deliver custom software solutions that enhance the digital journey using frontier technology to address challenges."},
    {"question": "Our technology partners", "answer": "Inzint relies on leading technology partners to provide products that meet the needs of our clients."},
    {"question": "What is the process for custom software development at Inzint?", "answer": "At Inzint, the process for custom software development involves understanding the client's requirements, designing and creating the software, deploying it, and providing ongoing maintenance and support."},
    {"question": "Can Inzint help with data transformation?", "answer": "Yes, Inzint can help accelerate the cycle of data transformation by offering digital enablement services to drive key business outcomes using a full-service digital stack."},
    {"question": "What is the innovation partnership approach at Inzint?", "answer": "Inzint adopts a collaborative approach to innovation, leveraging an innovation lab and forming alliances to create the future financial ecosystem."},
    {"question": "What are the career opportunities at Inzint?", "answer": "Inzint offers various career opportunities for talented individuals, including roles such as full-stack developers, backend developers, software project managers, and trainee developers."},
    {"question": "How can I contact Inzint for software consultation?", "answer": "You can contact Inzint for software consultation by reaching out to our team through the contact form on our website or by emailing us directly."},
    {"question": "What are the benefits of choosing Inzint for custom software development?", "answer": "Choosing Inzint for custom software development ensures that you receive a solution tailored to your specific needs, with a focus on cost-effectiveness, transparency, and superior customer service."},
    {"question": "What industries does Inzint serve?", "answer": "Inzint serves a wide range of industries, including healthcare, finance, education, retail, manufacturing, and more."},
    {"question": "How does Inzint ensure data security in cloud computing?", "answer": "Inzint ensures data security in cloud computing by implementing robust security measures, such as encryption, access controls, and regular security audits."},
    {"question": "Can Inzint help with SEO strategy?", "answer": "Yes, Inzint can assist with SEO strategy by providing services such as building backlinks, improving domain authority, and optimizing website content for search engines."},
    {"question": "What is the future of conversational AI at Inzint?", "answer": "At Inzint, the future of conversational AI is bright, with ongoing advancements in chat capabilities and the adoption of innovative AI models such as GPT (Generative Pre-trained Transformer)."},
    {"question": "What is the process for custom software development at Inzint?", "answer": "At Inzint, the process for custom software development involves understanding the client's requirements, designing and creating the software, deploying it, and providing ongoing maintenance and support."},
    {"question": "Can Inzint help with data transformation?", "answer": "Yes, Inzint can help accelerate the cycle of data transformation by offering digital enablement services to drive key business outcomes using a full-service digital stack."},
    {"question": "What is the innovation partnership approach at Inzint?", "answer": "Inzint adopts a collaborative approach to innovation, leveraging an innovation lab and forming alliances to create the future financial ecosystem."},
    {"question": "What are the career opportunities at Inzint?", "answer": "Inzint offers various career opportunities for talented individuals, including roles such as full-stack developers, backend developers, software project managers, and trainee developers."},
    {"question": "How can I contact Inzint for software consultation?", "answer": "You can contact Inzint for software consultation by reaching out to our team through the contact form on our website or by emailing us directly."},
    {"question": "What are the benefits of choosing Inzint for custom software development?", "answer": "Choosing Inzint for custom software development ensures that you receive a solution tailored to your specific needs, with a focus on cost-effectiveness, transparency, and superior customer service."},
    {"question": "What industries does Inzint serve?", "answer": "Inzint serves a wide range of industries, including healthcare, finance, education, retail, manufacturing, and more."},
    {"question": "How does Inzint ensure data security in cloud computing?", "answer": "Inzint ensures data security in cloud computing by implementing robust security measures, such as encryption, access controls, and regular security audits."},
    {"question": "Can Inzint help with SEO strategy?", "answer": "Yes, Inzint can assist with SEO strategy by providing services such as building backlinks, improving domain authority, and optimizing website content for search engines."},
    {"question": "What is the future of conversational AI at Inzint?", "answer": "At Inzint, the future of conversational AI is bright, with ongoing advancements in chat capabilities and the adoption of innovative AI models such as GPT (Generative Pre-trained Transformer)."},
    {"question": "How can I contact Inzint for software consultation?", "answer": "You can contact Inzint for software consultation by reaching out to our team through the contact form on our website or by emailing us directly."},
    {"question": "What services does Inzint provide?",
     "answer": "Inzint provides full support and commitment to developers working per business hour. We offer custom software development tailored to your needs using the latest technology. Additionally, we provide cloud computing services, delivering reliable hosting solutions through a global network of hosting providers. Our cloud computing services also include remote resource hiring to increase productivity and adaptability without additional entities."},
    {"question": "What expertise does Inzint offer in mobile app development?",
     "answer": "Inzint specializes in mobile app development, offering expertise in developing Android as well as iOS apps. Our developers are skilled in working across multiple platforms to ensure optimal performance and user experience."},
    {"question": "How does Inzint enhance web development processes?",
     "answer": "Inzint offers scalable web development services to automate work processes and enhance user experiences. Our team leverages the latest technologies to create innovative solutions that streamline workflows and improve efficiency."},
    {"question": "What role does software consultation play at Inzint?",
     "answer": "Inzint provides software consultation services to help businesses identify and overcome technology barriers that may hinder their growth. Our consultants partner with companies to understand their needs and provide tailored solutions."},
    {"question": "What is Inzint's mission and vision?",
     "answer": "Inzint is determined to deliver custom software solutions that enhance the digital journey of our clients using frontier technology. Our mission is to help businesses of all sizes and verticals accomplish their goals."},
    {"question": "What are the core principles of Inzint?",
     "answer": "One of Inzint's defining principles is to rely on leading technology partners to provide products that meet our clients' needs. We also have a highly experienced management team dedicated to delivering reliable and secure technology solutions."},
    {"question": "What is the importance of customer service at Inzint?",
     "answer": "At Inzint, we strive to provide superior customer service to ensure every client is completely satisfied with our work. Our engineers are trustworthy, dedicated, and experienced, going the extra mile to solve issues with quality solutions."},
    {"question": "How does Inzint approach innovation?",
     "answer": "Inzint adopts a collaborative approach to innovation, leveraging our innovation lab and forming partnerships with leading technology companies. We are always accommodating diverse needs and strive to be a part of our clients' success."},
    {"question": "What career opportunities are available at Inzint?",
     "answer": "Inzint offers various career opportunities for individuals passionate about technology and innovation. We have roles ranging from full-stack developers and engineers to management and business development positions."},
    {"question": "Where is Inzint located and how can I contact them?",
     "answer": "Inzint has offices in Noida, Sydney, and the United States. You can contact us through our website or by reaching out to our team members directly via email or phone."},
    {"question": "Who are the founders of Inzint?",
     "answer": "Inzint was founded by Jaideep Jai, Vikas Thakur. They are the directors of the company and have a long history of success in technology, business management, and franchising."},    
    {"question": "What is the team composition at Inzint?",
     "answer": "The team at Inzint consists of highly skilled professionals across various roles. We have engineers, managers, business development executives, HR managers, accountants, quality engineers, and more. Each member of our team is dedicated to delivering outstanding solutions and adding real value to our clients."},
    {"question": "How does Inzint ensure quality in its team?",
     "answer": "At Inzint, we have a rigorous hiring process to ensure that we onboard the best talent. Our people are at the heart of our operation, and we are fanatical about finding the brightest problem solvers in the industry. We provide a great place to work and choose people who are smart and dedicated to our mission."},    
    {"question": "What is the role of customer service at Inzint?",
     "answer": "Inzint strives to provide superior customer service to ensure that every client is completely satisfied with our work. Our engineers are trustworthy, dedicated, and experienced, and they go the extra mile to solve issues with quality solutions."},
    {"question": "What are the core values of Inzint's team?",
     "answer": "At Inzint, we value transparency, customer satisfaction, quality, and innovation. Our team is committed to delivering outstanding cutting-edge solutions that add real value to our clients. We believe in going beyond expectations and providing the best possible service."},
    {"question": "What career opportunities are available at Inzint?",
     "answer": "Inzint offers various career opportunities for individuals passionate about technology and innovation. We have roles ranging from full-stack developers and engineers to management and business development positions. We are always looking for talented individuals to join our team."},
    {"question": "How can I join the team at Inzint?",
     "answer": "If you are interested in joining the team at Inzint, you can check our current openings on our website or reach out to us directly. We are always looking for talented and passionate individuals to join our team and help us achieve our mission."},
    {"question": "Who are the founders of Inzint?",
     "answer": "Inzint was founded by Jaideep Jai, Vikas Thakur. They are the directors of the company and have a long history of success in technology, business management, and franchising."},  
    {"question": "What is the role of Jaideep Jai at Inzint?",
     "answer": "Jaideep Jai is one of the directors of Inzint. He plays a key role in shaping the company's vision and strategy, leveraging his expertise in technology and business management."},
    {"question": "What is the role of Vikas Thakur at Inzint?",
     "answer": "Vikas Thakur is also a director at Inzint. He brings his extensive experience in technology and franchising to the company, helping drive its growth and success."},
    {"question": "What is the role of Kakoli at Inzint?",
     "answer": "Kakoli is HR at Inzint. With her background in business management, she contributes to the company's operations and strategic decision-making process."},
    {"question": "Who is the HR manager at Inzint?",
     "answer": "Kakoli and Mohini is the HR manager at Inzint. She oversees all HR-related activities, including recruitment, employee relations, and performance management."},
    {"question": "What is the role of the engineers at Inzint?",
     "answer": "The engineers at Inzint are responsible for developing cutting-edge software solutions for our clients. They work across various technologies and platforms to deliver high-quality products."},
    {"question": "Who is the business development manager at Inzint?",
     "answer": "Amit is the business development manager at Inzint. He leads the company's efforts to acquire new clients and expand its business operations."},
    {"question": "What is the role of the quality engineer at Inzint?",
     "answer": "Dennis is the quality engineer at Inzint. He ensures that all products and services meet the highest quality standards through rigorous testing and quality assurance processes."},
    {"question": "Who is responsible for project management at Inzint?",
     "answer": "Jayesh is responsible for project management at Inzint. He oversees the planning, execution, and delivery of projects to ensure they are completed on time and within budget."},
    {"question": "What is the role of the corporate trainer at Inzint?",
     "answer": "Vanshika is the corporate trainer at Inzint. She conducts training sessions to enhance the skills and knowledge of our employees, ensuring they stay updated with the latest technologies and industry trends."},
    {"question": "What services does Inzint provide?",
     "answer": "Inzint provides full support and commitment to developers, working per business hour. They offer custom software solutions designed as per the client's needs using the latest technology. They also specialize in cloud computing, delivering reliable hosting services worldwide. Additionally, they offer cloud computing remote resource hire to increase productivity and adaptability without the need for additional entities."},    
    {"question": "What expertise does Inzint have in mobile app development?",
     "answer": "Inzint has expertise in developing mobile apps for both Android and iOS platforms. Their team of experts works across multiple platforms to deliver high-quality mobile applications."},
    {"question": "What services does Inzint offer for web development?",
     "answer": "Inzint offers scalable web development services. They specialize in automating work processes to enhance user experience."},
    {"question": "Who is Vanshika?","answer": "Vanshika is a corporate trainer at Inzint, who is well-trained and knowledgeable in AI/ML, Python, etc."},
    {"question": "Who is Vanshika at Inzint?","answer": "Vanshika is a corporate trainer at Inzint, who is well-trained and knowledgeable in AI/ML, Python, etc."},
    {"question": "How does Inzint provide software consultation?",
     "answer": "Inzint offers software consultation services where consultants help identify and overcome technology barriers that may hinder business growth. They partner with companies to provide the best solutions tailored to their needs."},
    {"question": "Who are the key members of the Inzint team?",
     "answer": "The key members of the Inzint team include Vikas Thakur (Director), Jaideep Jai (Director), Kakoli (Asst Manager HR), Dhiraj (Account Manager), Garima (Business Manager), and a team of skilled engineers and developers such as Amit, Aman, Dennis, Jayesh, Samkeet, Mordhawaj, Para, Shivam, Hardik, Saksham, Mohini, Vartika, and others."},  
    {"question": "What is the mission and vision of Inzint?",
     "answer": "The mission of Inzint is to deliver custom software solutions that enhance the digital journey of their clients using frontier technology. Their vision is to help organizations, both small and large, accomplish their goals through innovative software solutions."},
    {"question": "What is the main service offered by Inzint?",
     "answer": "Inzint provides custom software development services designed to meet specific demands, budgets, and timelines. They aim to lead the transformation of businesses by delivering innovative software solutions tailored to the client's needs. They take care of all stages of development, including product design, coding, testing, deployment, and support."},  
    {"question": "What is the expertise of Inzint in cloud computing?",
     "answer": "Inzint specializes in cloud computing and delivers reliable hosting services globally. They work with leading network hosting providers to ensure highly available and secure technology platforms. They also offer remote resource development services, allowing businesses to hire resources without additional entities, thereby increasing productivity and adaptability."},  
    {"question": "What expertise does Inzint have in mobile app development?",
     "answer": "Inzint is experienced in mobile app development, with expertise in developing apps for Android and iOS platforms. They work across multiple platforms to deliver high-quality mobile applications."},  
    {"question": "What services does Inzint offer for web development?",
     "answer": "Inzint offers scalable web development services. They specialize in automating work processes to enhance user experience."},  
    {"question": "How does Inzint ensure customer satisfaction?",
     "answer": "Inzint believes in providing customer satisfaction by incorporating ideas and suggestions at every stage of development. They strive to keep the development process transparent, involving customers in evaluating progress."},
    {"question": "What is the innovation and technology expertise of Inzint?",
     "answer": "Inzint has a strong technology development and innovation presence in the USA, Australia, and India. They use their expertise and tech background to provide powerful and adaptable digital solutions, transforming businesses and ensuring customer satisfaction."},
    {"question": "What is the history of Inzint?",
     "answer": "Inzint began as a freelancing division of a software company in 2015, completing various projects across multiple domains. In 2020, it became an independent company offering multiple services. It moved its office to Noida, India, where it witnessed new members joining the team, contributing to its talent pool. Inzint has made its mark in the industry by delivering solutions to clients on time and within budget. It has received external recognition and has completed extensive training to consistently meet the needs of its customers."},
    {"question": "Where are the locations of Inzint offices?",
     "answer": "Inzint has offices in Noida, India (G13, Sector 3, Noida, India 201301), Australia (15 Carrington Rd, Marrickville, Australia 2204), and the United States (214 Fairway Green Dr, Fallon, MO, USA 63368). You can also contact them at +253."},
    {"question": "What services does Inzint offer for software consultation?",
     "answer": "Inzint provides software consultation services to help identify technology barriers and improve business performance, scalability, and competitiveness. Their experienced consultants offer unbiased and independent views to align technology with business plans."},
    {"question": "How does Inzint help businesses improve service efficiency?",
     "answer": "Inzint offers comprehensive services, including network management, monitoring, and service desk support. They use the latest technology and best practices to ensure products meet market demands and provide the best possible user experience. Businesses can scale costs according to their requirements and benefit from a trusted advisor relationship with Inzint."},
    {"question": "How does Inzint accommodate diverse needs?",
     "answer": "Inzint always accommodates diverse needs and makes clients feel like a part of the company rather than an external supplier. They prioritize client satisfaction and strive to meet unique requirements."},    
    {"question": "Who is Laurie Mahon and how can they help with custom software?",
     "answer": "Laurie Mahon is associated with PBT Solution. They can help with custom software development. Clients can contact them today for an overview of solutions and benefits."},    
    {"question": "What is the process for custom software development at Inzint?",
     "answer": "Inzint follows a specific process for custom software development, keeping client demands in mind. This process includes designing, creating, deploying, and maintaining software to meet organizational functions. They believe in providing cost-competitive solutions to meet unique requirements."},  
    {"question": "How does Inzint's custom software service help businesses succeed?",
     "answer": "Inzint's custom software service ensures the success of businesses by offering comprehensive services. These include network management, monitoring, and service desk support. They maximize service efficiency, resolve problems, and drive continuous improvement in service and infrastructure."},
    {"question": "How does Inzint help companies reach their full potential?",
     "answer": "Inzint helps companies reach their full potential by expanding their digital footprint across mobile and web platforms. They provide superior software, web, mobile, and cloud solutions globally. With their strong technology development and innovation centers in Noida and Sydney, they transform businesses and ensure customer satisfaction."},  
    {"question": "What are the current openings at Inzint?",
     "answer": "Inzint has openings for full-stack developers and backend developers in Noida. They are always looking for talented individuals to join their team."},
    {"question": "What are the benefits of being a member of Inzint?",
     "answer": "Members of Inzint receive benefits such as assigned devices to enhance their work experience."},
    {"question": "What are some perks offered by Inzint to its employees?",
     "answer": "Inzint offers flexibility in work hours, approved vacation, paid maternal and parental leave, unlimited healthy catered lunches and beverages, fun board games, team outings, and company parties. These perks encourage excellent performance and foster a positive work environment."},
    {"question": "How has the understanding of chat capability changed with the latest version of GPT?",
     "answer": "The latest version of GPT (Generative Pre-trained Transformer) has improved chat capabilities. It is a natural language processing model developed by OpenAI. Compared to its predecessor, it promises more advanced chat capabilities."},
    {"question": "How has GPT transformed marketing?",
     "answer": "Chat GPT has completely changed the way companies communicate with clients, especially in the area of marketing. It enables businesses to interact with customers in a more personalized manner, providing individualized experiences."},
    {"question": "What is the impact of GPT on customer service?",
     "answer": "GPT has revolutionized customer service by providing sophisticated language models that comprehend natural language and produce responses. This revolution is transforming the customer service sector."},
    {"question": "What is the significance of adopting agile methodology in software development?",
     "answer": "Adopting agile methodology in software development provides numerous benefits to development teams and organizations as a whole. One key benefit is adaptability, allowing teams to respond to changes and deliver value more efficiently."},
    {"question": "What is the MERN stack?",
     "answer": "The MERN stack is a group of strong technologies used to create scalable and feature-rich web applications. It includes MongoDB (a NoSQL database), Express.js (a web application framework), React (a JavaScript library for building user interfaces), and Node.js (a JavaScript runtime environment)."},
    {"question": "What is the future of AI according to a February 2023 article?",
     "answer": "According to the article, the future of AI includes highly developed systems like ChatGPT, which are capable of generating text responses resembling human speech. These systems are trained on large corpora of conversational text, enabling them to generate natural and coherent responses."},
    {"question": "Where are Inzint's regional offices located?",
     "answer": "Inzint has regional offices located around the world. Specifically, it has two regional offices across the globe. For assistance, one can visit their database messaging service at Australia: 15 Carrington Rd, Marrickville, Australia; India: Sector 3, Noida, India 201301; United States: 12379 Cross Creek Cove, Louis, MO 63141, USA."},
    {"question": "What services does Inzint offer regarding remote resources?",
     "answer": "Inzint offers remote resource hiring services without the need for additional entities. They prioritize productivity and adaptability, providing skilled developers and modern technology to manage software development remotely. Their comprehensive services ensure brilliant results for clients."},
    {"question": "How does Inzint prioritize communication with clients during the development process?",
     "answer": "Inzint prioritizes clear communication and direct interaction with developers to ensure that clients feel involved in the development process. This approach enables clients to communicate their requirements effectively."},
    {"question": "What industries does Inzint cater to with its custom software solutions?",
     "answer": "Inzint offers custom software solutions tailored to the unique needs of clients in various industries, including healthcare, cybersecurity, cloud services, and retail. The company adapts its services to meet the specific requirements of each industry."},
    {"question": "What factors contribute to Inzint being a reliable partner for businesses seeking software solutions?",
     "answer": "Inzint's dedication to customer satisfaction, focus on transparency and flexibility, and track record of successful projects contribute to its reputation as a reliable partner for businesses seeking innovative software solutions."},
    {"question": "What is the approach of Inzint towards managing costs in cloud computing?",
     "answer": "Inzint scales costs according to the client's requirements, whether increasing or decreasing staff or project work. Through regular account management meetings, the managed service company oversees the overall roadmap to become a trusted advisor. As businesses grow, the support structure can be scaled using managed services."},
    {"question": "How does Inzint assist in web development?",
     "answer": "Inzint offers web app development services that include scalable web development for any type of business. The company automates work processes and enhances customer experience using front-end technologies like JavaScript and back-end technologies like Got. The experienced software development team ensures the best results."},
    {"question": "What is Inzint's approach to mobile app development?",
     "answer": "Inzint offers mobile app development services for both iOS and Android platforms. The company assists in building applications that work equally well across devices. With expertise gained from 11 years of Android and iOS app development, Inzint promises reliable products appealing to platform users."},
    {"question": "When was Inzint started?",
     "answer": "Inzint was started in the year 2020."},
    {"question": "Who is corporate trainer?",
     "answer": "The corporate trainer at Inzint is Vanshika."},
    {"question": "Can you provide information about other team members at Inzint?",
     "answer": "Sure, here are some other team members at Inzint:\n- Amit: Engineer (Full Stack)\n- Aman: Engineer (Full Stack)\n- Dennis: Quality Engineer\n- Jayesh: Management\n- Samkeet: BD\n- Mordhawaj: Engineer (Full Stack)\n- Para: Software Engineer\n- Shivam: Software Engineer\n- Hardik: Software Engineer\n- Saksham: Software Engineer\n- Mohini: HR Executive\n- Vartika Pandey: Wordpress Developer\n- Kunal: Social Media Intern\n- Radhika: BDE Intern\n- Faizan: Engineer (Full Stack)\n- Parakh: Engineer (Full Stack)\n- Ziaul: Engineer (Full Stack)\n- Himannshu: Engineer (Full Stack)\n- Atif: Engineer (Full Stack)\n- Abhiraj: Engineer (Full Stack)\n- Alok Sharma: Trainee Developer\n- Priyanshu: Engineer (Full Stack)\n- Rohit: Engineer (Full Stack)\n- Md Imtiyaz: Office Administrator\n- Akash Kumar: Software Project Manager\n- Pratham: Trainee Developer\n- Ujjwal Deep: Trainee Developer\n- Ravi Kumar Ray: Trainee Developer\n- Sunny Patel: Trainee Developer\n- Shilpi Shukla: Trainee Developer\n- Adarsh Singh: Trainee Developer\n- Vansh Bhardwaj: Trainee Developer\n- Abhay Tyagi: Trainee Developer\n- Prashant Saini: Trainee Developer\n- Mohd Arman: Trainee Developer"},
    {"question": "Who is Amit?","answer": "Amit is an Engineer (Full Stack) at Inzint."},
    {"question": "Who is Aman?","answer": "Aman is an Engineer (Full Stack) at Inzint."},
    {"question": "Who is Dennis?","answer": "Dennis is a Quality Engineer at Inzint."},
    {"question": "Who is Jayesh?","answer": "Jayesh is in Management at Inzint."},
    {"question": "Who is Samkeet?","answer": "Samkeet is in BD at Inzint."},
    {"question": "Who is Mordhawaj?","answer": "Mordhawaj is an Engineer (Full Stack) at Inzint."},
    {"question": "Who is Para?","answer": "Para is a Software Engineer at Inzint."},
    {"question": "Who is Shivam?","answer": "Shivam is a Software Engineer at Inzint."},
    {"question": "Who is Hardik?","answer": "Hardik is a Software Engineer at Inzint."},
    {"question": "Who is Saksham?","answer": "Saksham is a Software Engineer at Inzint."},
    {"question": "Who is Mohini?","answer": "Mohini is the HR Executive at Inzint."},
    {"question": "Who is Vartika Pandey?","answer": "Vartika Pandey is a Wordpress Developer at Inzint."},
    {"question": "Who is Kunal?","answer": "Kunal is a Social Media Intern at Inzint."},
    {"question": "Who is Radhika?","answer": "Radhika is a BDE Intern at Inzint."},
    {"question": "Who is Faizan?","answer": "Faizan is an Engineer (Full Stack) at Inzint."},
    {"question": "Who is Parakh?","answer": "Parakh is an Engineer (Full Stack) at Inzint."},
    {"question": "Who is Ziaul?","answer": "Ziaul is an Engineer (Full Stack) at Inzint."},
    {"question": "Who is Himannshu?","answer": "Himannshu is an Engineer (Full Stack) at Inzint."},
    {"question": "Who is Atif?","answer": "Atif is an Engineer (Full Stack) at Inzint."},
    {"question": "Who is Abhiraj?","answer": "Abhiraj is an Engineer (Full Stack) at Inzint."},
    {"question": "Who is Alok Sharma?","answer": "Alok Sharma is a Trainee Developer at Inzint."},
    {"question": "Who is Priyanshu?","answer": "Priyanshu is an Engineer (Full Stack) at Inzint."},
    {"question": "Who is Rohit?","answer": "Rohit is an Engineer (Full Stack) at Inzint."},
    {"question": "Who is Md Imtiyaz?","answer": "Md Imtiyaz is the Office Administrator at Inzint."},
    {"question": "Who is Akash Kumar?","answer": "Akash Kumar is the Software Project Manager at Inzint."},
    {"question": "Who is Pratham?","answer": "Pratham is a Trainee Developer at Inzint."},
    {"question": "Who is Ujjwal Deep?","answer": "Ujjwal Deep is a Trainee Developer at Inzint."},
    {"question": "Who is Ravi Kumar Ray?","answer": "Ravi Kumar Ray is a Trainee Developer at Inzint."},
    {"question": "Who is Sunny Patel?","answer": "Sunny Patel is a Trainee Developer at Inzint."},
    {"question": "Who is Shilpi Shukla?","answer": "Shilpi Shukla is a Trainee Developer at Inzint."},
    {"question": "Who is Adarsh Singh?","answer": "Adarsh Singh is a Trainee Developer at Inzint."},
    {"question": "Who is Vansh Bhardwaj?","answer": "Vansh Bhardwaj is a Trainee Developer at Inzint."},
    {"question": "Who is Abhay Tyagi?","answer": "Abhay Tyagi is a Trainee Developer at Inzint."},
    {"question": "Who is Prashant Saini?","answer": "Prashant Saini is a Trainee Developer at Inzint."},
    {"question": "Who is Mohd Arman?","answer": "Mohd Arman is a Trainee Developer at Inzint."},
    {"question": "Who is Kakoli?","answer": "Kakoli is the HR Assistant Manager at Inzint."},
    {"question": "Who is Vikas Thakur?","answer": "Vikas Thakur is the Co-Founder of Inzint. He is also a Developer proficient in JavaScript & Python."},
    {"question": "Who is Jaideep Goyal?","answer": "Jaideep Goyal is the Co-Founder of Inzint. He specializes in Software Development, Web 3, Metaverse, and Custom Solution."},
    {"question": "What services does Inzint provide?","answer": "Inzint provides a range of services including Metaverse, IT Services, Mobile App Development, Web Development, Cloud Computing, Custom Software, Remote Resources, and Software Consultation."},
    {"question": "When was Inzint founded?","answer": "Inzint was founded in 2020."},
    {"question": "What is the industry of Inzint?","answer": "Inzint operates in the Information Technology & Services industry."},
    {"question": "What is the size of Inzint?","answer": "Inzint has 11-50 employees."},
    {"question": "Where is the headquarters of Inzint located?","answer": "The headquarters of Inzint is in Noida, Uttar Pradesh."},
    {"question": "What are the specialties of Inzint?","answer": "Inzint specializes in Web Development, Mobile App, Cloud, Software Maintenance, Software Consultancy, Remote Resource, Blockchain Development, AI/ML Development, AR/VR, and Metaverse."},
    {"question": "What is the website of Inzint?","answer": "The website of Inzint is https://inzint.com."},
    {"question": "What is the phone number of Inzint?","answer": "The phone number of Inzint is +91 92899 09174."},
    {"question": "What are the major industries that Inzint serves?","answer": "Inzint serves a wide range of industries including healthcare, cybersecurity, retail, finance, and more. We tailor our solutions to meet the unique needs of each industry."},
    {"question": "How does Inzint ensure the security of its software solutions?","answer": "Security is a top priority at Inzint. We employ industry-standard security practices and protocols to ensure the confidentiality, integrity, and availability of our clients' data. Additionally, our team undergoes regular security training to stay updated on the latest threats and vulnerabilities."},
    {"question": "Can Inzint provide examples of successful projects?","answer": "Certainly! Inzint has successfully completed numerous projects across various industries. From developing custom software solutions to implementing cloud-based services, our portfolio showcases our expertise and dedication to client satisfaction."},
    {"question": "How does Inzint handle communication during the development process?","answer": "At Inzint, we prioritize clear communication and direct interaction with our clients. We provide regular updates on project progress and encourage client feedback throughout the development lifecycle. Our goal is to ensure that clients feel involved and informed every step of the way."},
    {"question": "Who was the founder of Inzint?","answer": "The founders of Inzint are Vikas Thakur and Jaideep Goyal."},
    {"question": "What technologies does Inzint specialize in?","answer": "Inzint specializes in a wide range of technologies including Machine learning, Artificial Intellegence, Blockchain, JavaScript, Python, Java, PHP, HTML5, CSS3, React, Angular, Vue.js, Node.js, MongoDB, MySQL, AWS, Microsoft Azure, Google Cloud Platform, and more. We leverage these technologies to deliver cutting-edge solutions to our clients."},
    {"question": "What services does Inzint offer?","answer": "Inzint offers a range of services including Metaverse development, IT services, mobile app development, web development, cloud computing, custom software solutions, remote resources, and software consultation."},
    {"question": "How experienced is Inzint in the industry?","answer": "Inzint has over 7 years of expertise in the technology industry. Our team is committed to providing cutting-edge solutions to companies of all sizes."},
    {"question": "Can Inzint help with API integrations?","answer": "Absolutely! Inzint specializes in seamless API integrations to enhance your business operations. Whether it's integrating third-party services or building custom APIs, we've got you covered."},
    {"question": "What makes Inzint stand out from other technology service providers?","answer": "Inzint stands out for its commitment to excellence, innovation, and customer satisfaction. Our team comprises talented and passionate individuals dedicated to providing the best experience to our clients worldwide."},
    {"question": "How can I get in touch with Inzint for further inquiries?","answer": "You can reach out to us via phone at +91 92899 09174 or visit our website at https://inzint.com for more information. Additionally, feel free to drop us an email at [email protected] We look forward to hearing from you!"},
    {"question": "Who was the founder of Inzint?","answer": "The founders of Inzint are Vikas Thakur and Jaideep Goyal."},
    {"question": "How does Inzint ensure the quality of its software solutions?","answer": "Quality assurance is integral to our development process at Inzint. We follow rigorous testing procedures, including unit testing, integration testing, and user acceptance testing, to ensure that our software meets the highest standards of quality and reliability."},
    {"question": "Can Inzint assist with digital transformation initiatives?","answer": "Absolutely! Inzint specializes in helping businesses navigate digital transformation. Whether it's migrating to the cloud, implementing AI/ML solutions, or developing innovative mobile apps, we have the expertise to drive your digital transformation initiatives forward."},
    {"question": "What sets Inzint apart from other technology service providers?","answer": "At Inzint, we differentiate ourselves through our commitment to client satisfaction, our depth of technical expertise, and our innovative approach to problem-solving. We strive to exceed client expectations at every turn and deliver solutions that drive tangible business results."},
    {"question": "How does Inzint handle data privacy and compliance?","answer": "Data privacy and compliance are paramount concerns for Inzint. We adhere to strict data protection regulations, such as GDPR and HIPAA, and implement robust security measures to safeguard sensitive information. Our team is well-versed in data privacy best practices and ensures compliance with relevant regulations."},
    {"question": "Can Inzint provide ongoing support and maintenance for software solutions?","answer": "Yes, Inzint offers comprehensive support and maintenance services to ensure the continued functionality and performance of our software solutions. Whether it's troubleshooting issues, implementing updates, or scaling infrastructure, our team is here to provide ongoing support to our clients."},
    {"question": "How does Inzint ensure the quality of its software solutions?", "answer": "Quality assurance is integral to our development process at Inzint. We follow rigorous testing procedures, including unit testing, integration testing, and user acceptance testing, to ensure that our software meets the highest standards of quality and reliability."},
    {"question": "Can Inzint assist with digital transformation initiatives?", "answer": "Absolutely! Inzint specializes in helping businesses navigate digital transformation. Whether it's migrating to the cloud, implementing AI/ML solutions, or developing innovative mobile apps, we have the expertise to drive your digital transformation initiatives forward."},
    {"question": "What sets Inzint apart from other technology service providers?", "answer": "At Inzint, we differentiate ourselves through our commitment to client satisfaction, our depth of technical expertise, and our innovative approach to problem-solving. We strive to exceed client expectations at every turn and deliver solutions that drive tangible business results."},
    {"question": "How does Inzint handle data privacy and compliance?", "answer": "Data privacy and compliance are paramount concerns for Inzint. We adhere to strict data protection regulations, such as GDPR and HIPAA, and implement robust security measures to safeguard sensitive information. Our team is well-versed in data privacy best practices and ensures compliance with relevant regulations."},
    {"question": "Can Inzint provide ongoing support and maintenance for software solutions?", "answer": "Yes, Inzint offers comprehensive support and maintenance services to ensure the continued functionality and performance of our software solutions. Whether it's troubleshooting issues, implementing updates, or scaling infrastructure, our team is here to provide ongoing support to our clients."},
    {"question": "Does Inzint offer scalable solutions for businesses of all sizes?", "answer": "Absolutely! Inzint specializes in providing scalable solutions tailored to the unique needs and growth trajectories of businesses of all sizes. Whether you're a startup looking to launch a new product or an enterprise seeking to optimize your operations, we have the expertise to scale our solutions to meet your requirements."},
    {"question": "How quickly can Inzint deliver custom software solutions?", "answer": "The delivery timeline for custom software solutions can vary depending on the complexity of the project and specific client requirements. However, at Inzint, we prioritize efficiency and strive to deliver solutions in a timely manner without compromising on quality. We work closely with our clients to establish realistic timelines and keep them informed of progress every step of the way."},
    {"question": "Is Inzint experienced in developing solutions for specific industries?", "answer": "Yes, Inzint has extensive experience in developing software solutions for a wide range of industries, including healthcare, finance, retail, manufacturing, and more. Our team understands the unique challenges and requirements of each industry and leverages industry-specific expertise to deliver tailored solutions that address our clients' needs."},
    {"question": "What technologies does Inzint specialize in?", "answer": "Inzint specializes in a wide range of technologies, including but not limited to JavaScript, Python, Java, Swift, React, Angular, Node.js, AWS, Azure, Google Cloud Platform, Docker, Kubernetes, and more. Our team stays abreast of the latest technological advancements and leverages cutting-edge tools and frameworks to deliver innovative solutions."},
    {"question": "Can Inzint provide references or case studies of past projects?", "answer": "Absolutely! Inzint is proud of our track record of successful projects and satisfied clients. We can provide references or case studies upon request to showcase the quality of our work and the value we bring to our clients."},
    {"question": "Does Inzint offer consultation services for businesses exploring technology solutions?", "answer": "Yes, Inzint offers consultation services to businesses seeking guidance on technology solutions. Whether you're exploring new technologies, evaluating software vendors, or planning a digital transformation initiative, our experienced consultants can provide valuable insights and recommendations to help you make informed decisions."},
    {"question": "How does Inzint ensure seamless integration of software solutions with existing systems?", "answer": "At Inzint, we understand the importance of seamless integration with existing systems for our clients. We leverage industry best practices, robust APIs, and careful planning to ensure smooth integration of our software solutions with our clients' existing infrastructure and applications. Our goal is to minimize disruption and maximize efficiency throughout the integration process."},
    {"question": "Can Inzint provide training or documentation for using its software solutions?", "answer": "Yes, Inzint offers training and documentation services to ensure that our clients are equipped with the knowledge and resources they need to effectively use our software solutions. Whether it's user training sessions, comprehensive documentation, or ongoing support, we're committed to empowering our clients to get the most out of our solutions."},
    {"question": "How does Inzint stay updated on the latest technology trends?", "answer": "At Inzint, we prioritize continuous learning and professional development. Our team regularly attends industry conferences, participates in training programs, and engages in knowledge-sharing activities to stay updated on the latest technology trends and best practices. Additionally, we foster a culture of innovation and encourage our team members to explore new technologies and methodologies."},
    {"question": "What support options does Inzint offer for its software solutions?", "answer": "Inzint offers a range of support options to ensure that our clients receive the assistance they need when they need it. This includes dedicated support channels, ticket-based assistance, on-call support for emergencies, and more. Our goal is to provide prompt and effective support to address any issues or concerns our clients may have."},
    {"question": "Can Inzint provide assistance with software maintenance and updates?", "answer": "Yes, Inzint offers comprehensive software maintenance and update services to ensure that our clients' software solutions remain up-to-date, secure, and optimized for performance. Whether it's applying security patches, implementing feature enhancements, or performing routine maintenance tasks, our team is here to keep your software running smoothly."},
    {"question": "Is Inzint open to collaboration with other technology companies or service providers?", "answer": "Absolutely! Inzint believes in the power of collaboration and is open to partnering with other technology companies, service providers, and industry stakeholders to deliver innovative solutions to our clients. Whether it's joint ventures, strategic alliances, or technology partnerships, we're always looking for opportunities to collaborate and create value."},
    {"question": "What is Inzint's approach to project management?", "answer": "At Inzint, we follow agile project management methodologies to ensure transparency, flexibility, and efficiency throughout the project lifecycle. This includes iterative development, regular communication with stakeholders, continuous feedback loops, and adaptive planning. Our goal is to deliver high-quality solutions that meet our clients' evolving needs while staying on time and within budget."},
    {"question": "Can Inzint provide assistance with scaling software solutions as our business grows?", "answer": "Yes, Inzint offers scalability services to help businesses scale their software solutions as they grow. Whether it's optimizing infrastructure, adding new features, or expanding functionality to support increased demand, our team has the expertise and experience to ensure that your software solutions can scale seamlessly with your business."}]




# Initialize the text generation pipeline
text_generator = pipeline("text-generation", model="gpt2")

# Function to find the closest match between user query and questions in the data
def find_closest_match(user_query, data):
    best_match = None
    best_ratio = 0.60
    for item in data:
        question = item["question"]
        ratio = difflib.SequenceMatcher(None, user_query.lower(), question.lower()).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = item
    return best_match

# Streamlit app
def main():
    st.set_page_config(page_title="INFO INZ", page_icon=":bar_chart:", layout="wide")
    st.title("INFO INZ")
    st.sidebar.image("https://inzint.com/wp-content/uploads/2022/09/inzint-logo-dark.png", use_column_width=True)
    st.sidebar.markdown("Welcome to INFO INZ! Ask any question about our services.")

    # User input
    user_query = st.text_input("What are you looking for?")
    
    # Find the closest match
    closest_match = find_closest_match(user_query, data)
    
    if closest_match:
        st.subheader("Match found in data:")
        st.write("I found this question with the best match:", closest_match["question"])
        st.write("Answer:", closest_match["answer"])
        st.write("Response Source: Data, We found this info in our database.")
        
        # Add buttons for user feedback
        feedback = st.radio("Are you satisfied with the response?", ('Yes', 'No','Generate Response from GPT-2'))
        
        if feedback == 'Yes':
            st.write("Thank you for your feedback!")
        elif feedback == 'No':
            st.write("We'll try to improve the response next time.")
        elif feedback == 'Generate Response from GPT-2':
            # Generate answer using GPT-2 model
            generated_text = text_generator(user_query)[0]['generated_text']
            st.subheader("Disclaimer: GPT answers can be completely out of context, so keep your query specific!!!")
            st.write("Answer:", generated_text)
            st.write("Response Source: GPT-2")
    else: 
            generated_text = text_generator(user_query)[0]['generated_text']
            st.subheader("Disclaimer: GPT answers can be completely out of context, so keep your query specific!!!")
            st.write("Answer:", generated_text)
            st.write("Response Source: GPT-2")


if __name__ == "__main__":
    main()

