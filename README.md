# Sample-Student-Survey
Sample Student Survey Analysis<br>
CS100 – Roadmap To Computing<br>

📌 Project Overview<br>
This project analyzes a dataset of 500 student survey responses modeled after an NJIT student experience survey. Each row represents one student’s responses, including both numeric ratings and open-ended feedback.<br>
The goal of the project is to clean messy real-world survey data and extract meaningful insights using Python.<br>

📁 Dataset Description<br>

15 quantitative questions<br>
Rating scale: 1–5<br>
1 = Very Dissatisfied<br>
5 = Very Satisfied<br>

3 qualitative (open-ended) questions<br>

The dataset contains invalid entries, such as:<br>
Blank cells or “NA”<br>
Numbers outside the valid range<br>
Typos and very short text responses<br>
Handling this messy data was a core part of the project.<br>

⚙️ What the Program Does<br>
Quantitative Analysis<br>
Cleans invalid numeric responses<br>
Normalizes ratings<br>
Calculates:<br>
Average rating for each category<br>
Category with the highest average rating<br>

Qualitative Analysis<br>
Processes open-ended responses<br>
Removes common stop words and punctuation<br>
Identifies:<br>
Most frequent keywords<br>
Most polarizing word (appearing frequently in both positive and negative feedback)<br>

🧠 Concepts & Skills Used<br>
File handling using Python’s csv module<br>
Dictionaries and lists<br>
Loops and conditionals<br>
String manipulation<br>
Data cleaning and validation<br>
Modular programming with functions<br>

▶️ How to Run<br>

Place the CSV file in an accessible location<br>
Run the script using IDLE or VS Code<br>
Enter the file location for input<br>
Call different variables to get the values<br>

🤝 Team & Credits<br>

This project was completed as a team final project for CS100.<br>
Kanika<br>
Remy Fortsch ( @SirLampsALot )<br>
Jester De Jesus<br>

All team members contributed to the design, logic, and implementation of the project.
