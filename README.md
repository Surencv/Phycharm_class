 Requisition Management System & Academic Performance Evaluator
 Project Summary
This repository showcases two Python-driven modules designed to streamline operational workflows and academic assessments:
1.	Requisition Management System – Facilitates staff requisition tracking, automates approval decisions, and generates summary statistics.
2.	Academic Performance Evaluator – Computes total and average scores, assigns academic grades, and determines pass/fail outcomes.
Both modules reflect core software engineering principles through modular architecture, encapsulated logic, and clean output formatting.
 Key Design Principles
1. Modular Architecture
Each module is structured into independent, reusable components:
•	The Requisition class encapsulates requisition-related data and behavior.
•	Methods like respond() and display() handle decision-making and presentation separately.
•	Academic functions such as calculate_average() and assign_grade() isolate computation from evaluation.
2. Encapsulation
•	Attributes like staff_id, items, and status are contained within the requisition class.
•	Internal mechanisms (e.g., approval reference generation) are abstracted from external access, preserving data integrity.
3. Single Responsibility Principle
Every function and method is designed to perform a distinct task:
•	respond() modifies requisition status.
•	show_statistics() aggregates and presents requisition metrics.
•	main() coordinates input/output flow without embedding business logic.
4. Scalability
•	Use of global counters and lists allows future integration with databases or persistent storage.
•	Flexible input handling is achieved through dynamic subject lists and keyword arguments (**scores).
5. Readability & Maintainability
•	Descriptive variable names (e.g., total_marks, average_marks, approval_ref) enhance clarity.
•	Inline comments guide the reader through each logical step.
•	Output formatting is consistent and user-friendly, supporting intuitive interpretation.
Git hub link:
https://github.com/Surencv/Phycharm_class

